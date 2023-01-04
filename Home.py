# Libraries
import streamlit as st
from PIL import Image


# Layout
st.set_page_config(page_title='Terra MegaDashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('Terra Dashboard')

# Content
c1, c2, c3, c4 = st.columns(4)
c4.image(Image.open('Images/3.png'))
with c1:
    st.write("""# Introduction #""")

st.write("""
 
 Terra is an open-source blockchain payment platform for an algorithmic stablecoin, which are cryptocurrencies that automatically track the price of currencies or other assets. The Terra blockchain enables users to instantly spend, save, trade, or exchange Terra stablecoins.

 The Terra protocol creates stablecoins designed to consistently track the price of a fiat currency (a government-backed currency such as the U.S. dollar or euro). It consists of two cryptocurrency tokens—Terra and Luna.
 ##
 Terra and Luna

 Because the primary value of stablecoins is derived from the stability of the price peg, theoretically bypassing the volatility typical of cryptocurrencies, the Terra protocol attempts to maintain the price of the Terra stablecoin by ensuring that the supply and demand for it are always balanced by employing arbitrage.1

 Luna is the variable counterweight to the Terra stablecoin and absorbs its volatility. To understand how Terra works, envision the entire Terra "economy" to consist of a Terra pool and a Luna pool, which are used to adjust the price via incentives for network participants.

 Terra

 These are stablecoins that track the price of fiat currencies and are named after them. For instance, the base Terra stablecoin tracks the price of the International Monetary Fund's Special Drawing Rights and is named TerraSDR or SDT. Other Terra stablecoin denominations include TerraUSD (UST), which tracks the U.S. dollar, and TerraKRW (KRT) which tracks the South Korean won. Users mint new Terra by burning Luna.71

 Luna

 Used for governance and mining, Luna is the Terra protocol's staking token, which absorbs the price volatility of Terra stablecoins. Users stake Luna to Terra blockchain miners (called "validators"), who record and verify transactions on the blockchain and receive rewards from transaction fees as compensation. As Terra usage grows, Luna's worth increases as well.
 # Collapse of terra #

 At the height of the 2022 bull market, the Terra ecosystem was booming with talent and innovation. The native token of the Terra blockchain had made its way to the top 10 cryptocurrencies by total market capitalization. Protocols were building the next iteration of a super cycle that seemed like it would never end.

 Terraform Labs created Terra amid the crypto market crash of 2018 and built it all through the bear market. The Terra ecosystem's main appeal and claim for glory came from its offer of the best yields in decentralized finance (DeFi), with up to 20% yield on its stablecoin through the Anchor protocol.

 As of March 2022, Terra had a total of 73 projects built in the ecosystem. The ambition of the team was to onboard at least 87 more projects by the end of the year. Terra was becoming a serious competitor to BNB Chain, Solana, Cardano, Avalanche and other layer-1 blockchain infrastructure in their quest to gain market share from the current leader, Ethereum.

 Being a blockchain built on the Cosmos network meant Terra could scale and interoperate with other blockchains through the Interblockchain Communication Protocol (IBC). The hype from the bull market was attracting liquidity and Terra was benefiting from users appetite for new opportunities in the market.

 Terra reached over 90 percent of the total value locked (TVL) of all the Cosmos blockchains with more than $21 billion worth of assets in May 2022.
 That same month of May will be remembered as Terra's collapse. The Terra token was supposed to maintain the peg of Terra's algorithmic stablecoin — until it didn't. Billions of dollars were wiped out from the market in just a couple of days and the flourishing ecosystem Terra had built was left for dead.
 """
         )
