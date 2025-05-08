import yfinance as yf
from db_utils import get_conn
import pandas as pd

def fetch_and_store(symbol="ITC.NS", start="2023-01-01", end="2025-05-10"):
    stock = yf.download(symbol, start=start, end=end)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM stock_prices")

    for _, row in stock.iterrows():
        try:
            # Print out the row and its length for rows with insufficient data
            if len(row) < 6:
                print(f"Row {row.name} has {len(row)} columns: {row}")
            else:
                open_value = float(row.iloc[0])  # 'Open' column is at position 0
                high_value = float(row.iloc[1])  # 'High' column is at position 1
                low_value = float(row.iloc[2])  # 'Low' column is at position 2
                close_value = float(row.iloc[3])  # 'Close' column is at position 3
                volume_value = int(row.iloc[5])  # 'Volume' column is at position 5

                # Insert values into the database
                cur.execute("""
                    INSERT INTO stock_prices (date, open, high, low, close, volume)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (date) DO NOTHING;
                """, (row.name.date(), open_value, high_value, low_value, close_value, volume_value))
        except Exception as e:
            print(f"Skipping row {row.name} due to error: {e}")



    conn.commit()
    cur.close()
    conn.close()

fetch_and_store()
