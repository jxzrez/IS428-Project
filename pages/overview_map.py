import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="HDB Resale Price Analysis - Overview Map")

st.title("HDB Resale Price Analysis - Overview Map")

# Tableau visualization URL
url1 = "https://public.tableau.com/views/HDBResalePriceAnalysis_17298503036490/OverviewDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

# Embed Tableau visualization
my_js = f"""
<script type="text/javascript" src="https://public.tableau.com/javascripts/api/tableau-2.min.js"></script>
<div id="vizContainer"></div>
<script>
    var containerDiv = document.getElementById('vizContainer');
    var url = "{url1}";
    var options = {{
        hideTabs: true,
        onFirstInteractive: function() {{
            console.log("Dashboard is interactive");
        }}
    }};
    var viz = new tableau.Viz(containerDiv, url, options);
</script>
"""
html(my_js, height=1350)