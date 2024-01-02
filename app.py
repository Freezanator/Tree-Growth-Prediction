import streamlit as st
import pandas as pd

# Reads from the dataset
df = pd.read_csv('Data Pasoh Results.csv')

# Title
st.title('Pasoh DBH Prediction')

# Dropdown for selecting TAG
selected_tag = st.selectbox('Select TAG:', df['TAG'])

# Display selected row data horizontally
selected_row = df[df['TAG'] == selected_tag].squeeze()
st.write('Selected Row Data:')
st.write(pd.DataFrame(selected_row[['TAG', 'QUAD', 'XCO', 'YCO', 'DBH2017', 'DBH2019', 'DBH2021', 'DBH2023']]).transpose())

# Plot graph for selected TAG using st.line_chart
st.line_chart(selected_row[['DBH2017', 'DBH2019', 'DBH2021', 'DBH2023']])
