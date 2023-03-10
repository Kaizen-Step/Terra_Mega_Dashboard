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
st.set_page_config(page_title='Supply - Terra Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('💰Supply')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'weekly_staking_Volume':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/0d88eabc-5b31-4c79-af0e-aa54bda80fd4/data/latest')
    elif query == 'weekly_staking_actions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/28dffd18-f243-45f2-8d33-7feb11b5fa46/data/latest')
    elif query == 'weekly_staking_Reward':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/433a3016-4c68-4dd2-ad96-19aa374d4c5b/data/latest')
    elif query == 'Balance_Range':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/19584bc1-1088-4dd9-be3c-c99744e7a09b/data/latest')
    elif query == 'Reward_Recievers':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7cff5cc4-779c-4637-81f4-5716a0f76eee/data/latest')
    elif query == 'Reward_Distributions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b6ee5c0d-ba2e-4b82-9591-ea79480bdb54/data/latest')
    elif query == 'top_10_Validators':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/93c0836d-f007-413b-9087-561059765e50/data/latest')
    elif query == 'top_10_delegator_base_on_reward':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/75286595-05ef-4b6b-b398-8863a586c4e4/data/latest')
    elif query == 'top10delegatort_TX':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ff03c681-5dd4-42e1-a930-f1cb6046de4f/data/latest')
    elif query == 'TopValidators_Volume':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6df6689b-4452-44d8-a221-2cb579cb44c7/data/latest')
    elif query == 'TopValidators_Users':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/bb2c01ba-99af-41cf-8686-5f94a10b984b/data/latest')
    elif query == 'Validators_Base_Users':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/53645133-f532-43c6-8186-a919382803ff/data/latest')
    elif query == 'Stake_volume_per_user_TX':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/39bbd1b5-3ab1-4ca3-862b-16cbef65da8f/data/latest')
    elif query == 'Unstake_volume_per_user_TX':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fb77d712-e7f6-4c6e-a099-a7b90ebfbffc/data/latest')
    return None


weekly_staking_Volume = get_data('weekly_staking_Volume')
weekly_staking_actions = get_data('weekly_staking_actions')
weekly_staking_Reward = get_data('weekly_staking_Reward')
Balance_Range = get_data('Balance_Range')
Reward_Recievers = get_data('Reward_Recievers')
Reward_Distributions = get_data('Reward_Distributions')
top_10_Validators = get_data('top_10_Validators')
top_10_delegator_base_on_reward = get_data('top_10_delegator_base_on_reward')
top10delegatort_TX = get_data('top10delegatort_TX')
TopValidators_Volume = get_data('TopValidators_Volume')
TopValidators_Users = get_data('TopValidators_Users')
Validators_Base_Users = get_data('Validators_Base_Users')
Stake_volume_per_user_TX = get_data('Stake_volume_per_user_TX')
Unstake_volume_per_user_TX = get_data('Unstake_volume_per_user_TX')

st.subheader('Supply Charts')

df = weekly_staking_Volume
df2 = weekly_staking_actions
df3 = weekly_staking_Reward
df4 = Balance_Range
df5 = Reward_Recievers
df6 = Reward_Distributions
df7 = top_10_Validators
df8 = top_10_delegator_base_on_reward
df9 = top10delegatort_TX
df10 = TopValidators_Volume
df11 = TopValidators_Users
df12 = Validators_Base_Users
df13 = Stake_volume_per_user_TX
df14 = Unstake_volume_per_user_TX

# weekly staking actions-Volume
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df["DATE"], y=df['CUM_STAKE_VOLUME'],
                      name='CUM STAKE VOLUME'), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df['CUM_UNSTAKEE_VOLUME'],
                      name='CUM UNSTAKEE VOLUME'), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df['CUM_SATAKING_NET_VOLUME'],
                      name='CUM SATAKING NET VOLUME'), secondary_y=False)
fig.update_layout(
    title_text='Weekly Staking Actions-Volume Cumulative Values'.title())
fig.update_yaxes(title_text='Volume', secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Action Net-volume
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE"], y=df["NET_VOLUME"],
                     name="NET VOLUME".title()), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df['CUM_SATAKING_NET_VOLUME'],
                      name='CUMULATIVE SATAKING NET VOLUME'.title()), secondary_y=True)
fig.update_layout(
    title_text='Weekly Action Net-volume')
