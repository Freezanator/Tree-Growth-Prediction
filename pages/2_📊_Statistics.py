import streamlit as st
import pandas as pd

def main():
    st.header('Statistics')

    st.title("")
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Average growth from 2019 to 2021 (Actual)", value="+0.57 cm", delta="+0.07 cm")

    with col2:
        st.metric(label="Average growth from 2021 to 2023 (Predicted)", value="+0.58 cm", delta="+0.01 cm")

    st.divider()

    st.write("The trees are classfied into the following 9 DBH classes:")

    # Create a list of lists with the data values
    data = [
        ["DBH Class", "DBH Range"],
        ["1", "<5 cm"],
        ["2", "5.1-10 cm"],
        ["3", "10.1-20 cm"],
        ["4", "20.1-30 cm"],
        ["5", "30.1-40 cm"],
        ["6", "40.1-50 cm"],
        ["7", "50.1-60 cm"],
        ["8", "60.1-70 cm"],
        ["9", ">70 cm"],
    ]

    # Create a dataframe from the list of lists
    df = pd.DataFrame(data)

    st.dataframe(df, hide_index="True")


if __name__ == "__main__":
    main()