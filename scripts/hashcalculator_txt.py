# A Hash Calculator script written in python for a plain text file output
# Made by github.com/redtrillix
# Version: v0.4.1

import hashlib
import os
import tkinter as tk
from tkinter import filedialog

# Select files using file explorer
root = tk.Tk()
root.withdraw()
files = filedialog.askopenfilenames(title="Select files")

# Calculate hash for each file
if files:
    hashes = {}
    for file_path in files:
        with open(file_path, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        hashes[file_path] = file_hash

    # Store hashes in text file
    output_dir = "data"
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, "hashes.txt")
    with open(output_file_path, "a") as f:
        for file_path, file_hash in hashes.items():
            f.write(f"{file_path}\t{file_hash}\n")
