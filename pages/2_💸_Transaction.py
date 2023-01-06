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
    elif query == 'TX_Num_Overtime':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4e1c9246-a508-475f-9048-8abba7eb96d7/data/latest')
    elif query == 'Terra_Transactions_Intervals':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/22fab0e2-89d7-4f75-a2d1-d96c5dc017d1/data/latest')
    return None


transactions_weekly = get_data('Transactions Weekly')
Luna_daily_tx_vol = get_data('Luna Daily Transaction')
TX_Num_Overtime = get_data('TX_Num_Overtime')
Terra_Transactions_Intervals = get_data('Terra_Transactions_Intervals')

st.subheader('Transaction Charts')
df = transactions_weekly
df2 = Luna_daily_tx_vol
df3 = TX_Num_Overtime
df4 = Terra_Transactions_Intervals

tab_Overtime, tab_Averages = st.tabs(['**Over Time**', '**Averages**'])

with tab_Overtime:
    interval = st.radio('**Time Interval**',
                        ['Daily', 'Weekly', 'Monthly'], key='fees_interval', horizontal=True)

    if st.session_state.fees_interval == 'Daily':

        # Total Transaction over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df4["DAY"], y=df4["TOTAL_TRANSACTIONS_OVER_TIME"],
                             name='Total Transaction'), secondary_y=False)
        fig.add_trace(go.Line(x=df4["DAY"], y=df4["CUMULATIVE_TRANSACTIONS_DAILY"],
                              name='CUMULATIVE Transactions'), secondary_y=True)
        fig.update_layout(
            title_text='Total Transactions Daily with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Transaction', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Transaction', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Total Fees over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df4["DAY"], y=df4["TOTAL_FEES_OVER_TIME"],
                             name='Total Fee'), secondary_y=False)
        fig.add_trace(go.Line(x=df4["DAY"], y=df4["CUMULATIVE_FEE_DAILY"],
                              name='CUMULATIVE Fee'), secondary_y=True)
        fig.update_layout(
            title_text='Total Fees Daily with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Fee', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Fee', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Block Time over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df4["DAY"], y=df4["AVG_BLOCK_TIME_DAILY"],
                             name='Average Block Time'), secondary_y=False)
        fig.update_layout(title_text='Block Time daily')
        fig.update_yaxes(title_text='Average Block Time', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

     # TPs over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df4["DAY"], y=df4["TPS_DAILY"],
                             name='TPS'), secondary_y=False)
        fig.update_layout(title_text='TPS Daily ')
        fig.update_yaxes(title_text='TPS', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    elif st.session_state.fees_interval == 'Weekly':

        # Total Transaction over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df4["WEEK"], y=df4["TOTAL_TRANSACTIONS_OVER_TIME"],
                             name='Total Transaction'), secondary_y=False)
        fig.add_trace(go.Line(x=df4["WEEK"], y=df4["CUMULATIVE_BLOCK_WEEKLY"],
                              name='CUMULATIVE Transactions'), secondary_y=True)
        fig.update_layout(
            title_text='Total Transactions Weekly with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Transaction', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Transaction', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Total Fees over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df4["WEEK"], y=df4["TOTAL_FEES_OVER_TIME"],
                             name='Total Fee'), secondary_y=False)
        fig.add_trace(go.Line(x=df4["WEEK"], y=df4["CUMULATIVE_FEE_WEEKLY"],
                              name='CUMULATIVE Fee'), secondary_y=True)
        fig.update_layout(
            title_text='Total Fees Weekly with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Fee', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Fee', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Block Time over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df4["WEEK"], y=df4["AVG_BLOCK_TIME_WEEKLY"],
                             name='Average Block Time'), secondary_y=False)
        fig.update_layout(title_text='AVG BLOCK TIME WEEKLY'.title())
        fig.update_yaxes(title_text='Average Block Time', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # TPs over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df4["WEEK"], y=df4["TPS_WEEKLY"],
                             name='TPS'), secondary_y=False)
        fig.update_layout(title_text='TPS Weekly')
        fig.update_yaxes(title_text='TPS', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    elif st.session_state.fees_interval == 'Monthly':

        # Total Transaction over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df4["MONTH"], y=df4["TOTAL_TRANSACTIONS_OVER_TIME"],
                             name='Total Transaction'), secondary_y=False)
        fig.add_trace(go.Line(x=df4["MONTH"], y=df4["CUMULATIVE_TRANSACTIONS_MONTHLY"],
                              name='CUMULATIVE Transactions'), secondary_y=True)
        fig.update_layout(
            title_text='Total Transactions Monthly with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Transaction', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Transaction', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Total Fees over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df4["MONTH"], y=df4["TOTAL_FEES_OVER_TIME"],
                             name='Total Fee'), secondary_y=False)
        fig.add_trace(go.Line(x=df4["MONTH"], y=df4["CUMULATIVE_BLOCK_MONTHLY"],
                              name='CUMULATIVE Fee'), secondary_y=True)
        fig.update_layout(
            title_text='Total Fees Monthly with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Fee', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Fee', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Block Time over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df4["MONTH"], y=df4["AVG_BLOCK_TIME_MONTHLY"],
                             name='Average Block Time'), secondary_y=False)
        fig.update_layout(title_text='AVG BLOCK TIME Monthly'.title())
        fig.update_yaxes(title_text='Average Block Time', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # TPs over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df4["MONTH"], y=df4["TPS_MONTHLY"],
                             name='TPS'), secondary_y=False)
        fig.update_layout(title_text='TPS Monthly')
        fig.update_yaxes(title_text='TPS', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with tab_Averages:

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

    # Average Transactions Fee per Week
    fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
    fig.add_trace(go.Bar(x=df["WEEK"], y=df["AVG_TRANSACTION_FEE_WEEKLY"],
                         name='Average Transaction Fee'), secondary_y=False)
    fig.update_layout(title_text='Average Transactions Fee per Week')
    fig.update_yaxes(title_text='Average Transaction Fee', secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Luna Daily Transactions
    st.subheader('Luna Daily Transactions')

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
