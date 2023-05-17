import streamlit as st
from stocknews import StockNews
import json
import requests 
import streamlit as st  
from streamlit_lottie import st_lottie 

tickers = st.sidebar.text_input('Pick Your Stock')


st.title('Top 10 News of')
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_coding = load_lottiefile("img2.json")  
lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_i2eyukor.json")

st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", 
    height=None,
    width=None,
    key=None,
)


st.header(f'News of {tickers}')
sn=StockNews(tickers,save_news=False)
df_news=sn.read_rss()
for i in range(10):
	st.subheader(f'News {i+1}')
	st.write(df_news['published'][i])
	st.write(df_news['title'][i])
	st.write(df_news['summary'][i])
	#title_sentiment=df_news['sentiment_title']
	#st.write(f'Title Sentiment {title_sentiment}')
	#news_sentiment = df_news['sentiment_summary'][i]
	#st.write(f'News Sentiment {news_sentiment}')