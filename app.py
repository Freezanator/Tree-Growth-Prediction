import streamlit as st
import pandas as pd
import plotly.express as px

# Reads from the dataset
df = pd.read_csv('Results Data Pasoh.csv')

# Title
st.title('Pasoh DBH Prediction')

# Dropdown for selecting SP
selected_sp = st.selectbox('Select SP:', df['SP'].unique())

# Filter DataFrame based on selected SP
filtered_df = df[df['SP'] == selected_sp]

# Dropdown for selecting TAG
selected_tag = st.selectbox('Select TAG:', filtered_df['TAG'])

# Display selected row data horizontally
selected_row = filtered_df[filtered_df['TAG'] == selected_tag].squeeze()
st.write('Selected Row Data:')
st.write(pd.DataFrame(selected_row[['TAG', 'QUAD', 'XCO', 'YCO', 'D12', 'D15', 'D17', 'D19', 'D21', 'D23']]).transpose())

# Create a custom Plotly Express line chart
fig = px.line(
    selected_row,
    x=['D12', 'D15', 'D17', 'D19', 'D21', 'D23'],
    y=[selected_row['D12'], selected_row['D15'], selected_row['D17'], selected_row['D19'], selected_row['D21'], selected_row['D23']],
    labels={'x': 'Parameter', 'y': 'Value'},
    title=f'Data Points for {selected_tag}'
)

# Customize axis labels and rename D23
fig.update_xaxes(title_text='Custom D-Axis', ticktext=['D12', 'D15', 'D17', 'D19', 'D21', 'D23'], tickvals=['D12', 'D15', 'D17', 'D19', 'D21', 'D23'])
fig.update_yaxes(title_text='Custom Value-Axis')

# Display the customized Plotly Express chart
st.plotly_chart(fig)