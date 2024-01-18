import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def main():
    st.header('Digital Twin')

    # Load your dataset
    data = pd.read_csv('Data Pasoh TrainTest Featured OneZero.csv')
    data = data[['SPECIES', 'XCO', 'YCO', 'DBH2021', 'CLASS2021']]  # Considering 'DBH' as the column for Diameter at Breast Height

    # Filter out trees with DBH=0
    data = data[data['DBH2021'] != 0]

    # Map species to categorical values for color representation
    data['SP_category'] = pd.Categorical(data['SPECIES'])
    data['SP_code'] = data['SP_category'].cat.codes

    # Get unique species values for the selectbox
    species_list = data['SPECIES'].unique().tolist()

    def mapshow_3d_with_line(df, key):
        fig = go.Figure()

        # Add tree points in 3D scatter plot
        fig.add_trace(go.Scatter3d(
            x=df['XCO'], y=df['YCO'], z=df['DBH2021'],
            mode='markers',
            marker=dict(color=df['SP_code'], size=df['DBH2021'], colorscale='Viridis', colorbar=dict(title='SPECIES')),
            name='SPECIES'
        ))

        # Add lines from each tree to its top based on height
        for i, row in df.iterrows():
            fig.add_trace(go.Scatter3d(
                x=[row['XCO'], row['XCO']], y=[row['YCO'], row['YCO']],
                z=[0, row['DBH2021']],
                mode='lines',
                line=dict(color='#5E4C3E', width=3),
                showlegend=False
            ))

        # Update layout for larger plot
        fig.update_layout(
            scene=dict(
                xaxis_title='XCO Title',
                yaxis_title='YCO Title',
                zaxis_title='Tree DBH',
            ),
            title='3D Tree Locations with Heights and Lines Representing Tree Heights',
            width=800,  # Adjust the width of the plot
            height=800,  # Adjust the height of the plot
        )

        st.plotly_chart(fig, key=key)

    # Dropdown to select species
    selected_species = st.multiselect('Select Species to see their 3D location with height (Excluding DBH=0)',
                                    species_list, key='unique_key')

    if selected_species:
        filtered_df = data[data['Species'].isin(selected_species)]
        mapshow_3d_with_line(filtered_df, key='unique_chart')
    else:
        mapshow_3d_with_line(data, key='unique_chart')

        
if __name__ == "__main__":
    main()