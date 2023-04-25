# A Hash Calculator script written in python for a plain text file output
# Made by redtrillix
# Version: v0.3.0

import hashlib
import os
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

# Write hashes to a text file
txt_path = "hashes.txt"
header_written = os.path.isfile(txt_path) and os.path.getsize(txt_path) > 0
with open(txt_path, "a") as f:
    if not header_written:
        f.write("File Path\tHash Value\n")
    for file_path, file_hash in hashes.items():
        f.write(f"{file_path}\t{file_hash}\n")
