import csv, sqlite3
import pandas as pd


dt = pd.read_csv('test_data.csv')
# print(dt['pnl'])

# if contains "(" then it is a negative
is_neg = dt["pnl"].str.contains("(", regex=False)

# Removed the parenthesis and converted into float
dt['pnl'] = (dt['pnl']
             .str.replace('(', '', regex=False)
             .str.replace('$', '', regex=False)
             .str.replace(')','',regex=False)
             .astype(float))

#applies negative sign
dt.loc[is_neg, "pnl"] *= -1


dt = dt.rename(columns={'symbol': 'symbol',
                        'boughtTimestamp': 'bought time',
                        'soldTimestamp': 'sold time',
                        })

# print(dt)

connection = sqlite3.connect("trades.db")

dt.to_sql("trades", connection, if_exists='append', index=False)
connection.close()