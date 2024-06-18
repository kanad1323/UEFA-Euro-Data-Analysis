# Acknowledgements
# Plotly (MIT License) - https://github.com/plotly/plotly.py
# Pandas (BSD-3-Clause license) - https://github.com/pandas-dev/pandas
# Wikipedia (Creative Commons Attribution-ShareAlike 3.0 Unported License (CC BY-SA 3.0)) - https://en.wikipedia.org/wiki/UEFA_European_Championship
# Streamlit (Apache-2.0 license) - https://github.com/streamlit/streamlit

import pandas as pd
import plotly.express as px
import streamlit as st

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

# I have put all my source data files in the data folder
file_path = './data/220-red_cards.csv'
data = pd.read_csv(file_path)

# Define a function to create and display pie charts for different rounds and card colors
def create_pie_chart(round_name, card_color):
    # Filter the data for the specified round and card color
    filtered_data = data[(data['Round'] == round_name) & (data['Card Color'] == card_color)]

    if not filtered_data.empty:
        # Count the contributions by country
        country_counts = filtered_data['Representing'].value_counts().reset_index()
        country_counts.columns = ['Country', 'Count']

        # Create a pie chart with rounded percentage labels
        fig = px.pie(country_counts, values='Count', names='Country', title=f'{card_color} Cards in {round_name}')
        fig.update_traces(textinfo='percent+label', texttemplate='%{label}: %{percent:.0%}')

        return fig, country_counts
    else:
        return None, None

# Streamlit works with line breaks in a weird way. I used the tricks from here - https://github.com/streamlit/streamlit/issues/868#issuecomment-930499725
st.title("Penalty Cards")
st.write("""
         On this page I have plotted pie-charts for information about **Penalty Cards**. \n
         What is meant by Penalty Cards?
            - `Red Card` - It is issued for serious offences. It leads to a player's dismissal from the match. This player can not be replaced for the remainder of the game.
           - `Two-Yellow Cards` - First yellow card is a warning issued by the referee to a player as a caution. Two yellow cards to the same player in one match results in a red card, leading to their dismissal from the match.

         Click on the tabs below to see statistics about Red and Two-Yellow cards issued to each country across various stages of the Euro (as of June 14, 2024).
""")

# Each tab of my streamlit page contains different charts.
# Define the rounds to analyze
rounds = ["Group stage", "Round of 16", "Quarter-finals", "Semi-finals", "Final"]

# Define the card colors to analyze
card_colors = ["Red", "Two-Yellow"]

# Create tabs for each round
tabs = st.tabs([f"{round_name}" for round_name in rounds])

# Display pie charts in respective tabs
for round_name, tab in zip(rounds, tabs):
    with tab:
        #st.subheader(f"Analysis for {round_name}")

        # https://plotly.com/python/pie-charts/
        for card_color in card_colors:
            fig, country_counts = create_pie_chart(round_name, card_color)
            if fig:
                st.plotly_chart(fig)
                #st.dataframe(country_counts, hide_index=True)
            else:
                st.markdown(f"<div style='color: red; font-size: 18px; font-weight: bold;'>No {card_color} cards issued in this round.</div>", unsafe_allow_html=True)

        # Filter and display data relevant to the current round
        round_data = data[data['Round'] == round_name].copy()

        # Reorder columns to have 'Round' as the first column and remove comma from 'Tournament'
        round_data['Tournament'] = round_data['Tournament'].astype(str).str.replace(',', '')
        round_data = round_data[['Round'] + [col for col in round_data.columns if col != 'Round']]

        st.write(f"### Data for {round_name}")# https://docs.streamlit.io/develop/concepts/design/dataframes#additional-formatting-options
        st.dataframe(round_data, hide_index=True)
