from tkinter import *
import pandas as pd
import tkinter.messagebox as messagebox

def add_data(df,root,entry_fields):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu", "Vui lòng tải dữ liệu trước khi thêm dữ liệu!")
        root.destroy() 
        return None
    data = {}  # Tạo một dictionary để lưu dữ liệu
    for column in df.columns:
        data[column] = entry_fields[column].get()  # Lấy dữ liệu từ các ô nhập liệu
    df.loc[len(df)] = data  # Thêm dữ liệu vào DataFrame
    messagebox.showinfo("Thông báo", "Thêm dữ liệu thành công!")  # Hiển thị thông báo thành công
    
    root.destroy() 