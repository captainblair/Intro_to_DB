#!/usr/bin/env python3

import mysql.connector  

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''  # 💡 Put your actual MySQL password if set
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create database if not exists (NO SELECT/SHOW used)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:  # Specific error catch
    print(f"Error: {err}")

finally:
    # Clean shutdown of resources
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
