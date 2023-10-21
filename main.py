# file: main.py
import pandas as pd 
import tkinter as tk
from ttkbootstrap import Style
from tkinter import ttk
from tkinter import Menu
from src.loadFile import load_file
from src.displayDataAndInfo import display_data_and_info
from src.dropduplicate import dropDuplicate
from src.removeNullValue import removeNullValue

def load_and_display():
    global df
    df = load_file()
    display_data_and_info(df, tree, info_text_widget)
def drop_duplicate_and_display():
    global df
    drop_duplicates_df = dropDuplicate(df) 
    if drop_duplicates_df is not None:
        display_data_and_info(drop_duplicates_df, tree, info_text_widget)
def remove_Null():
    global df
    remove_null_df = removeNullValue(df) 
    if remove_null_df is not None:
        display_data_and_info(remove_null_df, tree, info_text_widget)

root = tk.Tk()
root.title("Quản lý dữ liệu học tập")
root.wm_state('zoomed')

#root1=tk.Tk()
#root1.title("Tính toán")
#root1.vm_state('zoomed')

style = Style(theme='darkly')
notebook = ttk.Notebook(root)
notebook.pack(pady=10, padx=10, expand=True, fill='both')

#style1 = Style(theme='darkly')
#notebook = ttk.Notebook(root1)
#notebook.pack(pady=10, padx=10, expand=True, fill='both')

#columns=df.columns
#optionMenu=tk.OptionMenu(root1,"",*columns)
#optionMenu.config("Chọn thuộc tính")
#label=tk.Label(root1)
#button=tk.Button(root1,text="Close")

#optionMenu.pack()
#label.pack()
#button.pack()

#olumn = optionMenu.get()
#label.config(column)



tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Dữ Liệu')
tree_frame = ttk.Frame(tab1)
tree_frame.pack(pady=10, padx=10, expand=True, fill='both')
tree = ttk.Treeview(tree_frame, style="Treeview")
vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
vsb.pack(side='right', fill='y')
tree.configure(yscrollcommand=vsb.set)
hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
hsb.pack(side='bottom', fill='x')
tree.configure(xscrollcommand=hsb.set)
tree.pack(expand=True, fill='both')
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Thông Tin')
info_text_widget = tk.Text(tab2, wrap='word', height=5, bg=style.colors.dark, fg=style.colors.light, insertbackground=style.colors.light, insertwidth=2)
info_text_widget.pack(pady=10, padx=10, expand=True, fill='both')

df = pd.DataFrame(columns=['Column 0', 'Column 1', 'Column 2', 'Column 3'])
display_data_and_info(df, tree, info_text_widget)
menubar = Menu(root)


root.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Load File", command=load_and_display)
file_menu.add_command(label="loại bỏ trùng lặp",command=drop_duplicate_and_display)
file_menu.add_command(label="Xóa các dòng có Null",command=remove_Null)
root.mainloop()
