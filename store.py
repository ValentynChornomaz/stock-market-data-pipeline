import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd

load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

def create_table():
    """Create a stock data table if it doesn't exist."""
    querry = """
    CREATE TABLE IF NOT EXISTS stock_prices (
    timestamp TIMESTAMP PRIMARY KEY,
    symbol TEXT NOT NULL,
    open NUMERIC(10,4),
    high NUMERIC(10,4),
    low NUMERIC(10,4),
    close NUMERIC(10,4),
    volume BIGINT
    );
    """
    connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    cursor = connection.cursor()
    cursor.execute(query=querry)
    connection.commit()
    cursor.close()

def save_to_database(df, symbol):
    """Save stock data to Postgres database"""
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()

    for index, row in df.iterrows():
        querry= """
        INSERT INTO stock_prices (timestamp, symbol, open, high, low, close, volume)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (timestamp) DO NOTHING;
        """
        values = (
            index, 
            symbol, 
            float(row["open"]), 
            float(row["high"]), 
            float(row["low"]), 
            float(row["close"]), 
            int(row["volume"])
            )
        # print(values)
        cur.execute(querry, values)

    conn.commit()
    cur.close()
    conn.close()
    print(f"Data for {symbol} saved to DataBase")

if __name__ == "__main__":
    create_table()