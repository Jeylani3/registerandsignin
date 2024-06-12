# File: config.py

import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': 'localhost',
    'user': 'admin',
    'password': 'mansojey56',
    'database': 'items',  # Update with your database name
}

def get_db_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print("Error while connecting to MySQL:", e)
        return None