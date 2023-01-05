# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Aknowledgement - Terra Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('🙏Aknowledgement')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Aknowledgement
st.write("""
We are grateful to all who help us develop this project specially ****Mr. Ali Taslimi**** (twitter: @AliTslm ) with comprehensive streamlit open source project that provide streamlit functions and tools.
And also ****Flipside Crypto**** with massive database and at last ****MetricsDao**** that is reason behind this project.
""")
