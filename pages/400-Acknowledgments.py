import streamlit as st

config = {'scrollZoom': True, 'displayModeBar': True, 'displaylogo': False}
st.set_page_config(page_title="UEFA Euro Graphs", page_icon=":soccer:", layout="wide", initial_sidebar_state="expanded", menu_items=None)
st.write("""
#### Acknowledgments

All code in this repository is made possible by the contributions of these initiatives. \n
I fully acknowledge their efforts and attribute the usage of their components & data to them:

- **[Pandas](https://github.com/pandas-dev/pandas)** - Licensed under the BSD-3-Clause License
- **[Streamlit](https://github.com/streamlit/streamlit)** - Licensed under the Apache-2.0 License
- **[Plotly](https://github.com/plotly/plotly.py)** - Licensed under the MIT License
- **[Wikipedia](https://en.wikipedia.org/wiki/UEFA_European_Championship)** - Data licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License (CC BY-SA 3.0)

#### Full Code

My own code that powers this website is also MIT Licenced. [Check it out here](https://github.com/kanad13/UEFA-Euro-Data-Analysis)! \n
If you see any inaccuracies with the data or the code, then please drop me a message on [LinkedIn](https://www.linkedin.com/in/kunal-pathak-profile/).
				 """)
