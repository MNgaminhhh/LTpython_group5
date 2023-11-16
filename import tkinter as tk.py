import tkinter as tk
from tkinter import ttk

def on_tree_select(event):
    selected_item = tree.selection()
    print("Selected item:", selected_item)

# Tạo cửa sổ
root = tk.Tk()

# Tạo cây dữ liệu (treeview)
tree = ttk.Treeview(root)
tree["columns"] = ("Name", "Age")

# Thêm cột vào cây
tree.column("#0", width=70)
tree.column("Name", width=150)
tree.column("Age", width=50)

# Đặt tên cho cột
tree.heading("#0", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")

# Thêm dữ liệu vào cây
tree.insert("", "end", values=("John Doe", 25))
tree.insert("", "end", values=("Jane Doe", 30))

# Gắn sự kiện cho việc chọn một dòng trong cây
tree.bind('<<TreeviewSelect>>', on_tree_select)

# Hiển thị cửa sổ
tree.pack()
root.mainloop()
