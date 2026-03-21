import sqlite3

def connection_to_flask():
    connection = sqlite3.connect("trades.db", check_same_thread=False)
    journal_query = """
    CREATE TABLE IF NOT EXISTS journal (
    symbol TEXT,
    entry_time TEXT,
    pnl REAL,
    size INTEGER,
    duration TEXT
    )
    """
    connection.execute(journal_query)
    return(connection)
