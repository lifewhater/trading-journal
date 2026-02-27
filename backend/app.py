# Handles flask api endpoints
import flask, csv_format as format, db_connection as connection

"""
TODO: 
- Need to create schema where each contract is unique and no duplicates allowed
 if same csv uploaded using ID
- Handle uploading through frontend and automating importing csv to sqlite
- FIX DATE AND TIME FORMATTING (yyyy-mm-dd)
- Get the stats: AVG, SUM, EOD profit, 
"""
