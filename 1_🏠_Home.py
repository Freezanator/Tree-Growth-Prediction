import streamlit as st
import pandas as pd
import folium
import plotly.express as px


def folium_static_map(m):
    width, height = 700, 400
    html = m.get_root().render()
    st.components.v1.html(html, width=width, height=height)

def main():
    st.title("Home")

    st.divider()

    st.subheader("Introduction")

    st.write("The Pasoh Forest Reserve is a nature reserve situated approximately 8 km from Simpang Pertang, Malaysia, and about 70 km southeast of Kuala Lumpur. It spans an area of 2,450 hectares, with a central zone of 600 hectares encircled by a buffer zone. The reserve is bordered by palm oil plantations on three sides, while a selectively logged dipterocarp forest adjoins the remaining side. The reserve receives an annual rainfall averaging 2 metres, with a range between 1,728 and 3,112 mm. In 1987, a 50-hectare forest dynamics plot was set up within the reserve. This initiative was a joint effort between the Forest Research Institute Malaysia, the Forest Global Earth Observatory (previously known as the Center for Tropical Forest Science), and the Smithsonian Tropical Research Institute. Since 1989, three censuses have been conducted in the plot, recording approximately 340,000 trees from 800 different species.")

    st.divider()
    
    st.subheader("Pasoh Forest Reserve Map")

    # Coordinates for Pasoh Forest Reserve
    pasoh_coords = (2.981981025774135, 102.31312029808895)

    # Create a Folium map centered around Pasoh Forest Reserve
    map_pasoh = folium.Map(location=pasoh_coords, zoom_start=10)

    # Add a marker for Pasoh Forest Reserve
    folium.Marker(location=pasoh_coords,
                  popup="Pasoh Forest Reserve").add_to(map_pasoh)

    # Display the map using st.write()
    folium_static_map(map_pasoh)


if __name__ == "__main__":
    main()
