import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Getting Stock Price

You'll find below the stock closing price and volume of TESLA.
""")

tickerSymbol = 'TSLA'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2011-1-8', end='2021-1-8')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

st.write("""
##### Created by Chris kagabe (credit: freeCodeCamp.org and DataProfessor)
""")
