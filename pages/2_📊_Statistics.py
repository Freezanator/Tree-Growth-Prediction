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

    # Import streamlit and pandas
    import streamlit as st
    import pandas as pd

    # Load the dataset
    df = pd.read_csv("DBH Classes.csv")

    # Create a container for the tabs
    tabs = st.tabs(["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7", "Class 8", "Class 9"])

    # Loop through each tab and plot the average DBH for the corresponding class
    for i in range(1, 10):
        with tabs[i-1]:

            # Filter the dataset by the selected DBH class
            df_class = df[df[f"{i}"] == 1]

            # Calculate the average DBH for each year
            avg_dbh = df_class.mean(axis=0)[:6]

            # Plot the average DBH over the years
            st.title(f"Average DBH for class {i}")
            st.line_chart(avg_dbh)



if __name__ == "__main__":
    main()