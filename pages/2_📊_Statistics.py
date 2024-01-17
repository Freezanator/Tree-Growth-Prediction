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
    tab_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Create a list of tabs using st.tabs
    tabs = st.tabs(tab_names)

    # Loop through the tabs and the df columns
    for i in range(len(tabs)):
        # Get the current tab and the corresponding df column
        tab = tabs[i]
        col = df.columns[i+1]

        # Use the tab as a context manager
        with tab:
            # Create a subheader with the column name
            tab.subheader(f"Graph of average DBH according to DBH Class in {col}")
            # Filter the dataframe to only keep the columns for DBH class and the current column
            df_filtered = df[["DBH Class", col]]
            # Create a bar chart to show the DBH against DBH class
            st.bar_chart(df_filtered.set_index("DBH Class"))



if __name__ == "__main__":
    main()