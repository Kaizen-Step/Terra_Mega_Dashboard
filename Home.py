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
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")

    st.write("""# 🌔Terra (blockchain) #""")

st.write("""
Terra is a blockchain protocol and payment platform used for algorithmic stablecoins. The project was created in 2018 by Terraform Labs, a startup co-founded by Do Kwon and Daniel Shin. It is most known for its Terra stablecoin and the associated Luna reserve asset cryptocurrency.  
In May 2022, the Terra blockchain was temporarily halted after the collapse of the stablecoin TerraUSD (UST) and Luna, in an event that wiped out almost USD45 billion in capitalization within a week. 
### Design ###
Terra is a blockchain that leverages fiat-pegged stablecoins to power a payment system. For consensus the Terra blockchain uses a proof-of-stake codesign. Several stablecoins are built atop the Terra protocol, including TerraUSD, which was the third-largest stablecoin by capitalization before its collapse in May 2022. The Terra blockchain has a fully functional ecosystem of Dapps such as Anchor, Mirror, and Pylon which has utilized the stable-coin infrastructure of Terra. 
Terra is a group of algorithmic stablecoins, named according to the currencies to which they are pegged—for example, TerraUSD (UST) is pegged to the U.S. dollar.  
Luna serves as the primary backing asset for Terra, and is also used as a governance token for users to vote on Terra community proposals.  
UST stablecoins were not backed by U.S. dollars; instead, it was designed to maintain its peg through a complex model called a "burn and mint equilibrium". This method uses a two-token system, whereby one token is supposed to remain stable (UST) while the other token (LUNA) is meant to absorb volatility. 
### History ###
In 2018, Do Kwon and Daniel Shin (also known as Shin Hyun-sung) co-founded Terraform Labs in Seoul, South Korea. In 2019, Terraform Labs launched its first cryptocurrency token. Terraform Labs raised more than USD200 million from investment firms such as Arrington Capital, Coinbase Ventures, Galaxy Digital and Lightspeed Venture Partners.  
In January 2022, the Luna Foundation Guard (LFG) was established as a non-profit based in Singapore, with Do Kwon serving as its director. Terraform Labs allocated a portion of the money obtained from UST sales to Luna Foundation Guard, to be used as reserves to stabilize the price of UST. As of 7 May, just before UST broke its peg, LFG held reserves of 80,394 bitcoin worth approximately USD2.4 billion. Bitcoin was the largest portion of the reserve assets, though LFG also held reserves in various other stablecoins and cryptocurrencies. 
In February 2022, Terra and the Washington Nationals Major League Baseball team announced they had entered into a sponsorship agreement which provided stadium and television branding, as well as the rebranding of the Washington Nationals club and lounge to the "Terra Club".  
The deal was originally proposed to the Terra community by Kwon, referring only to an unnamed "sports franchise in one of the four major American professional sports leagues", and the community agreed to pay USD38.15 million for a five-year-long exclusive partnership. 
### Collapse ###
Beginning on 9 May 2022, the tokens made headlines after UST began to break its peg to the US dollar. Over the next week, the price of UST plunged to 10 cents, while Luna fell to "virtually zero", down from an all-time high of USD119.51. Before the crash, Luna was one of the top ten largest cryptocurrencies on the market. The collapse wiped out almost USD45 billion of market capitalization over the course of a week. 
On 13 May, Terraform Labs temporarily halted the Terra blockchain in response to the falling prices of UST and Luna.  
Despite the company's attempts to stabilize UST and Luna via its bitcoin and other cryptocurrency reserves from the Luna Foundation Guard, the 1:1 peg of UST to USD did not materialize. As of 16 May 2022, blockchain analysts claim that the usage of the bitcoin reserves of LFG still remains largely uncertain. 
On 25 May, a proposal was approved to reissue a new Luna cryptocurrency and to decouple from and abandon the devalued UST stablecoin. The original blockchain is now called Terra Classic (LUNC), and the original Luna token is called Luna Classic. The new Luna coin is called "Terra 2.0" by investors, and has lost valuation in the opening days of being listed on exchanges. 

 





 
 """
         )


st.write("""   
##### Sources #####   """)
st.write("""    1.https: // www.scoutinsights.co. in /post/luna-and -lunc-coins-destroyed  
        2.https: // www.bloomberg.com/news/articles/2022-05-14  
        3.https: // social.techcrunch.com/2022/05/12/  
              """)
c1, c2 = st.columns(2)
with c2:
    st.info(
        '**Project Supervisor:  [MetricsDao](https://metricsdao.notion.site/)**', icon="👨🏻‍💼")
with c1:
    st.info(
        '**Data:  [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="🧠")
