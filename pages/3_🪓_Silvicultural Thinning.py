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



if __name__ == "__main__":
    main()