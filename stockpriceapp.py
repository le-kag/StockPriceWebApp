import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Buying TSLA Stock?

### You'll find below the stock closing price and volume of TESLA.

""")

tickerSymbol = 'TSLA'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2011-1-8', end='2021-1-10')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

tsla = yf.Ticker("tsla")
st.write("""


### The forward P/E ratio. One of the reason why the stock is sky rocketing. (However, I noticed a slight decrease over the past few days...)

""")
tsla.info['forwardPE']

st.write("""
### As we can see below, the P/E ratio is over 1600 currently.
This shows that investors are willing to pay a higher share price today because of growth expectations in the future.
"The high multiple indicates that investors expect higher growth from the company compared to the overall market.
A high P/E does not necessarily mean a stock is overvalued." - *Investopedia*

""")
import yahoo_fin.stock_info as si
tsla_data = si.get_quote_table("TSLA")

tsla_data

#tickers_list = ["tsla", "aapl", "goog"] # example list
#tickers_data= {} # empty dictionary

#for ticker in tickers_list:
#    ticker_object = yf.Ticker(ticker)

    #convert info() output from dictionary to dataframe
#    temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
#    temp.reset_index(inplace=True)
#    temp.columns = ["Attribute", "Recent"]
    
    # add (ticker, dataframe) to main dictionary
#    tickers_data[ticker] = temp

st.write("""
### Some Data about the company. (Expand if needed)

""")

temp = pd.DataFrame.from_dict(tsla.info, orient="index")
temp.reset_index(inplace=True)
temp.columns = ["Attribute", "Recent"]
st.dataframe(temp)

st.write("""
### More historical data.

""")

tsla_historical = tsla.history(period="max", interval="1wk")
st.dataframe(tsla_historical)

st.write("""
### Thank you for reading! - Chris Kagabe

**Disclaimer: This content is for educational purposes only. The Information should not be construed as investment/trading advice and is not meant to be a solicitation or recommendation to buy, sell, or hold any securities mentioned. **

""")
