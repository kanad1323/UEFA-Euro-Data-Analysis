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
The following graphs showcase the performance of national teams in the UEFA Euro Championship as of June 14, 2024.\n
Click on the tabs below to uncover interesting insights.
""")

# Each tab of my streamlit page contains different charts.
tab1, tab2 = st.tabs(["Goals & Points", "Won & Lost"])

# Tab 1: Goals and Points
with tab1:
    st.write("""
    - `Total Points`: The cumulative points earned by each team, with 3 points awarded for a win, 1 point for a draw, and 0 points for a loss.
    - `Goals Scored`: The total number of goals scored by each team during the tournament.
    - `Goals Conceded`: The total number of goals conceded by each team during the tournament.

    **Click on the "How To Use" button in the sidebar to know how to use the graphs below.**
    """)

    # Dropdown menu for selecting the number of top teams to display
    option = st.selectbox(
        '**Select number of top teams to display:**',
        ('Top 5 teams', 'Top 10 teams', 'All Teams')
    )

    # Filter and sort the data separately for each metric before plotting, so that each sub-plot reflects top values for that metric.
    # https://plotly.com/python/subplots/
    # I want to round them off later, but i dont have time today. https://plotly.com/python/bar-charts/#rounded-bars
    if option == 'Top 5 teams':
        df_points = df.nlargest(5, 'Total points')
        df_goals_scored = df.nlargest(5, 'Goals scored')
        df_goals_conceded = df.nlargest(5, 'Goals conceded')
    elif option == 'Top 10 teams':
        df_points = df.nlargest(10, 'Total points')
        df_goals_scored = df.nlargest(10, 'Goals scored')
        df_goals_conceded = df.nlargest(10, 'Goals conceded')
    else:
        df_points = df.sort_values(by='Total points', ascending=False)
        df_goals_scored = df.sort_values(by='Goals scored', ascending=False)
        df_goals_conceded = df.sort_values(by='Goals conceded', ascending=False)

    # Create subplots
    fig = make_subplots(rows=1, cols=3, subplot_titles=("Total Points", "Goals Scored", "Goals Conceded"))

    # Add bar charts for each metric
    fig.add_trace(
        go.Bar(x=df_points['Team'], y=df_points['Total points'], name='Total Points', marker=dict(color='#fe218b')),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(x=df_goals_scored['Team'], y=df_goals_scored['Goals scored'], name='Goals Scored', marker=dict(color='#fed700')),
        row=1, col=2
    )

    fig.add_trace(
        go.Bar(x=df_goals_conceded['Team'], y=df_goals_conceded['Goals conceded'], name='Goals Conceded', marker=dict(color='#21b0fe')),
        row=1, col=3
    )

    # Update the layout of the subplots
    fig.update_layout(height=600, width=1200, title_text="Goals & Points Subplots", barmode='group')

    # Display the subplots in Streamlit
    st.plotly_chart(fig, config=config)

    # Display the input data table based on the selected top teams
    st.write("""
    ### Input Data

    This table gets updated based on your selection from the drop-down above.\n
    The table can be sorted and scrolled as you like.
    """)

    # https://docs.streamlit.io/develop/concepts/design/dataframes#additional-formatting-options
    st.dataframe(df_points,  hide_index=True)
    st.write("""

    **Note**:\n
    - In this ranking 3 points are awarded for a win, 1 for a draw and 0 for a loss.
    - As per statistical convention in football, matches decided in extra time are counted as wins and losses, while matches decided by penalty shoot-outs are counted as draws.
    """)

# Tab 2: Won & Lost
with tab2:
    st.write("""
    - `Matches Played`: The total number of matches played by each team.
    - `Won`: The total number of matches won by each team.
    - `Drawn`: The total number of matches drawn by each team.
    - `Lost`: The total number of matches lost by each team.
    """)

    # Dropdown menu for selecting the number of top teams to display (by Matches Played)
    option2 = st.selectbox(
        '**Select number of top teams to display (by Matches Played):**',
        ('Top 5 teams', 'Top 10 teams', 'All Teams'),
        key='selectbox2'
    )

    # Filter and sort the data based on the selected number of top teams
    if option2 == 'Top 5 teams':
        df_played = df.nlargest(5, 'Matches Played')
    elif option2 == 'Top 10 teams':
        df_played = df.nlargest(10, 'Matches Played')
    else:
        df_played = df.sort_values(by='Matches Played', ascending=False)

    # Create subplots for the 2x2 grid
    # https://plotly.com/python/subplots/#multiple-subplots
    fig2 = make_subplots(rows=2, cols=2, subplot_titles=("Matches Played", "Matches Won", "Matches Drawn", "Matches Lost"))

    # Add bar charts for each metric
    fig2.add_trace(
        go.Bar(x=df_played['Team'], y=df_played['Matches Played'], name='Matches Played', marker=dict(color='#26547c')),
        row=1, col=1
    )

    # Filter and sort data for the other metrics based on the selected teams
    df_won = df[df['Team'].isin(df_played['Team'])].sort_values(by='Won', ascending=False)
    df_drawn = df[df['Team'].isin(df_played['Team'])].sort_values(by='Drawn', ascending=False)
    df_lost = df[df['Team'].isin(df_played['Team'])].sort_values(by='Lost', ascending=False)

    fig2.add_trace(
        go.Bar(x=df_won['Team'], y=df_won['Won'], name='Matches Won', marker=dict(color='#ef476f')),
        row=1, col=2
    )

    fig2.add_trace(
        go.Bar(x=df_drawn['Team'], y=df_drawn['Drawn'], name='Matches Drawn', marker=dict(color='#ffd166')),
        row=2, col=1
    )

    fig2.add_trace(
        go.Bar(x=df_lost['Team'], y=df_lost['Lost'], name='Matches Lost', marker=dict(color='#06d6a0')),
        row=2, col=2
    )

    # Update the layout of the subplots
    fig2.update_layout(height=600, width=1200, title_text="Match Statistics Subplots", barmode='group')

    # Display the subplots in Streamlit
    st.plotly_chart(fig2, config=config)

    # Display the input data table based on the selected top teams
    st.write("""
    ### Input Data

    This table gets updated based on your selection from the drop-down above.\n
    The table can be sorted and scrolled as you like.
    """)

    # https://docs.streamlit.io/develop/concepts/design/dataframes#additional-formatting-options
    st.dataframe(df_played,  hide_index=True)
