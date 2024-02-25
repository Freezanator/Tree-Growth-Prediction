import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import altair as alt


def map(df2):
    # Convert 'SP' column to categorical
    df2['SPECIES'] = df2['SPECIES'].astype('category')

    fig = px.scatter(df2, x='XCO', y='YCO', color='SPECIES', color_discrete_sequence=px.colors.qualitative.Pastel, labels={'SPECIES':'Species'})

    # Update title attributes
    fig.update_layout(
        title='Location of Trees to be Harvested',
        xaxis_title='X-Coordinate',
        yaxis_title='Y-Coordinate'
    )

    st.plotly_chart(fig)

def mapshow_3d_with_line(df, key):
    fig = go.Figure()

    # Add tree points in 3D scatter plot
    fig.add_trace(go.Scatter3d(
        x=df['XCO'], y=df['YCO'], z=df['DBH2023'],
        mode='markers',
        marker=dict(color=df['SP_code'], size=df['DBH2023'], colorscale='Viridis', colorbar=dict(title='SPECIES')),
        name=''
    ))

    # Add lines from each tree to its top based on height
    for i, row in df.iterrows():
        fig.add_trace(go.Scatter3d(
            x=[row['XCO'], row['XCO']], y=[row['YCO'], row['YCO']],
            z=[0, row['DBH2023']],
            mode='lines',
            line=dict(color='#5E4C3E', width=3),
            showlegend=False
        ))

    # Update layout for larger plot
    fig.update_layout(
        scene=dict(
            xaxis_title='X-Coordinate',
            yaxis_title='Y-Coordinate',
            zaxis_title='Tree DBH',
        ),
        title='Location of Trees to be Harvested in 3D',
        width=800,  # Adjust the width of the plot
        height=800,  # Adjust the height of the plot
    )

    st.plotly_chart(fig, key=key)
    
def main():
    st.title('Silvicultural Thinning')

    st.divider()

    st.subheader('What is Silvicultural Thinning?')

    st.write('Silvicultural thinning is an operation where the main objective is to reduce the density of trees in a stand, improve the quality and growth of the remaining trees and produce a saleable product. Thinning can also achieve other objectives such as altering the species composition of a stand, improving the health of the remaining trees or disturbing an established ground flora to enhance opportunities for natural regeneration (Kerr & Haufe, 2011).')

    st.divider()

    st.subheader('DBH Class Distribution in 2023 after Thinning')

    intensity = st.select_slider('Select a thinning intensity', options = ['Very Mild', 'Mild', 'Moderate', 'Intense', 'Very Intense'])
        
    # Load data from csv
    if intensity == 'Very Mild':
        df1 = pd.read_csv('Thinning Bar 1.csv')

    elif intensity == 'Mild':
        df1 = pd.read_csv('Thinning Bar 2.csv')
            
    elif intensity == 'Moderate':
        df1 = pd.read_csv('Thinning Bar 3.csv')

    elif intensity == 'Intense':
        df1 = pd.read_csv('Thinning Bar 4.csv')

    elif intensity == 'Very Intense':
        df1 = pd.read_csv('Thinning Bar 5.csv')

    # Melt the dataframe to long format
    df_long = pd.melt(df1, id_vars='DBH Class', value_vars=['Harvested', 'Remaining'], var_name='Count', value_name='Value')

    # Create the stacked bar chart using Altair
    chart = alt.Chart(df_long).mark_bar().encode(
        x=alt.X('DBH Class:N', title='DBH Class'),
        y=alt.Y('Value:Q', title='Count'),
        color=alt.Color('Count:N', title='Count')
    )

    # Display the chart using Streamlit
    st.altair_chart(chart, use_container_width=True)

    st.divider()

    if intensity == 'Very Mild':
        lowtrees = pd.read_csv('Thinning Scatter 1.csv')

    elif intensity == 'Mild':
        lowtrees = pd.read_csv('Thinning Scatter 2.csv')
        
    elif intensity == 'Moderate':
        lowtrees = pd.read_csv('Thinning Scatter 3.csv')

    elif intensity == 'Intense':
        lowtrees = pd.read_csv('Thinning Scatter 4.csv')

    elif intensity == 'Very Intense':
        lowtrees = pd.read_csv('Thinning Scatter 5.csv')

    st.subheader("Table of Trees to be Thinned")

    # Display the DataFrame as a table
    lowtrees_renamed = lowtrees.rename(columns={"SPECIES": "Species", "XCO": "X Coordinate", "YCO": "Y Coordinate", "DBH2023": "DBH", "GROWTH2123": "Growth Rate", "CLASS2023": "DBH Class"})
    lowtrees_sorted = lowtrees_renamed.sort_values(by="DBH Class", ascending=True)
    st.dataframe(lowtrees_sorted, height=100)
    st.table(lowtrees_sorted)

    data = lowtrees[['SPECIES', 'XCO', 'YCO', 'DBH2023', 'CLASS2023']]  # Considering 'DBH' as the column for Diameter at Breast Height

    # Filter out trees with DBH=0
    data = data[data['DBH2023'] != 0]

    # Map species to categorical values for color representation
    data['SP_category'] = pd.Categorical(data['SPECIES'])
    data['SP_code'] = data['SP_category'].cat.codes

    mapshow_3d_with_line(data, key='unique_chart')


if __name__ == '__main__':
    main()