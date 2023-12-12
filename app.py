import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

# Plot graph for selected TAG
fig, ax = plt.subplots()
ax.plot(['D12', 'D15', 'D17', 'D19', 'D21', 'D23'], selected_row[['D12', 'D15', 'D17', 'D19', 'D21', 'D23']])
ax.set_title(f'DBH of TAG {selected_tag} from SP {selected_sp}')
ax.set_xlabel('Parameter')
ax.set_ylabel('Value')
st.pyplot(fig)