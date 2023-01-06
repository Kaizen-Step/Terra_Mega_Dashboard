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
st.set_page_config(page_title='Overview - Terra Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('📈Overview')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources


@st.cache()
def get_data(query):
    if query == 'Overview_Supply':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/2e9b8bd7-11f8-4856-9e1d-31c34adb5c45/data/latest')
    elif query == 'Overview_Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/eae94398-3e31-4f57-a188-7832b2fc542c/data/latest')
    elif query == 'Overview_Contract_Deployed':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/aecb2cbd-9f9c-4a69-97eb-5a0a13cf04c6/data/latest')
    elif query == 'Overview_Total_Staking_Reward':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/97a71654-c83b-4f34-be2c-6f9f826822fd/data/latest')
    elif query == 'Overview_bridge_out':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/89ff4f7f-817e-4337-bff0-b54e4b83b763/data/latest')
    elif query == 'Overview_new':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ffd5b837-e3bf-4f55-a415-331c67137ac1/data/latest')
    elif query == 'Terra_heatmap2':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/f0f8af7f-08b8-4efe-853c-f0572a8b2290/data/latest')
    elif query == 'Terra_heatmap1':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/be525b82-1dd2-4969-af01-ddd330ac26f9/data/latest')
    return None


Overview_Supply = get_data('Overview_Supply')
Overview_Transactions = get_data('Overview_Transactions')
Overview_Contract_Deployed = get_data('Overview_Contract_Deployed')
Overview_Total_Staking_Reward = get_data('Overview_Total_Staking_Reward')
Overview_bridge_out = get_data('Overview_bridge_out')
Overview_new = get_data('Overview_new')
Terra_heatmap2 = get_data('Terra_heatmap2')
Terra_heatmap1 = get_data('Terra_heatmap1')

# Single Number Overview
st.subheader('Overview')
df1 = Overview_Supply
df2 = Overview_Transactions
df3 = Overview_Contract_Deployed
df4 = Overview_Total_Staking_Reward
df5 = Overview_bridge_out
df6 = Overview_new
df7 = Terra_heatmap2
df8 = Terra_heatmap1

c1, c2, c3 = st.columns(3)
with c1:
    st.metric(label='**Luna Total Supply**',
              value=str(df1['TOTAL_SUPPLY'].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Luna Circulating Supply**',
              value=df1['CIRCULATING_SUPPLY'].map('{:,.0f}'.format).values[0])
    st.metric(label='**Total Contract Deployed**',
              value=df3['Total Contracts Deployed'].map('{:,.0f}'.format).values[0])
    st.metric(label='**Sucsess Rate of Transactions**',
              value=df6["SUCCESS_RATE"].map('{:,.2f}'.format).values[0])
    st.metric(label='**Avg Fee**',
              value=df6["AVG_FEE"].map('{:,.4f}'.format).values[0])
with c2:
    st.metric(label='**Total Transactions**',
              value=str(df6["TOTAL_TRANSACTIONS"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Average Daily Transactions**',
              value=df2["AVERAGE_DAILY_TRANSACTION"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Total Staking Reward**',
              value=df4["CUMULATIVE_STAKING_REWARDS"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Avg Fee per Block**',
              value=df6["AVG_FEE_PER_BLOCK"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Max FEE**',
              value=df6["MAX_FEE"].map('{:,.0f}'.format).values[0])
with c3:
    st.metric(label='**Bridge out-Number of Unique Users**',
              value=str(df5["ACTIVE_USERS"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Bridge out-Total TX of luna**',
              value=df5["NUMBER"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Bridge out-Total volume of luna**',
              value=df5["VOLUME"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Total Blocks**',
              value=df6["TOTAL_BLOCKS"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Total Fees [Luna]**',
              value=df6["TOTAL_FEES"].map('{:,.0f}'.format).values[0])

st.text(" \n")
st.text(" \n")

st.subheader('Heatmaps')

# Block per minute on hour of day (UTC)
fig = px.density_heatmap(df7, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="block per minute on hour of day (UTC)",
                         histfunc='avg', title='Block per minute on hour of day (UTC) Heatmap', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 1}, coloraxis_colorbar=dict(title="block per minute on hour of day (UTC)"))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# User per minute on hour of day (UTC)
fig = px.density_heatmap(df7, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="User per minute on hour of day (UTC)",
                         histfunc='avg', title="User per minute on hour of day (UTC)".title(), nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 1}, coloraxis_colorbar=dict(title="User per minute on hour of day (UTC)"))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# transactions per minute on hour of day (UTC)
fig = px.density_heatmap(df7, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="transactions per minute on hour of day (UTC)",
                         histfunc='avg', title="Transactions per minute on hour of day (UTC)".title(), nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 1}, coloraxis_colorbar=dict(title="transactions per minute on hour of day (UTC)"))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Failedtransactions per minute on hour of day (UTC)
fig = px.density_heatmap(df8, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="Failed transactions per minute on hour of day (UTC)",
                         histfunc='avg', title="Failed transactions per minute on hour of day (UTC)".title(), nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 1}, coloraxis_colorbar=dict(title="Failed transactions per minute on hour of day (UTC)"))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Success transactions per minute on hour of day (UTC)
fig = px.density_heatmap(df8, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="Success transactions per minute on hour of day (UTC)",
                         histfunc='avg', title="Success transactions per minute on hour of day (UTC)".title(), nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 1}, coloraxis_colorbar=dict(title="Success transactions per minute on hour of day (UTC)"))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
