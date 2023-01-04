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
st.set_page_config(page_title='Transactions - Terra Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('💸Transactions')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Transactions Weekly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/2ece64b2-f7af-46e2-9da7-44c350eb0352/data/latest')
    elif query == 'Luna Daily Transaction':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b08821ca-c8fb-4db0-b95f-4dd0d25df9b9/data/latest')
    return None


transactions_weekly = get_data('Transactions Weekly')
Luna_daily_tx_vol = get_data('Luna Daily Transaction')

st.subheader('Transaction Charts')
df = transactions_weekly
df2 = Luna_daily_tx_vol

# Total Transaction Fees Per Week With Cumulative Value
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['WEEK'], y=df['TOTAL_FEES_WEEKLY'],
                     name='TOTAL_FEES_WEEKLY'), secondary_y=False)
fig.add_trace(go.Line(x=df['WEEK'], y=df['CUMULATIVE_FEE'],
                      name='CUMULATIVE_FEE'), secondary_y=True)
fig.update_layout(
    title_text='Total Transaction Fees Per Week With Cumulative Value')
fig.update_yaxes(
    title_text='TOTAL FEES WEEKLY', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE FEE', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Total Number of Transactions Per Week With Cumulative Value
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['WEEK'], y=df['TOTAL_TRANSACTIONS_WEEKLY'],
                     name='Number of Transactions'), secondary_y=False)
fig.add_trace(go.Line(x=df['WEEK'], y=df['CUMULATIVE_TRANSACTIONS'],
                      name='CUMULATIVE_TRANSACTIONS'), secondary_y=True)
fig.update_layout(
    title_text='Total Number of Transactions Per Week With Cumulative Value')
fig.update_yaxes(
    title_text='Total Number of Transactions', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE TRANSACTIONS', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Average Block Time Per Week chart
fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
fig.add_trace(go.Bar(x=df['WEEK'], y=df['AVG_BLOCK_TIME'],
              name='Average Block Time'), secondary_y=False)
fig.update_layout(title_text='Average Block Time Per Week')
fig.update_yaxes(title_text='Average Block Time', secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Average TPS Per Week Chart
fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
fig.add_trace(go.Bar(x=df['WEEK'], y=df['TPS_WEEKLY'],
              name='TPS'), secondary_y=False)
fig.update_layout(title_text='Average TPS Per Week')
fig.update_yaxes(title_text='TPS Weekly', secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Average Transaction Fee Per Transaction Per Week
fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
fig.add_trace(go.Bar(x=df['WEEK'], y=df['AVG_TRANSACTION_FEE_WEEKLY'],
              name='AVG_TRANSACTION_FEE_WEEKLY'), secondary_y=False)
fig.update_layout(
    title_text='Average Transaction Fee Per Transaction Per Week')
fig.update_yaxes(title_text='AVG TRANSACTION FEE WEEKLY', secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Luna Daily Transactions
st.subheader('Luna Daily Transactions')

# Luna Daily Volume With Standard Moving Averages
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2['DATE'], y=df2['VOLUME'],
                     name='Daily Volume'), secondary_y=False)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA7_VOL'],
                      name='Daily Moving average (MA7))'), secondary_y=True)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA26_VOL'],
                      name='Daily Moving average (MA26)'), secondary_y=True)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA52_VOL'],
                      name='Daily Moving average (MA52))'), secondary_y=True)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA100_VOL'],
                      name='Daily Moving average (MA100)'), secondary_y=True)
fig.update_layout(
    title_text='Luna Daily Volume With Standard Moving Averages')
fig.update_yaxes(
    title_text='Volume', secondary_y=False)
fig.update_yaxes(title_text='Moving averages Volume', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Luna Daily Volume With Cumulative Value
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2['DATE'], y=df2['VOLUME'],
                     name='VOLUME'), secondary_y=False)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['CUMULATIVE_VOLUME'],
                      name='CUMULATIVE VOLUME'), secondary_y=True)
fig.update_layout(
    title_text='Luna Daily Volume With Cumulative Value')
fig.update_yaxes(
    title_text='Daily Volume', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Volume', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Luna Daily Number of Transaction With Standard Moving Averages
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2['DATE'], y=df2['NUMBER_OF_TRANSACTIONS'],
                     name='Daily NUMBER OF TRANSACTIONS'), secondary_y=False)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA7_TX'],
                      name='Daily Moving average (MA7))'), secondary_y=True)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA26_TX'],
                      name='Daily Moving average (MA26)'), secondary_y=True)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA52_TX'],
                      name='Daily Moving average (MA52))'), secondary_y=True)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA100_TX'],
                      name='Daily Moving average (MA100)'), secondary_y=True)
fig.update_layout(
    title_text='Luna Daily Number of Transaction With Standard Moving Averages')
fig.update_yaxes(
    title_text='Daily NUMBER OF TRANSACTIONS', secondary_y=False)
fig.update_yaxes(title_text='Moving averages TX Number', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily Number of Transaction with Cumulative Value
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2['DATE'], y=df2['NUMBER_OF_TRANSACTIONS'],
                     name='Transaction Number'), secondary_y=False)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['CUMULATIVE_TRANSACTIONS'],
                      name='CUMULATIVE TRANSACTIONS'), secondary_y=True)
fig.update_layout(
    title_text='Luna Daily Volume With Cumulative Value')
fig.update_yaxes(
    title_text='Daily Volume', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE TRANSACTIONS', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
