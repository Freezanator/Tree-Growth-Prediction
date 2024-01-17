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

    # Create a list of years to plot
    years = [2013, 2015, 2017, 2019, 2021, 2023]

    # Create a list of tabs with the year as the label
    tabs = [st.tabs(str(year)) for year in years]

    # Loop through the tabs and the years
    for tab, year in zip(tabs, years):
        # Use the tab as a context manager
        with tab:
            # Create a figure and an axis
            fig, ax = plt.subplots()
            # Plot the DBH of the year against the DBH class
            ax.plot(df["DBH Class"], df[str(year)], marker="o")
            # Set the title and the labels
            ax.set_title(f"DBH of {year} against the DBH class")
            ax.set_xlabel("DBH Class")
            ax.set_ylabel(f"DBH of {year}")
            # Display the figure using st.pyplot
            st.pyplot(fig)



if __name__ == "__main__":
    main()