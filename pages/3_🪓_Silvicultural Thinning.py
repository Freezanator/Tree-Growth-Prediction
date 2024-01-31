import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt


def map(df):
    # Convert 'SP' column to categorical
    df['SP'] = df['SP'].astype('category')

    fig = px.scatter(df, x='XCO', y='YCO', color='SP', color_discrete_sequence=px.colors.qualitative.Pastel, labels={'SP':'Species'})

    # Update title attributes
    fig.update_layout(
        title='Coordinates of Trees in 2021',
        xaxis_title='X-Coordinate',
        yaxis_title='Y-Coordinate'
    )

    st.plotly_chart(fig)


def main():
    st.title("Silvicultural Thinning")

    st.divider()

    st.header("What is Silvicultural Thinning?")

    st.write("Silvicultural thinning is an operation where the main objective is to reduce the density of trees in a stand, improve the quality and growth of the remaining trees and produce a saleable product. Thinning can also achieve other objectives such as altering the species composition of a stand, improving the health of the remaining trees or disturbing an established ground flora to enhance opportunities for natural regeneration.")

    st.divider()

    st.write("Please select a type of silvicultural thinning.")
    
    # Load the CSV files
    low_trees = pd.read_csv('Plot Low Trees.csv')
    crown_trees = pd.read_csv('Plot Crown Trees.csv')

    col1, col2 = st.columns(2) # Create two columns
    button1 = col1.button('Low Thinning') # Assign the first button to the first column
    button2 = col2.button('Crown Thinning') # Assign the second button to the second column

    # Display the plot chart based on the button clicked
    if button1:
        # Load data from csv
        df = pd.read_csv ("data.csv")

        # Transform data to long format
        df_long = pd.melt (df, id_vars= ["DBH Class"], value_vars= ["Harvested", "Remaining"], var_name= "Legend", value_name= "Count")

        # Create Altair chart
        chart = alt.Chart (df_long).mark_bar ().encode (
            x= alt.X ("DBH Class:N", sort= alt.Sort (order= "descending")), # Use DBH Class as x axis and sort in descending order
            y= alt.Y ("Count:Q", stack= "zero"), # Use Count as y axis and stack by zero baseline
            color= alt.Color ("Year:N") # Use Year as color
        )

        # Display chart in Streamlit
        st.altair_chart (chart, use_container_width= True)


    elif button2:
        fig = px.line(crown_trees, x='x', y='y', title='Crown Thinning Plot')
        st.plotly_chart(fig)


if __name__ == "__main__":
    main()