fig.update_yaxes(
    title_text='NET VOLUME'.title(), secondary_y=False)
fig.update_yaxes(title_text='CUM SATAKING NET VOLUME'.title(),
                 secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Weekly Staking Actions
fig = px.bar(df2.sort_values(["DATE", "NUMBER"], ascending=[
             True, False]), x="DATE", y="NUMBER", color="ACTION", title='Weekly Staking Actions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='TX Number')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Staking Actions-Volume
fig = px.bar(df2.sort_values(["DATE", "VOLUME"], ascending=[
             True, False]), x="DATE", y="VOLUME", color="ACTION", title='Weekly Staking Actions-Volume')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Volume')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Staking Reward USD-scale
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df3["DATE"], y=df3["STAKING_REWARDS_USD"],
                     name="STAKING REWARDS [USD]".title()), secondary_y=False)
fig.add_trace(go.Line(x=df3["DATE"], y=df3["CUMULATIVE_STAKING_REWARDS"],
                      name="CUMULATIVE STAKING REWARDS".title()), secondary_y=True)
fig.update_layout(
    title_text='Staking Reward [USD]')
fig.update_yaxes(
    title_text='STAKING REWARDS [USD]'.title(), secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE STAKING REWARDS'.title(),
                 secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Balance Range
fig = px.bar(df4, x="BALANCE_RANGE", y="WALLET_NUMBER",
             color="BALANCE_RANGE", title='Balance Range')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Number of Wallet')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Users Distribution Based on Reward Range
fig = px.bar(df5, x="NUMBER", y="REWARD_RANGE",
             color="REWARD_RANGE", title='Users Distribution Based on Reward Range')
fig.update_layout(showlegend=True, xaxis_title='Number of User',
                  yaxis_title=None)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Reward Distributions
fig = px.bar(df6, x="NUMBER", y="REWARD_RANGE",
             color="REWARD_RANGE", title='Reward Range Distribution')
fig.update_layout(showlegend=True, xaxis_title='Number of Transaction',
                  yaxis_title=None)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# top 10 validators
fig = px.pie(df7, values="Net Staked Volume",
             names="Validator", title='top 10 validators [Luna] ')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# top 10 delegator base on reward (USD scale)
fig = px.pie(df8, values="Reward Volume(USD)",
             names="Reciver", title='top 10 delegator base on reward [USD]')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# top 10 delegator based on Transactions
fig = px.bar(df9, x="Reciver", y="STAKES",
             color="Reciver", title='Top 10 delegator based on Transactions'.title())
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title="STAKES")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Top Validators Based on Volume
fig = px.bar(df10.sort_values(["DATE", "Net Staked Volume"], ascending=[
             True, False]), x="DATE", y="Net Staked Volume", color="Validator", title='Weekly Top Validators Based on Volume')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Net Staked Volume")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Top Validators Based on Users
fig = px.bar(df11.sort_values(["DATE", "DELEGATOR"], ascending=[
             True, False]), x="DATE", y="DELEGATOR", color="Validator", title='Weekly Top Validators Based on Users')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="DELEGATOR")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# top 10 validators Based on Users
fig = px.pie(df12, values="DELEGATOR",
             names="Validator", title='top 10 validators Based on Users')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Stake Volume per User
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df13['DATE'], y=df13["Stake Volume per User"],
                     name="Stake Volume per User"), secondary_y=False)
fig.update_layout(
    title_text='Stake Volume per User')
fig.update_yaxes(
    title_text="Stake Volume per User", secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Stake Transactions per User
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df13['DATE'], y=df13["Stake Transactions per User"],
                     name="Stake Transactions per User"), secondary_y=False)
fig.update_layout(
    title_text='Stake Transactions per User')
fig.update_yaxes(
    title_text="Stake Transactions per User", secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Unstake Transactions per User
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df14['DATE'], y=df14["Stake Transactions per User"],
                     name="Unstake Transactions per User"), secondary_y=False)
fig.update_layout(
    title_text='Unstake Transactions per User')
fig.update_yaxes(
    title_text="Unstake Transactions per User", secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Unstake Volume per User
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df14['DATE'], y=df14["Stake Volume per User"],
                     name="Unstake Volume per User"), secondary_y=False)
fig.update_layout(
    title_text=' Unstake Volume per User')
fig.update_yaxes(
    title_text="Unstake Volume per User", secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
