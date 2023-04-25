# A Hash Calculator script written in python for a comma seperated value (csv) file output
# Made by redtrillix
# Version: v0.2.2

import hashlib
import os
import csv
import tkinter as tk
from tkinter import filedialog

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

# Write hashes to a CSV file
csv_path = "hashes.csv"
file_exists = os.path.isfile(csv_path)
with open(csv_path, "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["File Path", "Hash Value"])
    for file_path, file_hash in hashes.items():
        writer.writerow([file_path, file_hash])
