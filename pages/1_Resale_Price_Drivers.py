import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Resale Price Drivers", layout="wide")
st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stMainBlockContainer]{
        gap: 0rem;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Resale Price Drivers")

# First Tableau visualization URL
url1 = "https://public.tableau.com/views/AnalysisofSingaporesHDBResalePrices1990-2023/2_MatrixDashboard1?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

st.markdown("## Scatter Plot Matrix 1")
st.markdown("##### A scatterplot matrix of various features of housing against resale price. Noteworthy relationships are Remaining Lease & Floor Area Sqm correlating with resale price. MRT, School & Mall analysis is on the “Infrastructure Insights” page.")
st.markdown("*Use the filters to adjust the year range, flat type, and town of interest. Hover over the trendline to view the R-squared value, which indicates how well this variable can explain variations in resale price.*")

# Embed first Tableau visualization
my_js1 = f"""
<script type="text/javascript" src="https://public.tableau.com/javascripts/api/tableau-2.min.js"></script>
<div id="vizContainer1" style="width:1200px; height:675px"></div>
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
url2 = "https://public.tableau.com/views/AnalysisofSingaporesHDBResalePrices1990-2023/2_MatrixDashboard2?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

st.subheader("", divider="orange")
st.markdown("## Scatter Plot Matrix 2")
st.markdown("##### Another matrix of Storey range plotted against resale price. Noteworthy relations are that for most towns, an identical flat above the 15th story can easily command a price twice that of lower floors. Employment rate and Interest rate show no clear correlation relationship.")
st.markdown("*Use the filters at the top to adjust the range of years, type of flat and town that you are interested in investigating (For storey-range, optimal analysis would be 7 towns at a time for neatness). Hovering over the graphs and trend lines will give additional information*")

# Embed second Tableau visualization
my_js2 = f"""
<script type="text/javascript" src="https://public.tableau.com/javascripts/api/tableau-2.min.js"></script>
<div id="vizContainer2" style="width:675px; height:1200px"></div>
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
html(my_js2, height=1200)