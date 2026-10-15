import sqlite3
import requests

def load_data_to_db():
    # 1. Fetch live data from API
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url, timeout=10)
    data = response.json()
    
    # 2. Connect to SQLite database (creates crypto.db if it doesn't exist)
    conn = sqlite3.connect("crypto.db")
    cursor = conn.cursor()
    
    # 3. Create a structured table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            coin_name TEXT,
            price_usd REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # 4. Insert extracted records
    for coin, details in data.items():
        cursor.execute("""
            INSERT INTO crypto_prices (coin_name, price_usd)
            VALUES (?, ?)
        """, (coin, details["usd"]))
    
    # 5. Commit changes and close connection
    conn.commit()
    conn.close()
    print("Data successfully loaded into SQLite database!")

if __name__ == "__main__":
    load_data_to_db()