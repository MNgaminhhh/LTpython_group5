import tkinter as tk
from tkinter import filedialog
import pandas as pd

def save_data(df):
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

    if file_path:
        try:
            # Lưu dataframe với encoding là UTF-8
            df.to_csv(file_path, index=False, encoding='utf-8-sig')
            tk.messagebox.showinfo("Thông báo", "Lưu file thành công!")
        except Exception as e:
            tk.messagebox.showerror("Lỗi", f"Lỗi khi lưu file: {e}")
