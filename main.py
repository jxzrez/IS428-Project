import streamlit as st

st.set_page_config(page_title="HDB Resale Price Analysis", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview Map", "Overview Dashboard", "Flat Analysis", "Predict Price"])

if page == "Overview Map":
    st.experimental_set_query_params(page="overview_map")
    st.title("HDB Resale Price Analysis - Overview Map")
    st.write("Please select the appropriate page from the sidebar.")
elif page == "Overview Dashboard":
    st.experimental_set_query_params(page="overview_dashboard")
    st.title("HDB Resale Price Analysis - Overview Dashboard")
    st.write("Please select the appropriate page from the sidebar.")
elif page == "Flat Analysis":
    st.experimental_set_query_params(page="flat_analysis")
    st.title("HDB Resale Price Analysis - Flat Analysis")
    st.write("Please select the appropriate page from the sidebar.")
elif page == "Predict Price":
    st.experimental_set_query_params(page="predict_price")
    st.title("Predict HDB Resale Price")
    st.write("Please select the appropriate page from the sidebar.")