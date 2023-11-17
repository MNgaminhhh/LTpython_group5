import tkinter as tk
from tkinter import filedialog
import pandas as pd

def save_data(df):
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[
        ("CSV files", "*.csv"),
        ("JSON files", "*.json")
    ])

    if file_path:
        try:
            if file_path.endswith(".csv"):
                # Save DataFrame as CSV
                df.to_csv(file_path, index=False, encoding='utf-8-sig')
            elif file_path.endswith(".json"):
                # Save DataFrame as JSON
                df.to_json(file_path, orient='records', lines=True)
            
            tk.messagebox.showinfo("Thông báo", "Lưu file thành công!")
        except Exception as e:
            tk.messagebox.showerror("Lỗi", f"Lỗi khi lưu file: {e}")