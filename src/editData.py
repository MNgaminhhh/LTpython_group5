from tkinter import *
import pandas as pd
import tkinter.messagebox as messagebox

def edit_data(df, entry_fields, tree):
     # Lấy giá trị từ entry_fields
    new_data = {}
    for column, entry in entry_fields.items():
        new_data[column] = entry.get()
    print(tree)
    # Kiểm tra xem có dòng nào được chọn trong cây không
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Lỗi", "Vui lòng chọn một dòng để chỉnh sửa.")
        return

    selected_item = selected_item[0]
    selected_data = tree.item(selected_item)['values']

    # Lấy chỉ mục của dòng được chọn trong DataFrame
    try:
       selected_index = df[df.apply(lambda row: row.equals(pd.Series(selected_data)), axis=1)].index.tolist()

    except IndexError:
        messagebox.showerror("Lỗi", "Không tìm thấy chỉ mục cho dòng được chọn.")
        return

    # Cập nhật dữ liệu trong DataFrame
    for column, value in new_data.items():
        df.at[selected_index.index, column] = value

    # Cập nhật dữ liệu trong cây
    tree.item(selected_item, values=list(new_data.values()))

    messagebox.showinfo("Thông báo", "Dữ liệu đã được chỉnh sửa thành công.")