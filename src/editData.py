from tkinter import *
import pandas as pd
import tkinter.messagebox as messagebox

def edit_data(df,root,id_entry,entry_fields):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu", "Vui lòng tải dữ liệu trước khi chỉnh sửa!")
        root.destroy() 
        return None

# Chỉnh sửa dữ liệu trong DataFrame dựa trên ID
    id = id_entry.get() 
    if id.isdigit():
        id=int(id) # Lấy ID từ ô nhập liệu
    data = {}  # Tạo một dictionary để lưu dữ liệu
    for column in df.columns:
        data[column] = entry_fields[column].get()  # Lấy dữ liệu từ các ô nhập liệu
    if any(df.iloc[:,0] == id):  # Kiểm tra xem có hàng nào có 'Student ID' bằng `id`
        df.loc[df.iloc[:,0] == id] = list(data.values())  # Cập nhật dữ liệu trong DataFrame
        messagebox.showinfo("Thông báo", "Chỉnh sửa dữ liệu thành công!")  # Hiển thị thông báo thành công
    else:
        messagebox.showinfo("Thông báo", "Không tìm thấy ID!")  # Hiển thị thông báo không tìm thấy ID
    root.destroy()  # Đóng cửa sổ GUI
    return df