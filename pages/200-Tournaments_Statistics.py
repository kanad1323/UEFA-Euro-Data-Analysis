# Acknowledgements
# Plotly (MIT License) - https://github.com/plotly/plotly.py
# Pandas (BSD-3-Clause license) - https://github.com/pandas-dev/pandas
# Wikipedia (Creative Commons Attribution-ShareAlike 3.0 Unported License (CC BY-SA 3.0)) - https://en.wikipedia.org/wiki/UEFA_European_Championship
# Streamlit (Apache-2.0 license) - https://github.com/streamlit/streamlit

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import plotly.express as px

# Config for Plotly graphs
# This dictionary configures the interactivity options for the Plotly graphs displayed in my Streamlit app.
# 'scrollZoom' enables zooming using the mouse scroll wheel, 'displayModeBar' shows the mode bar with options,
# and 'displaylogo' hides the Plotly logo from the mode bar.
# I added the config options I needed. You can find more options at:
# https://github.com/plotly/plotly.js/blob/master/src/plot_api/plot_config.js
config = {'scrollZoom': False, 'displayModeBar': True, 'displaylogo': False}

# Streamlit page configuration
# This function sets the basic configuration for the Streamlit app.
# 'page_title' sets the title of the web page,
# 'page_icon' sets an icon for the web page (soccer ball emoji in this case),
# 'layout' defines the layout of the app (wide layout to use the full screen width),
# 'initial_sidebar_state' sets the initial state of the sidebar (expanded by default),
# and 'menu_items' can be used to customize the menu items (none in this case).
# I added the config options I needed. You can find more options at:
# https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config
st.set_page_config(page_title="UEFA Euro Graphs", page_icon=":soccer:", layout="wide", initial_sidebar_state="expanded", menu_items=None)

# Load data from CSV file
# I have put all my source data files in the data folder
file_path = './data/100-overall_team_records.csv'
df = pd.read_csv(file_path)

# Streamlit works with line breaks in a weird way. I used the tricks from here - https://github.com/streamlit/streamlit/issues/868#issuecomment-930499725
st.write("""# Match performance
The following graphs showcase the Tournaments related statistics in the UEFA Euro Championship as of June 14, 2024.\n
Click on the tabs below to uncover interesting insights.
""")

# Each tab of my streamlit page contains different charts.
tab1, tab2 = st.tabs(["Host Nations", "Medals Tally"])

# Tab 1: Host Nations
with tab1:
    st.write("""
    - `Number of times hosted`: The number of times each nation has hosted the UEFA Euro Championship.

    **Click on the "How To Use" button in the sidebar to know how to use the graphs below.**
    """)

    # Dropdown menu for selecting the number of top host nations to display
    option4 = st.selectbox(
        '**Select number of top host nations to display:**',
        ('Top 5 nations', 'Top 10 nations', 'All Nations'),
        key='selectbox4'
    )

    # Load the data for host nations from CSV file
    file_path = './data/210-host_countries.csv'
    host_nations_df = pd.read_csv(file_path)

    # Prepare the data
    pie_data = host_nations_df[['Nation', 'Number of times hosted', 'Year(s)']]
    pie_data = pie_data.groupby('Nation').sum().reset_index()

    # Filter and sort the data based on the selected number of top host nations
    if option4 == 'Top 5 nations':
        pie_data = pie_data.nlargest(5, 'Number of times hosted')
    elif option4 == 'Top 10 nations':
        pie_data = pie_data.nlargest(10, 'Number of times hosted')
    else:
        pie_data = pie_data.sort_values(by='Number of times hosted', ascending=False)

    # Round the number of times hosted to the nearest integer
    pie_data['Number of times hosted'] = pie_data['Number of times hosted'].round().astype(int)

    # Create the pie chart
    fig4 = px.pie(pie_data, values='Number of times hosted', names='Nation', title='Number of Times Nations Hosted Events')

    # Display the pie chart in Streamlit
    st.plotly_chart(fig4, config=config)

    # Display the input data table based on the selected top host nations
    st.write("""
    ### Input Data

    This table gets updated based on your selection from the drop-down above.\n
    The table can be sorted and scrolled as you like.
    """)

    # https://docs.streamlit.io/develop/concepts/design/dataframes#additional-formatting-options
    st.dataframe(pie_data,  hide_index=True)

# Tab 2: Medals
with tab2:
    st.write("""
    - `Gold`: The number of gold medals won by each team.
    - `Silver`: The number of silver medals won by each team.
    - `Bronze`: The number of bronze medals won by each team.

    **Note**: The Third place playoff was removed in 1984. Since then, losing semi-finalists are both counted under bronze.

    **Click on the "How To Use" button in the sidebar to know how to use the graphs below.**
    """)

    # Dropdown menu for selecting the number of top teams to display (by Total Medals)
    option3 = st.selectbox(
        '**Select number of top teams to display (by Total Medals):**',
        ('Top 5 teams', 'Top 10 teams', 'All Teams'),
        key='selectbox3'
    )

    # Load the data for medals tally from CSV file
    file_path = './data/110-team_medals.csv'
    uefa_medals_df = pd.read_csv(file_path)

    # Filter and sort the data based on the selected number of top teams
    if option3 == 'Top 5 teams':
        uefa_medals_df = uefa_medals_df.nlargest(5, 'Total')
    elif option3 == 'Top 10 teams':
        uefa_medals_df = uefa_medals_df.nlargest(10, 'Total')
    else:
        uefa_medals_df = uefa_medals_df.sort_values(by="Total", ascending=False)

    # Define custom colors for each medal type
    custom_colors = {
        "Gold": "#fca311",  # Gold color
        "Silver": "#e5e5e5",  # Silver color
        "Bronze": "#14213d"  # Bronze color
    }

    # Create the bar chart
    # https://plotly.com/python/bar-charts/#bar-charts-with-wide-format-data
    fig3 = px.bar(uefa_medals_df, x="Team", y=["Gold", "Silver", "Bronze"], text_auto=True, title="UEFA Euro Tournament Medals by Country", color_discrete_map=custom_colors)

    # Display the chart in Streamlit
    st.plotly_chart(fig3, config=config)

    # Display the input data table based on the selected top teams
    st.write("""
    ### Input Data

    This table gets updated based on your selection from the drop-down above.\n
    The table can be sorted and scrolled as you like.
    """)

    # https://docs.streamlit.io/develop/concepts/design/dataframes#additional-formatting-options
    st.dataframe(uefa_medals_df,  hide_index=True)
