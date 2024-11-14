import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Resale Market Overview and Trends", layout="wide")
st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stMainBlockContainer]{
        gap: 0rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the Overview Map page content
st.title("Resale Market Overview and Trends")

# Caption 
st.markdown("## Map Dashboard")
st.markdown("##### The Housing Affordability Ratio or HFI is a measure of affordability by taking the ratio of the house price to total annual income. A HFI above 5 is considered unaffordable and the number generally indicates the number of years needed to save for a house without taking loans.")

# First Tableau visualization URL
url1 = "https://public.tableau.com/views/AnalysisofSingaporesHDBResalePrices1990-2023/1_MapDashboard?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

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

st.subheader("", divider="orange")
st.markdown("## Treemap Dashboard")
st.markdown("##### Treemap displays the proportion of all flats sold by town, including the average resale price")
st.markdown("""
    *Identify the region you are interested in. Hover over your desired area and you will be able to see the town, flat type and average resale price. The resale price is color-coded in the top right corner.*
    """)
# Second Tableau visualization URL
url2 = "https://public.tableau.com/views/AnalysisofSingaporesHDBResalePrices1990-2023/1_TreemapDashboard?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

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
url3 = "https://public.tableau.com/views/AnalysisofSingaporesHDBResalePrices1990-2023/1_TimeSeries?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

st.subheader("", divider="orange")
st.markdown("## Time Series Dashboard")
st.markdown("##### Economic indicators such as population growth, employment rate are plotted with resale price against year. Interest Rate is the Singapore Overnight Rate Average for loans published by the MAS. Due to the lack of data, there are some gaps in the line graphs.")
st.markdown("""
    *Use the filter below to adjust the years and see how resale trends change with each factor (interest rate, employment rate, population). For each graph, hover over the lines to view additional information*
    """)

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