import pandas as pd

def process_stock_data(raw_data):
    """Convert raw JSON data to a cleaned Pandas DataFrame."""
    df = pd.DataFrame.from_dict(raw_data, orient="index")
    df = df.rename(columns={
        "1. open":"open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "5. volume": "volume"
    })
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)
    df = df.sort_index()
    return df
