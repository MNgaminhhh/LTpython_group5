from tkinter import *
import pandas as pd
import tkinter.messagebox as messagebox

def load_data(df,root,id_entry, entry_fields):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu", "Vui lòng tải dữ liệu trước khi chỉnh sửa!")
        root.destroy() 
        return None
    # Tìm kiếm dữ liệu dựa trên ID và hiển thị lên các ô nhập liệu
    # Tìm kiếm dữ liệu dựa trên ID và hiển thị lên các ô nhập liệu
    id = id_entry.get()  # Lấy ID từ ô nhập liệu
    if any(df[df.iloc[:,0] == id]):  # Kiểm tra xem có hàng nào có 'Student ID' bằng `id`
        data = df.loc[df.iloc[:,0] == id].iloc[0]  # Tìm kiếm dữ liệu trong DataFrame
        for column in df.columns:
            entry_fields[column].delete(0, END)  # Xóa dữ liệu hiện tại trong ô nhập liệu
            entry_fields[column].insert(0, data[column])  # Điền dữ liệu vào ô nhập liệu
    else:
               messagebox.showinfo("Thông báo", "Không tìm thấy ID!")  # Hiển thị thông báo không tìm thấy ID