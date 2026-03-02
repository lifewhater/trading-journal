# Reformats dates and headers for sql
import pandas as pd

# =========== TRADOVATE ===========
# refactoring code 
tradovate = pd.read_csv('test_data.csv')
# if contains "(" then it is a negative
is_neg = tradovate["pnl"].str.contains("(", regex=False )

# Removed the parenthesis and converted into float
tradovate['pnl'] = (tradovate['pnl']
             .str.replace('(', '', regex=False )
             .str.replace('$', '', regex=False )
             .str.replace(')','',regex=False )
             .astype(float))

#applies negative sign
tradovate.loc[is_neg, "pnl"] *= -1

# renaming columns to match make sql queries easier
tradovate = tradovate.rename(columns={'symbol': 'symbol',
                        'boughtTimestamp': 'entry_time',
                        'soldTimestamp': 'exit_time',
                        'buyFillId' : 'buy_fill_id',
                        'sellFillId' : 'sell_fill_id'
                        })

# buy time reformatting for tradingview charts
tradovate["bought_time"] = pd.to_datetime(tradovate['bought_time'])
tradovate['bought_time'] = tradovate['bought_time'].dt.date

# sold time reformatting
tradovate["sold_time"] = pd.to_datetime(tradovate['sold_time'])
tradovate["sold_time"] = tradovate['sold_time'].dt.date

# =========== TOPSTEPX ===========
topstep = pd.read_csv('topstep.csv')

topstep = topstep.rename(columns={
    # NEED TO RENAME HERE TO "pnl", "entry_time", "exit_time"
})