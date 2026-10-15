import sqlite3
import pandas as pd

def transform_crypto_data():
    # 1. Connect to the database
    conn = sqlite3.connect("crypto.db")
    
    # 2. Load data into a pandas DataFrame for transformation
    query = "SELECT coin_name, price_usd, timestamp FROM crypto_prices;"
    df = pd.read_sql(query, conn)
    
    print("--- Raw Data Loaded into DataFrame ---")
    print(df)
    
    # 3. Perform aggregations (e.g., average price per coin)
    print("\n--- Transformed Summary: Average Price per Coin ---")
    summary_df = df.groupby("coin_name")["price_usd"].mean().reset_index()
    summary_df.rename(columns={"price_usd": "avg_price_usd"}, inplace=True)
    print(summary_df)
    
    # 4. Close connection
    conn.close()

if __name__ == "__main__":
    transform_crypto_data()