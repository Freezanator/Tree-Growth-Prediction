import streamlit as st
import pandas as pd
import folium
from st_pages import Page, show_pages, add_page_title

add_page_title()

show_pages(
	[
		Page("app.py", "Home"),
		Page("pages/Statistics.py", "Statistics"),
		Page("pages/DigitalTwin.py", "Digital Twin"),
	]
)

def main():

	st.header("Introduction")

	st.write("The Pasoh Forest Reserve, a nature reserve located about 8 km from Simpang Pertang, Malaysia and around 70 km southeast of Kuala Lumpur. It has a total area of 2,450 hectares, with a core area of 600 ha surrounded by a buffer zone. Palm oil plantations surround the reserve on three sides while the other side adjoins a selectively logged dipterocarp forest. An average of 2 metres of rain fall each year, ranging from 1,728 to 3,112 mm.[1] In 1987, a 50 hectare forest dynamics plot was established in the reserve,[2] which began as a collaboration between the Forest Research Institute Malaysia, the Forest Global Earth Observatory (ForestGEO; previously Center for Tropical Forest Science),[3] and the Smithsonian Tropical Research Institute.[4] Three censuses of the tree population in the plot have been carried out, the first in 1989, and have counted about 340,000 trees belonging to 800 species in that plot.")
	
	st.header("Pasoh Forest Reserve Map")
	
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