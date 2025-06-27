#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error

try:
    # CONNECT TO MYSQL SERVER 
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='' 
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # CREATE DATABASE IF NOT EXISTS
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as err:
    print(f"Error: {err}")

finally:
    # CLOSE CURSOR AND CONNECTION
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
