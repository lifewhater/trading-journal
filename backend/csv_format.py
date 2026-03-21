# Reformats dates and headers for sql
import pandas as pd


def load_to_db(connection):
    # =========== TRADOVATE ===========
    # refactoring code
    tradovate = pd.read_csv('tradovate.csv')
    # if contains "(" then it is a negative
    is_neg = tradovate["pnl"].str.contains("(", regex=False )

    # Removed the parenthesis and converted into float
    tradovate['pnl'] = (tradovate['pnl']
                 .str.replace('(', '', regex=False )
                 .str.replace('$', '', regex=False )
                 .str.replace(')','',regex=False )
                 .astype(float))

    # applies negative sign
    tradovate.loc[is_neg, "pnl"] *= -1

    # renaming columns to match make sql queries easier
    tradovate = tradovate.rename(columns={'symbol': 'symbol',
                            'boughtTimestamp': 'entry_time',
                            'soldTimestamp': 'exit_time',
                            'buyFillId' : 'id',
                            'qty' : 'size'
                            })

    # buy time reformatting for tradingview charts
    tradovate["entry_time"] = pd.to_datetime(tradovate['entry_time'])
    tradovate['entry_time'] = tradovate['entry_time'].dt.date

    # sold time reformatting
    tradovate["exit_time"] = pd.to_datetime(tradovate['exit_time'])
    tradovate["exit_time"] = tradovate['exit_time'].dt.date

    # =========== TOPSTEPX ===========
    topstep = pd.read_csv('topstep.csv')

    topstep = topstep.rename(columns={
        # NEED TO RENAME HERE TO "symbol", "pnl", "entry_time", "exit_time"
        'Id' : 'id',
        'ContractName' : 'symbol',
        'EnteredAt' : 'entry_time',
        'ExitedAt' : 'exit_time',
        'PnL' : 'pnl',
        'TradeDuration' : 'duration',
        'Size' : 'size'
    })
    topstep["entry_time"] = pd.to_datetime(topstep["entry_time"], utc=True)
    topstep['entry_time'] = topstep['entry_time'].dt.date

    topstep["exit_time"] = pd.to_datetime(topstep["exit_time"], utc=True)
    topstep['exit_time'] = topstep['exit_time'].dt.date

    connection.execute('DELETE FROM journal')
    tradovate[['symbol', 'entry_time', 'pnl', 'size']].to_sql('journal', connection, if_exists='append', index=False)
    topstep[['symbol', 'entry_time', 'pnl', 'size']].to_sql('journal', connection, if_exists='append', index=False)
