import streamlit as st

def main():
	st.header('Statistics')

col1, col2 = st.columns(2)
    
with col1:
    st.metric(label="Average growth of 2019 to 2021 (Actual)", value="+0.57 cm", delta="+0.07 cm")

with col2:
    st.metric(label="Average growth of 2021 to 2023 (Predicted)", value="+0.58 cm", delta="+0.01 cm")

if __name__ == "__main__":
    main()