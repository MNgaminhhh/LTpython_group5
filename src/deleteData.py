from tkinter import *
import pandas as pd
import tkinter.messagebox as messagebox

def delete_data(df,root,entry_field):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu", "Vui lòng tải dữ liệu trước khi xóa!")
        root.destroy() 
        return None
    id =entry_field.get()
    if id.isdigit():
        id=int(id)
    df = df.drop(df[df.iloc[:,0]==id].index,inplace=True)
    messagebox.showinfo("Thông báo", "Xóa dữ liệu thành công!")  # Hiển thị thông báo thành công'
    
    root.destroy() 
    return df