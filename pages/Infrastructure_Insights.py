import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Infrastructure Insights", layout="wide")
st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stMainBlockContainer]{
        gap: 0rem;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Infrastructure Insights")

# New Tableau visualization URL
url = "https://public.tableau.com/views/FINALExtractDistancetofacilitiesadded/3_MRT?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

# Embed new Tableau visualization
my_js = f"""
<script type="text/javascript" src="https://public.tableau.com/javascripts/api/tableau-2.min.js"></script>
<div id="vizContainer" style="width:675px; height:1450px"></div>
<script>
    var containerDiv = document.getElementById('vizContainer');
    var url = "{url}";
    var options = {{
        hideTabs: true,
        onFirstInteractive: function() {{
            console.log("Dashboard is interactive");
        }}
    }};
    var viz = new tableau.Viz(containerDiv, url, options);
</script>
"""
html(my_js, height=900)