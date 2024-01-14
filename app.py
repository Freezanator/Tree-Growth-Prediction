import streamlit as st
import pandas as pd
import folium
from st_pages import Page, show_pages, add_page_title

add_page_title()

show_pages(
	[
		Page("app.py", "Home")
		Page("pages/Statistics.py", "Statistics")
		Page("pages/DigitalTwin.py", "Digital Twin")
	]
)

def main():
	st.title("Pasoh Forest Reserve Map")
	
	# Coordinates for Pasoh Forest Reserve
	pasoh_coords = (2.981981025774135, 102.31312029808895)
	
	# Create a Folium map centered around Pasoh Forest Reserve
	map_pasoh = folium.Map(location = pasoh_coords, zoom_start = 10)
	
	# Add a marker for Pasoh Forest Reserve
	folium.Marker(location = pasoh_coords, popup = "Pasoh Forest Reserve").add_to(map_pasoh)
	
	# Display the map using st.write()
	folium_static_map(map_pasoh)


def folium_static_map(m):
	width, height = 700, 400
	html = m.get_root().render()
	st.components.v1.html(html, width = width, height = height)


if __name__ == "__main__":
	main()