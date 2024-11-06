import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="HDB Resale Price Analysis - Overview Dashboard",layout="wide")
st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stMainBlockContainer]{
        gap: 0rem;
    }
    </style>
    """, unsafe_allow_html=True)
st.title("HDB Resale Price Analysis - Overview Dashboard")

# Tableau visualization URLs
url1 = "https://public.tableau.com/views/extractforjustinLiveDistancetofacilitiesadded/1_MapDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
url2 = "https://public.tableau.com/shared/2DSFNZYGP?:display_count=n&:origin=viz_share_link"
url3 = "https://public.tableau.com/shared/Z92XZSXQR?:display_count=n&:origin=viz_share_link"

# Embed first Tableau visualization
my_js1 = f"""
<script type="text/javascript" src="https://public.tableau.com/javascripts/api/tableau-2.min.js"></script>
<div id="vizContainer1""></div>
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
html(my_js1, height=1450)

# Embed second Tableau visualization
my_js2 = f"""
<script type="text/javascript" src="https://public.tableau.com/javascripts/api/tableau-2.min.js"></script>
<div id="vizContainer2"</div>
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
html(my_js2, height=850)

# Embed third Tableau visualization
my_js3 = f"""
<script type="text/javascript" src="https://public.tableau.com/javascripts/api/tableau-2.min.js"></script>
<div id="vizContainer3"></div>
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
html(my_js3, height=1200)