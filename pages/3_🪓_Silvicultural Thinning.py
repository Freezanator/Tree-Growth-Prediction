import streamlit as st
import pandas as pd

def main():
    st.header("Silvicultural Thinning")

    st.write("Silvicultural thinning is a silvicultural operation where the main objective is to reduce the density of trees in a stand, improve the quality and growth of the remaining trees and produce a saleable product. Thinning can also achieve other objectives such as altering the species composition of a stand, improving the health of the remaining trees or disturbing an established ground flora to enhance opportunities for natural regeneration.")

    st.divider()

    st.write("The trees are classfied into the following 9 DBH classes:")

    # Create a dataframe from the list of lists
    df = pd.DataFrame({
        "DBH Class": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "DBH Range": ["<5cm", "5.1-10 cm", "10.1-20 cm","20.1-30 cm","30.1-40 cm","40.1-50 cm","50.1-60 cm","60.1-70 cm",">70 cm"]
    })
    st.dataframe(df, hide_index="True")

    st.divider()

    st.write("Select from 2 options of silvicultural thinning: Low Thinning or Crown Thinning.")

    tab1, tab2 = st.tabs(['Low Thinning', 'Crown Thinning'])

    