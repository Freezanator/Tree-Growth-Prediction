import streamlit as st
import pandas as pd
import folium
from st_pages import Page, show_pages, add_page_title

def main():
    st.title("Interactive Map with Streamlit and Folium")
    st.header("Pasoh Reserve Forest Location")

    # Create a Folium map
    m = folium.Map(
        location=[2.981981025774135, 102.31312029808895],  # Replace with your desired initial location
        zoom_start=12,  # Adjust the zoom level as needed
    )

    # Display the map in Streamlit using HTML
    st.write("### Interactive Map:")
    folium_static(m)

if __name__ == "__main__":
    main()
