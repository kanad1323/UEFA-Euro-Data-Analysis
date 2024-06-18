import streamlit as st

# https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config
st.set_page_config(page_title="UEFA Euro Graphs", page_icon=":soccer:", layout="wide", initial_sidebar_state="expanded", menu_items=None)

st.write("""
# How to use this website?
All graphs in this site are interactive and built using Python.\n
This page provides some visual aids on how to interact with these graphs.
Note that these are dummy graphs for illustrative purposes.\n
Some videos may look blurry because YouTube calculated your internet speed incorrectly. So just click the Gear Settings icon on the video to render them in high quality.\n
**Move the slider in the side-bar to make the videos bigger in size.**
""")

st.write("""
### Pages & Graphs
""")

# https://discuss.streamlit.io/t/changing-the-display-size-of-st-video/20559/6
DEFAULT_WIDTH = 50
width = st.sidebar.slider(
    label="Move this slider to make the videos bigger in size.", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%"
)

# If this code does not work then I will default to rendering videos the standard way - #https://docs.streamlit.io/develop/api-reference/media/st.video

# Link to my YouTube channel
st.sidebar.markdown("""
[Full playlist of videos on YouTube.](https://www.youtube.com/playlist?list=PLRIoderjwGT-d9oSkMysrYypXS6m6gdTs)
""")

# Ensure minimum width and calculate side margins
width = max(width, 0.01)
side = max((100 - width) / 2, 0.01)

# Function to create a container for the video with adjustable width
def video_container(url):
    _, container, _ = st.columns([side, width, side])
    container.video(url, loop=True, autoplay=True, muted=True)

# Video for Pages & Graphs
video_container("https://youtu.be/XAe64jUHW0c")

st.write("""
### Drop-downs and Tables
""")

# Video for Drop-downs and Tables
video_container("https://youtu.be/7FWUb8-z9FQ")

st.write("""
### Tabs & Zooming
""")

# Video for Tabs & Zooming
video_container("https://youtu.be/1DuUr80vY1c")

st.write("""
### Dynamic graphs
""")

# Video for Dynamic graphs
video_container("https://youtu.be/ixG7ZYcgsWE")
