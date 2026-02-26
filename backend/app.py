import sqlite3
import pandas as pd

"""
TODO: 
- Need to create schema where each contract is unique and no duplicates allowed if same csv uploaded using ID
- Handle uploading through frontend and automating importing csv to sqlite
- FIX DATE AND TIME FORMATTING (yyyy-mm-dd)
- Get the stats: AVG, SUM, EOD profit, 
"""

df = pd.read_csv('test_data.csv')

# if contains "(" then it is a negative
is_neg = df["pnl"].str.contains("(", regex=False)

# Removed the parenthesis and converted into float
df['pnl'] = (df['pnl']
             .str.replace('(', '', regex=False)
             .str.replace('$', '', regex=False)
             .str.replace(')','',regex=False)
             .astype(float))

#applies negative sign
df.loc[is_neg, "pnl"] *= -1
df = df.rename(columns={'symbol': 'symbol',
                        'boughtTimestamp': 'bought time',
                        'soldTimestamp': 'sold time',
                        })

# Time reformatting for tradingview charts
df["bought time"] = pd.to_datetime(df['bought time'])
df['bought time'] = df['bought time'].dt.date

connection = sqlite3.connect("trades.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS journal(
               symbol TEXT,
               buy_fill_id INTEGER,
               qty INTEGER,
               buy_price REAL,
               sell_price REAL,
               pnl REAL,
               bought_time TEXT,
               sold_time TEXT
               duration TEXT)""")

connection.commit()
connection.close()