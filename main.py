import os
from dotenv import load_dotenv
import pandas as pd
from fetch import fetch_stock_data
from process import process_stock_data
from store import save_to_database

load_dotenv()
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")

def run_pipeline(symbol):
    """Fetch, process and store stock data"""
    raw_data = fetch_stock_data(symbol)

    if raw_data:
        df = process_stock_data(raw_data)
        save_to_database(df, symbol)
    else:
        print(f"Failed to fetch dta for {symbol}")

if __name__ == "__main__":
    stock_symbol = "IBM"
    run_pipeline(stock_symbol)