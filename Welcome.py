import streamlit as st

config = {'scrollZoom': True, 'displayModeBar': True, 'displaylogo': False}
st.set_page_config(page_title="UEFA Euro Graphs", page_icon=":soccer:", layout="wide", initial_sidebar_state="expanded", menu_items=None)
st.write("""
#### UEFA Euro Championship Data Analysis

Hey! My name is [Kunal Pathak](https://www.kunal-pathak.com). And welcome to my web app.\n
This app features interactive visualizations that showcase the performance of each country in the UEFA Euro Championship as of June 14, 2024.\n

#### Go Germany!

I'm of cheering for Germany to win the UEFA Euro Championship in 2024! \n
What better way to cheer for our team, than to build graphs to showcase Germany's performance across the tournament history!\n
This app is my way of supporting our team and demonstrating my skills in using Python, Streamlit, and advanced graphing libraries like Plotly.

#### Check out

Start by clicking on the pages in the sidebar to explore the interactive graphs!\n
For more details, visit my [blog post](https://www.kunal-pathak.com/blog/UEFA-Euro-Data-Analysis).\n
Or dig into the code on  [Github](https://github.com/kanad13/UEFA-Euro-Data-Analysis).
				 """)

st.image('./assets/soccer_player.jpeg', caption=None, width=400, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


# https://docs.streamlit.io/develop/api-reference/widgets/st.page_link
# st.page_link("Welcome.py", label="Welcome")
# st.page_link("pages/050-Interactive_Graphs.py", label="Interactive Graphs")
# st.page_link("pages/100-Match_Performance.py", label="Match Performance")
# st.page_link("pages/200-Tournaments_Statistics.py", label="Tournaments Statistics")
# st.page_link("pages/300-Penalty_Cards.py", label="Penalty Cards")
# st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
