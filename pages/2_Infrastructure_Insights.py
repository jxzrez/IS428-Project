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
st.markdown("""##### This is a toggling dashboard between MRT, School or Mall plotted against resale price which can be swapped by clicking on the 3 icons next to the title against resale price.To conduct proper analysis of each factor, we suggest controlling for other variables as they may interact and obscure the effect of MRT distance.""")
st.markdown("""*Use the filters at the top to adjust the range of years, type of flat and town that you are interested in investigating (For storey-range, optimal analysis would be 7 towns at a time for neatness). Hovering over the graphs and trend lines will give additional information.*

*For example:*
- *Fix year to 2013-2015*
- *Only select 3 and 4 room flats*
- *Restrict the storey range to 15 floors*
- *Iterate through each town to see the R-square (explained variation) of the factor in the x-axis against Average resale price.*
            """)

# New Tableau visualization URL
url = "https://public.tableau.com/views/AnalysisofSingaporesHDBResalePrices1990-2023/3_MRT?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

# Embed new Tableau visualization
my_js = f"""
<script type="text/javascript" src="https://public.tableau.com/javascripts/api/tableau-2.min.js"></script>
<div id="vizContainer" style="width:675px; height:1000px"></div>
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
html(my_js, height=800)
st.subheader("", divider="orange")

st.markdown("## Analysis Findings")
st.markdown("##### The following is a visualisation of R-squared for each factor against resale price by iterating through each town with the exact parameters above, and visualising them on a map. Our threshold for a significant enough R-squared is 0.3, and the color legends for all 3 have this value as a centre")

st.markdown("## MRT")
st.markdown("Noteworthy areas where MRT distance has a factor in influencing resale price are Sembawang, Choa Chu Kang, Bukit Panjang, Bukit Timah, Serangoon, Sengkang, Pasir Ris")
st.image("https://github.com/jxzrez/IS428-Project/blob/main/pages/MRT%20Map.png?raw=true")

st.markdown("## Mall")
st.markdown("Mall distance was deemed to not be a factor driving resale price except in Bukit Timah and to a lesser extent Woodlands")
st.image("https://github.com/jxzrez/IS428-Project/blob/main/pages/Mall%20Map.png?raw=true")

st.markdown("## School")
st.markdown("School distance was deemed to have no effect on resale price due to the weak R-squared, except for Marine Parade")
st.image("https://github.com/jxzrez/IS428-Project/blob/main/pages/School%20Map.png?raw=true")