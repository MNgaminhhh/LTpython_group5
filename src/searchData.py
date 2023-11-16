import pandas as pd
import tkinter.messagebox as messagebox

def search_and_display(df, column, query, tree):
    # Thực hiện tìm kiếm
    result = search_data(df, column, query)

    # Xóa kết quả tìm kiếm cũ
    tree.delete(*tree.get_children())

    # Hiển thị kết quả tìm kiếm mới
    if result is not None:
        for _, row in result.iterrows():
            tree.insert('', 'end', values=tuple(row))

def search_data(df, column, query):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu", "Vui lòng tải dữ liệu trước khi tìm kiếm!")
        return None
    # Kiểm tra xem query có trống hay không
    if not query.strip():
        messagebox.showwarning("Không có truy vấn", "Vui lòng nhập truy vấn trước khi tìm kiếm!")
        return None
    # Tìm kiếm dữ liệu dựa trên giá trị của một cột cụ thể
    result = df[df[column].astype(str).str.contains(query, case=False, na=False)]
    return result if not result.empty else None