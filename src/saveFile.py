# saveFile.py
import tkinter as tk
from tkinter import filedialog
import pandas as pd

def save_data(df):
    file_path = filedialog.asksaveasfilename(defaultextension=".csv")
    if file_path:
        df.to_csv(file_path, index=False)
