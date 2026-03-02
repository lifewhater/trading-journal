import sqlite3
import csv_format as format

def connection_to_flask():
    connection = sqlite3.connect("backend/trades.db")
    return(connection)
