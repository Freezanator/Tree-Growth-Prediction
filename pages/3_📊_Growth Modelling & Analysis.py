import streamlit as st
import pandas as pd
import plotly.express as px

def map(df):
    # Convert 'SP' column to categorical
    df['SP'] = df['SP'].astype('category')

    fig = px.scatter(df, x='XCO', y='YCO', color='SP', color_discrete_sequence=px.colors.qualitative.Pastel, labels={'SP':'Species'})

    # Update title attributes
    fig.update_layout(
        title='Coordinates of Trees in 2021',
        xaxis_title='X-Coordinate',
        yaxis_title='Y-Coordinate'
    )

    st.plotly_chart(fig)

def distribution(df):
    # Create a plotly bar chart with custom font size and labels
    fig = px.bar(df, x="DBH Class", y="Count", text="Count")
    fig.update_layout(
        title="Bar Chart Example",
        xaxis_title="DBH Class",
        yaxis_title="Count",
        font=dict(size=18) # Change the font size for the whole chart
    )
    fig.update_xaxes(tickfont_size=16, tickmode='linear') # Change the font size for the x-axis ticks
    fig.update_yaxes(tickfont_size=16) # Change the font size for the y-axis ticks

    # Display the chart in Streamlit
    st.plotly_chart(fig)

def main():
    st.title("Growth Modelling & Analysis")
    st.title("")
    st.title("")

    st.header("Statistics")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total number of trees", "1944")

    with col2:
        st.metric("Total number of tree species", "379")

    st.divider()

    st.subheader("Tree Coordinate Map (as of 2021)")

    species_data = pd.read_csv('Species Coordinates.csv')
    df = pd.DataFrame(species_data)
    print(df.columns.str.strip())

    # Get unique species values for the selectbox
    species_list = ['ALL'] + sorted(df['SP'].unique().tolist())

    # Use selectbox to select species
    selected_species = st.selectbox('Select a species to view coordinates', species_list)

    # Show a plot of the selected species
    if selected_species != 'ALL':
        filtered_df = df[df['SP'] == selected_species]
        map(filtered_df)
    else:
        # Show a plot of all species
        map(df)

    st.title("")
    st.title("")
    st.header("Analysis")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Average growth from 2019 to 2021 (Actual)", value="+0.50 cm", delta="-0.03 cm")

    with col2:
        st.metric(label="Average growth from 2021 to 2023 (Predicted)", value="+0.59 cm", delta="+0.09 cm")

    st.divider()

    # Load the dataset
    df = pd.read_csv('Species Growth.csv')

    st.subheader("Growth Rates by Species")
    
    # Dropdown for species selection
    species = st.selectbox('Select a Species', df['SPECIES'].unique())

    # Filter the dataframe based on the selected species
    filtered_df = df[df['SPECIES'] == species]

    # Calculate the average values for each growth period
    average_growth1315 = filtered_df['GROWTH1315'].mean()
    average_growth1517 = filtered_df['GROWTH1517'].mean()
    average_growth1719 = filtered_df['GROWTH1719'].mean()
    average_growth1921 = filtered_df['GROWTH1921'].mean()
    average_growth2123 = filtered_df['GROWTH2123'].mean()

    # Preparing data for line chart
    chart_data = pd.DataFrame({
        'Growth Period': ['Growth 2013 - 2015', 'Growth 2015 - 2017', 'Growth 2017 - 2019', 'Growth 2019 - 2021', 'Growth 2021 - 2023'],
        'Average DBH': [average_growth1315, average_growth1517, average_growth1719, average_growth1921, average_growth2123]
    })

    # Display the line chart
    st.line_chart(chart_data.set_index('Growth Period'))

    st.divider()

    st.write("The trees are classfied into the following 9 DBH classes. The DBH classes range from <5cm up to >70cm (Shumi et al., 2019).")

    # Create a dataframe from the list of lists
    df = pd.DataFrame({
        "DBH Class": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "DBH Range": ["<5cm", "5.1-10 cm", "10.1-20 cm","20.1-30 cm","30.1-40 cm","40.1-50 cm","50.1-60 cm","60.1-70 cm",">70 cm"]
    })
    st.dataframe(df, hide_index="True")

    st.divider()

    st.subheader("Distribution of Trees in each DBH Class by Year")

    # Read the csv files
    df_2013 = pd.read_csv('DBH2013.csv')
    df_2015 = pd.read_csv('DBH2015.csv')
    df_2017 = pd.read_csv('DBH2017.csv')
    df_2019 = pd.read_csv('DBH2019.csv')
    df_2021 = pd.read_csv('DBH2021.csv')
    df_2023 = pd.read_csv('DBH2023.csv')

    # Create a tab container
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['2013', '2015', '2017', '2019', '2021', '2023 (Predicted)'])

    # Create a bar chart based on the selected tab
    with tab1:
        st.subheader(f"2013")
        distribution(df_2013)

    with tab2:
        st.subheader(f"2015")
        st.bar_chart(df_2015.set_index('DBH Class')) # Use streamlit's bar_chart and set the index to DBH Class
        st.markdown("<p style='text-align: center;'>DBH Class</p>", unsafe_allow_html=True)

    with tab3:
        st.subheader(f"2017")
        st.bar_chart(df_2017.set_index('DBH Class')) # Use streamlit's bar_chart and set the index to DBH Class
        st.markdown("<p style='text-align: center;'>DBH Class</p>", unsafe_allow_html=True)

    with tab4:
        st.subheader(f"2019")
        st.bar_chart(df_2019.set_index('DBH Class')) # Use streamlit's bar_chart and set the index to DBH Class
        st.markdown("<p style='text-align: center;'>DBH Class</p>", unsafe_allow_html=True)

    with tab5:
        st.subheader(f"2021")
        st.bar_chart(df_2021.set_index('DBH Class')) # Use streamlit's bar_chart and set the index to DBH Class
        st.markdown("<p style='text-align: center;'>DBH Class</p>", unsafe_allow_html=True)

    with tab6:
        st.subheader(f"2023 (Predicted)")
        st.bar_chart(df_2023.set_index('DBH Class')) # Use streamlit's bar_chart and set the index to DBH Class
        st.markdown("<p style='text-align: center;'>DBH Class</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()