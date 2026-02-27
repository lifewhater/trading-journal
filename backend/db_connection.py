import sqlite3
import csv_format as format

connection = sqlite3.connect("trades.db")
format.df.to_sql("journal", connection, if_exists='append',index=False)

connection.close()