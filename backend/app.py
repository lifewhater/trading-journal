# Handles flask api endpoints
from flask import Flask, jsonify
import csv_format as format
from db_connection import connection_to_flask

"""
TODO: 
- Need to create schema where each contract is unique and no duplicates allowed
 if same csv uploaded using ID
- Handle uploading through frontend and automating importing csv to sqlite
- [DONE] FIX DATE AND TIME FORMATTING (yyyy-mm-dd)
- [DONE] Get the stats: AVG, SUM, EOD profit (done through sql call from frontend)
"""

app = Flask(__name__)

connection = connection_to_flask()
format.load_to_db(connection)

@app.route('/')
def stats():
    cursor = connection.cursor()
    # Cumlative PNL
    total = cursor.execute('SELECT SUM(pnl) FROM journal').fetchone()[0]

    # Will add per day pnl view
    
    # Groups by per date and in ascending order
    cursor.execute('SELECT entry_time, symbol, pnl, size FROM journal GROUP BY entry_time ORDER BY entry_time ASC').fetchall()

    cursor.close()
    return jsonify({
        'pnl' : total,
    })