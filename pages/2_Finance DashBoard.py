import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px

st.title('Stock Finance DashBoard')


tickers = st.sidebar.text_input('Pick Your Stock')
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')

#dropdown= st.multiselect('Pick your assets',tickers)
df=yf.download(tickers,start_date,end_date)['Adj Close']
st.line_chart(df)

