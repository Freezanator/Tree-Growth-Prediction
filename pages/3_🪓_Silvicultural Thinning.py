import streamlit as st
import pandas as pd

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
        fig = px.line(low_trees, x='x', y='y', title='Low Thinning Plot')
        st.plotly_chart(fig)
    elif button2:
        fig = px.line(crown_trees, x='x', y='y', title='Crown Thinning Plot')
        st.plotly_chart(fig)



if __name__ == "__main__":
    main()