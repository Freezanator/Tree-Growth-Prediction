import streamlit as st
import pandas as pd
import folium
import plotly.express as px
from st_pages import Page, show_pages, add_page_title

add_page_title()

show_pages(
    [
        Page("Home.py", "Home"),
        Page("pages/Statistics.py", "Statistics"),
        Page("pages/DigitalTwin.py", "Digital Twin"),
    ]
)


def folium_static_map(m):
    width, height = 700, 400
    html = m.get_root().render()
    st.components.v1.html(html, width=width, height=height)

def map(df):
    # Convert 'SP' column to categorical
    df['SP'] = df['SP'].astype('category')

    fig = px.scatter(df, x='XCO', y='YCO', color='SP')

    # Update title attributes
    fig.update_layout(
        title='Coordinates of Trees in 2021',
        xaxis_title='X-Coordinate',
        yaxis_title='Y-Coordinate'
    )

    st.plotly_chart(fig)


def main():
    st.header("Introduction")

    st.write("The Pasoh Forest Reserve is a nature reserve situated approximately 8 km from Simpang Pertang, Malaysia, and about 70 km southeast of Kuala Lumpur. It spans an area of 2,450 hectares, with a central zone of 600 hectares encircled by a buffer zone. The reserve is bordered by palm oil plantations on three sides, while a selectively logged dipterocarp forest adjoins the remaining side. The reserve receives an annual rainfall averaging 2 metres, with a range between 1,728 and 3,112 mm. In 1987, a 50-hectare forest dynamics plot was set up within the reserve. This initiative was a joint effort between the Forest Research Institute Malaysia, the Forest Global Earth Observatory (previously known as the Center for Tropical Forest Science), and the Smithsonian Tropical Research Institute. Since 1989, three censuses have been conducted in the plot, recording approximately 340,000 trees from 800 different species.")

    st.title("")
    st.header("Pasoh Forest Reserve Map")

    # Coordinates for Pasoh Forest Reserve
    pasoh_coords = (2.981981025774135, 102.31312029808895)

    # Create a Folium map centered around Pasoh Forest Reserve
    map_pasoh = folium.Map(location=pasoh_coords, zoom_start=10)

    # Add a marker for Pasoh Forest Reserve
    folium.Marker(location=pasoh_coords,
                  popup="Pasoh Forest Reserve").add_to(map_pasoh)

    # Display the map using st.write()
    folium_static_map(map_pasoh)

    st.title("")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total number of trees", "1944")

    with col2:
        st.metric("Total number of tree species", "379")

    st.title("")
    st.header("Tree Coordinate Map (as of 2021)")

    data = pd.read_csv('Species Coordinates.csv')
    df = pd.DataFrame(data)
    print(df.columns.str.strip())

    # Get unique species values for the selectbox
    species_list = df['SP'].unique().tolist()

    selected_species = st.selectbox('Select a species to view coordinates', species_list)

    # Show a plot of selected species
    if selected_species:
        filtered_df = df[df['SP'].isin(selected_species)]
        map(filtered_df)
    else:
    # Show a plot of all species
        map(df)


if __name__ == "__main__":
    main()
