import pandas as pd
import tkinter.messagebox as messagebox

def shuffle_data(df):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu", "Vui lòng tải dữ liệu trước khi xáo trộn!")
        return None
    shuffled_df = df.sample(frac=1)
    return shuffled_df
