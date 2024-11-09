import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="IS428 Project", layout="wide")
st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stMainBlockContainer]{
        gap: 0rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Automatically set the query parameter to open overview_map.py
st.experimental_set_query_params(page="overview_map")

# Load the Overview Map page content
st.title("HDB Resale Price Analysis - Overview Map")

# First Tableau visualization URL
url1 = "https://public.tableau.com/views/FINALExtractDistancetofacilitiesadded/1_MapDashboard?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

# Embed first Tableau visualization
my_js1 = f"""
<script type="text/javascript" src="https://public.tableau.com/javascripts/api/tableau-2.min.js"></script>
<div id="vizContainer1" style="width:675px; height:1450px"></div>
<script>
    var containerDiv = document.getElementById('vizContainer1');
    var url = "{url1}";
    var options = {{
        hideTabs: true,
        onFirstInteractive: function() {{
            console.log("Dashboard 1 is interactive");
        }}
    }};
    var viz = new tableau.Viz(containerDiv, url, options);
</script>
"""
html(my_js1, height=800)

# Second Tableau visualization URL
url2 = "https://public.tableau.com/views/FINALExtractDistancetofacilitiesadded/1_TreemapDashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

# Embed second Tableau visualization
my_js2 = f"""
<script type="text/javascript" src="https://public.tableau.com/javascripts/api/tableau-2.min.js"></script>
<div id="vizContainer2" style="width:675px; height:1450px"></div>
<script>
    var containerDiv = document.getElementById('vizContainer2');
    var url = "{url2}";
    var options = {{
        hideTabs: true,
        onFirstInteractive: function() {{
            console.log("Dashboard 2 is interactive");
        }}
    }};
    var viz = new tableau.Viz(containerDiv, url, options);
</script>
"""
html(my_js2, height=830)

# Third Tableau visualization URL
url3 = "https://public.tableau.com/views/FINALExtractDistancetofacilitiesadded/1_TimeSeries?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

# Embed third Tableau visualization
my_js3 = f"""
<script type="text/javascript" src="https://public.tableau.com/javascripts/api/tableau-2.min.js"></script>
<div id="vizContainer3" style="width:675px; height:1450px"></div>
<script>
    var containerDiv = document.getElementById('vizContainer3');
    var url = "{url3}";
    var options = {{
        hideTabs: true,
        onFirstInteractive: function() {{
            console.log("Dashboard 3 is interactive");
        }}
    }};
    var viz = new tableau.Viz(containerDiv, url, options);
</script>
"""
html(my_js3, height=850)