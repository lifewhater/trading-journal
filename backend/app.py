# Handles flask api endpoints
from flask import Flask, jsonify
from flask_cors import CORS  # type: ignore
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
CORS(app)

connection = connection_to_flask()
format.load_to_db(connection)

@app.route('/')
def stats():
    cursor = connection.cursor()
    # Cumlative PNL
    total = cursor.execute('SELECT SUM(pnl) FROM journal').fetchone()[0]

    # Will add per day pnl view
    
    # Groups by per date and in ascending order
    daily_pnl = [dict(row) for row in cursor.execute('SELECT entry_time as date, symbol, SUM(pnl) as pnl, SUM(size) as size FROM journal GROUP BY date ORDER BY date ASC').fetchall()]

    cursor.close()

    return jsonify({
        'pnl' : total,
        'daily_pnl' : daily_pnl,
    })
