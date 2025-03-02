import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"


def fetch_stock_data(symbol:str, interval="5min"):
    """Fetch  data from Alpha Vantage API.\n
    symbol - The name of the equity of your choice. For example: symbol=IBM.\n
    intervals - Time interval between two consecutive data points in the time 
    series. The following values are supported: 1min, 5min, 15min, 30min, 60min."""
    
    parameters = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': interval,
        'apikey': API_KEY,
        'datatype':'json'
    }
    
    response = requests.get(BASE_URL,params=parameters)
    data = response.json()
    
    if f"Time Series ({interval})" not in data:
        print(f"Error fetching data: {data}")
        return None
    return data[f"Time Series ({interval})"]
