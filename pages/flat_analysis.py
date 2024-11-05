import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="HDB Resale Price Analysis - Flat Analysis")

st.title("HDB Resale Price Analysis - Flat Analysis")

# Tableau visualization URL
url3 = "https://public.tableau.com/shared/7P4YHXJS5?:display_count=n&:origin=viz_share_link"

# Embed Tableau visualization
my_js = f"""
<script type="text/javascript" src="https://public.tableau.com/javascripts/api/tableau-2.min.js"></script>
<div id="vizContainer" style="height: 800px;"></div>
<script>
    var containerDiv = document.getElementById('vizContainer');
    var url = "{url3}";
    var options = {{
        hideTabs: true,
        onFirstInteractive: function() {{
            console.log("Dashboard is interactive");
        }}
    }};
    var viz = new tableau.Viz(containerDiv, url, options);
</script>
"""
html(my_js, height=850, width=1000)