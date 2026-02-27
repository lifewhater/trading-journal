# Reformats dates and headers for sql
import pandas as pd

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
                        'boughtTimestamp': 'bought_time',
                        'soldTimestamp': 'sold_time',
                        'buyFillId' : 'buy_fill_id',
                        'sellFillId' : 'sell_fill_id'
                        })

# buy time reformatting for tradingview charts
df["bought_time"] = pd.to_datetime(df['bought_time'])
df['bought_time'] = df['bought_time'].dt.date

# sold time reformatting
df["sold_time"] = pd.to_datetime(df['sold_time'])
df["sold_time"] = df['sold_time'].dt.date


