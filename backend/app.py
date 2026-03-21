# Handles flask api endpoints
from flask import Flask, jsonify
import csv_format as format
from db_connection import connection_to_flask

"""
TODO: 
- Need to create schema where each contract is unique and no duplicates allowed
 if same csv uploaded using ID
- Handle uploading through frontend and automating importing csv to sqlite
- FIX DATE AND TIME FORMATTING (yyyy-mm-dd)
- Get the stats: AVG, SUM, EOD profit (done through sql call from frontend)
"""

app = Flask(__name__)

connection = connection_to_flask()
format.load_to_db(connection)

@app.route('/stats')
def stats():
    cursor = connection.cursor()
    total = cursor.execute('SELECT SUM(pnl) FROM journal').fetchone()[0]
    table = cursor.execute('SELECT * FROM journal').fetchall()

    cursor.close()
    return jsonify({
        'pnl' : total,
        'journal' : table 
    })