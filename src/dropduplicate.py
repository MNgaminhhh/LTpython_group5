import pandas as pd
import tkinter.messagebox as messagebox

def dropDuplicate(df):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu")
        return None 
    df_dropduplicate=df.drop_duplicates()
    return df_dropduplicate