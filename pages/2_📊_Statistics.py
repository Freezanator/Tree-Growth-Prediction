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

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["2013", "2015", "2017", "2019", "2021", "2023"])

    with tab1:
        tab1.subheader("Graph of average DBH according to DBH Class in 2013")
        df1 = df[["DBH Class", "2013"]]
        st.bar_chart(df1.set_index("DBH Class"))

    with tab2:
        tab2.subheader("Graph of average DBH according to DBH Class in 2015")
        df2 = df[["DBH Class", "2015"]]
        st.bar_chart(df2.set_index("DBH Class"))

    with tab3:
        tab3.subheader("Graph of average DBH according to DBH Class in 2017")
        df3 = df[["DBH Class", "2017"]]
        st.bar_chart(df3.set_index("DBH Class"))

    with tab4:
        tab4.subheader("Graph of average DBH according to DBH Class in 2019")
        df4 = df[["DBH Class", "2019"]]
        st.bar_chart(df4.set_index("DBH Class"))

    with tab5:
        tab5.subheader("Graph of average DBH according to DBH Class in 2021")
        df5 = df[["DBH Class", "2021"]]
        st.bar_chart(df5.set_index("DBH Class"))

    with tab6:
        tab6.subheader("Graph of average DBH according to DBH Class in 2023")
        df6 = df[["DBH Class", "2023"]]
        st.bar_chart(df6.set_index("DBH Class"))



if __name__ == "__main__":
    main()