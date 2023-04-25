# A Hash Calculator script written in python for a comma separated value (csv) file output
# Made by redtrillix
# Version: v0.3.0

import hashlib
import os
import csv
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

# Write hashes to a CSV file
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)
csv_path = os.path.join(output_dir, "hashes.csv")
file_exists = os.path.isfile(csv_path)
with open(csv_path, "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["File Path", "Hash Value", "Date"])
    calculated_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    for file_path, file_hash in hashes.items():
        writer.writerow([file_path, file_hash, calculated_date])
