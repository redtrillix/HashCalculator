# A Hash Calculator script written in python for a sqlite database output
# Made by github.com/redtrillix
# Version: v0.2.1

import hashlib
import os
import sqlite3
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

# Select files using file explorer
root = tk.Tk()
root.withdraw()
files = filedialog.askopenfilenames(title="Select files")

# Calculate hash for each file
hashes = {}
for file_path in files:
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    hashes[file_path] = file_hash

# Store hashes in SQLite database
output_dir = "data"  # Directory to save the database file
db_name = "hashes.db"  # Name of the database file
db_path = os.path.join(output_dir, db_name)  # Path to the database file
conn = sqlite3.connect(db_path)  # Connect to the database
cursor = conn.cursor()  # Create a cursor object
cursor.execute("CREATE TABLE IF NOT EXISTS hashes (file_path TEXT PRIMARY KEY, file_hash TEXT, date TEXT)")  # Create a table to store the hashes
calculated_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")  # Get the current date and time in the desired format
for file_path, file_hash in hashes.items():
    cursor.execute("INSERT OR REPLACE INTO hashes VALUES (?, ?, ?)", (file_path, file_hash, calculated_date))  # Insert or replace the hash value and date for each file into the database
conn.commit()  # Save the changes to the database
conn.close()  # Close the database connection
