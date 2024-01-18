import streamlit as st
import pandas as pd

def main():
    st.header('Statistics')

    st.title("")
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Average growth from 2019 to 2021 (Actual)", value="+0.50 cm", delta="-0.03 cm")

    with col2:
        st.metric(label="Average growth from 2021 to 2023 (Predicted)", value="+0.59 cm", delta="+0.09 cm")

    st.divider()

    st.write("The trees are classfied into the following 9 DBH classes:")

    # Create a dataframe from the list of lists
    df = pd.DataFrame({
        "DBH Class": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "DBH Range": ["<5cm", "5.1-10 cm", "10.1-20 cm","20.1-30 cm","30.1-40 cm","40.1-50 cm","50.1-60 cm","60.1-70 cm",">70 cm"]
    })
    st.dataframe(df, hide_index="True")

    st.divider()

    # Load the dataset
    df = pd.read_csv("DBH Classes.csv")

    # Create a list of tab names
    tab_names = [f"DBH Class {i}" for i in range(1, 10)]

    # Create a list of column names
    col_names = [str(i) for i in range(1, 10)]

    # Create a tabs container using st.tabs()
    tabs = st.tabs(tab_names)

    # Loop through each tab and column
    for tab, col in zip(tabs, col_names):
        # Select the tab
        with tab:
            # Create a bar chart using st.bar_chart()
            st.subheader(f"Average DBH of trees in DBH Class {col}")
            st.bar_chart(df[["Year", col]].set_index("Year"))



if __name__ == "__main__":
    main()