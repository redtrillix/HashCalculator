# A Hash Calculator script written in python for a sqlite database output
# Made by redtrillix
# Version: v0.2.0

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
output_dir = "data"
db_path = os.path.join(output_dir, "hashes.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS hashes (file_path TEXT PRIMARY KEY, file_hash TEXT, date TEXT)")
calculated_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
for file_path, file_hash in hashes.items():
    cursor.execute("INSERT OR REPLACE INTO hashes VALUES (?, ?, ?)", (file_path, file_hash, calculated_date))
conn.commit()
conn.close()
