import streamlit as st

st.set_page_config(page_title="IS428 Project", layout="wide")
st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stMainBlockContainer]{
        gap: 0rem;
    }
    </style>
    """,unsafe_allow_html=True)

# Automatically set the query parameter to open overview_map.py
st.experimental_set_query_params(page="overview_map")

# Load the Overview Map page content
st.title("HDB Resale Price Analysis - Overview Map")
st.write("Please select the appropriate page from the sidebar.")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.") 