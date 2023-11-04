import pandas as pd
import tkinter.messagebox as messagebox

def removeNullValue(df):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu", "Vui lòng tải dữ liệu trước khi loại bỏ giá trị Null!")
        return None 
    df_dropna=df.dropna()
    return df_dropna