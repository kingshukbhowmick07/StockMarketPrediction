import streamlit as st
import json
import requests 
import streamlit as st  
from streamlit_lottie import st_lottie 


st.title("An overview of Our App")
st.header("What is Stock Market?")
st.text('''The stock market refers to the collection of exchanges and markets where stocks and other securities are 
bought and sold. These securities represent ownership in publicly-traded companies, and their values are 
subject to market fluctuations based on supply and demand.The stock market is an important component of the 
global financial system, providing a mechanism for companies to raise capital by issuing stocks and allowing
investors to buy and sell securities, including stocks, bonds, and other financial instruments. The stock 
market also serves as a barometer of the overall health of the economy, with fluctuations in stock prices 
often reflecting changes in economic conditions and investor sentiment.''')
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_coding = load_lottiefile("img1.json")  # replace link to local lottie file
lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_dwivte2j.json")

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

st.header('Importance of Stocl Market')
st.text('''Help the companies to raise capital
Helps create personal wealth
Serves as an indicator of the state of the economy
Helps to increase investment''')



lottie_coding = load_lottiefile("img2.json")  # replace link to local lottie file
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


st.header('How our Webapp Works !!')
st.text('''This is a Streamlit app that allows the user to select a stock ticker and predict its future stock 
prices using the Prophet forecasting model.The app first prompts the user to input a stock ticker through a 
text input field. Then, it displays a slider that allows the user to select the number of years they want
to predict.After the user inputs the stock ticker and selects the number of years to predict, the app downloads
the historical stock data from Yahoo Finance using the yfinance package. The data is then preprocessed and used
to fit a Prophet model, which is a time-series forecasting model.The app then displays the raw historical stock 
data in a line chart using the Plotly library. The user can zoom in and out of the chart to explore the data.
Next, the app displays the predicted stock prices for the selected stock and time period in a line chart using
the Prophet model. The user can again zoom in and out of the chart to explore the predicted data.
Finally, the app displays the components of the Prophet model's forecast, including the trend, 
seasonality, and holidays. This allows the user to see how each component contributes to the forecasted
stock prices.
''')





 
