import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt


def map(df2):
    # Convert 'SP' column to categorical
    df2['SPECIES'] = df2['SPECIES'].astype('category')

    fig = px.scatter(df2, x='XCO', y='YCO', color='SPECIES', color_discrete_sequence=px.colors.qualitative.Pastel, labels={'SPECIES':'Species'})

    # Update title attributes
    fig.update_layout(
        title='Location of Trees to be Harvested',
        xaxis_title='X-Coordinate',
        yaxis_title='Y-Coordinate'
    )

    st.plotly_chart(fig)


def main():
    st.title('Silvicultural Thinning')

    st.divider()

    st.subheader('What is Silvicultural Thinning?')

    st.write('Silvicultural thinning is an operation where the main objective is to reduce the density of trees in a stand, improve the quality and growth of the remaining trees and produce a saleable product. Thinning can also achieve other objectives such as altering the species composition of a stand, improving the health of the remaining trees or disturbing an established ground flora to enhance opportunities for natural regeneration.')

    st.divider()

    st.subheader('DBH Class Distribution after Thinning')

    intensity = st.select_slider('Select a thinning intensity', options = ['Very Mild', 'Mild', 'Moderate', 'Intense', 'Very Intense'])
        
    # Load data from csv
    if intensity == 'Very Mild':
        df1 = pd.read_csv('Thinning Bar 1.csv')

    elif intensity == 'Mild':
        df1 = pd.read_csv('Thinning Bar 2.csv')
            
    elif intensity == 'Moderate':
        df1 = pd.read_csv('Thinning Bar 3.csv')

    elif intensity == 'Intense':
        df1 = pd.read_csv('Thinning Bar 4.csv')

    elif intensity == 'Very Intense':
        df1 = pd.read_csv('Thinning Bar 5.csv')

    # Melt the dataframe to long format
    df_long = pd.melt(df1, id_vars='DBH Class', value_vars=['Harvested', 'Remaining'], var_name='Count', value_name='Value')

    # Create the stacked bar chart using Altair
    chart = alt.Chart(df_long).mark_bar().encode(
        x=alt.X('DBH Class:N', title='DBH Class'),
        y=alt.Y('Value:Q', title='Count'),
        color=alt.Color('Count:N', title='Count')
    )

    # Display the chart using Streamlit
    st.altair_chart(chart, use_container_width=True)

    if intensity == 'Very Mild':
        lowtrees = pd.read_csv('Thinning Scatter 1.csv')

    elif intensity == 'Mild':
        lowtrees = pd.read_csv('Thinning Scatter 2.csv')
        
    elif intensity == 'Moderate':
        lowtrees = pd.read_csv('Thinning Scatter 3.csv')

    elif intensity == 'Intense':
        lowtrees = pd.read_csv('Thinning Scatter 4.csv')

    elif intensity == 'Very Intense':
        lowtrees = pd.read_csv('Thinning Scatter 5.csv')

    df2 = pd.DataFrame(lowtrees)
    map(df2)


if __name__ == '__main__':
    main()