import streamlit as st
import pandas as pd

def main():
    st.title("Silvicultural Thinning")

    st.divider()

    st.header("What is Silvicultural Thinning?")

    st.write("Silvicultural thinning is an operation where the main objective is to reduce the density of trees in a stand, improve the quality and growth of the remaining trees and produce a saleable product. Thinning can also achieve other objectives such as altering the species composition of a stand, improving the health of the remaining trees or disturbing an established ground flora to enhance opportunities for natural regeneration.")

    st.divider()

    st.write("Select a type of silvicultural thinning.")

    tab1, tab2 = st.tabs(['Low Thinning', 'Crown Thinning'])

    # Load the CSV files
    low_trees = pd.read_csv('Plot Low Trees.csv')
    crown_trees = pd.read_csv('Plot Crown Trees.csv')

    # Create the buttons
    low_button = st.button('Low Thinning')
    crown_button = st.button('Crown Thinning')

    # Display the plot chart based on the button clicked
    if low_button:
        fig = px.line(low_trees, x='x', y='y', title='Low Thinning Plot')
        st.plotly_chart(fig)
    elif crown_button:
        fig = px.line(crown_trees, x='x', y='y', title='Crown Thinning Plot')
        st.plotly_chart(fig)
    else:
        st.write('Please select a button to see the plot chart.')



if __name__ == "__main__":
    main()