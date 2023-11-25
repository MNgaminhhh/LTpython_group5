import pandas as pd 
import tkinter as tk
from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk
from tkinter import Menu
from tkinter.ttk import Treeview
import tkinter.messagebox as messagebox
from tkinter import scrolledtext
from src.loadFile import load_file
from src.displayDataAndInfo import display_data_and_info
from src.dropduplicate import dropDuplicate
from src.removeNullValue import removeNullValue

from src.loaddictionary import loadDictionary
from src.replaceNullValue import replaceNullwithmax
from src.replaceNullValue import replaceNullwithmedium
from src.replaceNullValue import replaceNullwithmin
from src.shuffleData import shuffle_data
from src.saveFile import save_data
from src.addData import add_data
from src.deleteData import delete_data
from src.loadData import load_data
from src.editData import edit_data
from src.loadmoreData import concatenate_dataframes
from src.searchData import search_data
from src.searchData import search_and_display
def sortAscending():
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu", "Vui lòng tải dữ liệu trước khi sắp xếp!")
        return
    root = Tk()
    root.title("Sắp xếp")
    root.geometry('')
    label_column = Label(root, text="Chọn cột:")
    label_column.pack(padx=10, pady=10)
    selected_column = StringVar(root)
    selected_column.set(df.columns[0])
    column_menu = OptionMenu(root, selected_column, *df.columns)
    column_menu.config(width=70)
    column_menu.pack(padx=10, pady=10)
    label_order = Label(root, text="Chọn thứ tự:")
    label_order.pack(padx=10, pady=10)
    selected_order = StringVar(root)
    selected_order.set("Tăng dần")
    order_menu = OptionMenu(root, selected_order, "Tăng dần", "Giảm dần")
    order_menu.config(width=70)
    order_menu.pack(padx=10, pady=10)
    def perform_sort_and_update():
        column_to_sort = selected_column.get()
        ascending = True if selected_order.get() == "Tăng dần" else False
        df.sort_values(by=column_to_sort, inplace=True, ascending=ascending)
        root.destroy()
        display_data_and_info(df, tree, info_text_widget)
    sort_button = Button(root, text='Sắp xếp', command=perform_sort_and_update)
    sort_button.pack(pady=10)
    root.mainloop()
def load_more_data_and_display():
    global df2,df
    df2 = load_file()
    df = concatenate_dataframes(df,df2)
    display_data_and_info(df, tree, info_text_widget)
    
def load_and_display():
    global df
    df = load_file()
    display_data_and_info(df, tree, info_text_widget)

def reset_button():
    global df
    display_data_and_info(df, tree, info_text_widget)

def drop_duplicate_and_display():
    global df
    drop_duplicates_df = dropDuplicate(df)
    if drop_duplicates_df is not None:
        df = drop_duplicates_df 
        display_data_and_info(df, tree, info_text_widget)
def remove_Null():
    global df
    remove_null_df = removeNullValue(df)
    if remove_null_df is not None:
        df = remove_null_df
        display_data_and_info(df, tree, info_text_widget)
def find_Min(df, column):
    try:
        if df is None or df.empty:
            messagebox.showwarning("Không có dữ liệu")
            return None
        if column in df.columns:
            min_value = df[column].min()
            return min_value
        else:
            messagebox.showwarning(f"Cột '{column}' không tồn tại trong DataFrame.")
            return None
    except Exception as e:
        print(f"Lỗi khi tìm giá trị nhỏ nhất cho cột {column}: {e}")
        return None

def find_Max(df, column):
    try:
        if df is None or df.empty:
            messagebox.showwarning("Không có dữ liệu")
            return None
        if column in df.columns:
            max_value = df[column].max()
            return max_value
        else:
            messagebox.showwarning(f"Cột '{column}' không tồn tại trong DataFrame.")
            return None
    except Exception as e:
        print(f"Lỗi khi tìm giá trị lớn nhất cho cột {column}: {e}")
        return None

def find_Average(df, column):
    try:
        if df is None or df.empty:
            messagebox.showwarning("Không có dữ liệu")
            return None
        if column in df.columns:
            numeric_column = pd.to_numeric(df[column])
            average_value = numeric_column.mean()
            return average_value
        else:
            messagebox.showwarning(f"Cột '{column}' không tồn tại trong DataFrame.")
            return None
    except Exception as e:
        print(f"Lỗi khi tính giá trị trung bình cho cột {column}: {e}")
        return None
def thay_the_null_bang_min(column):
    global df
    try:
        replace_null_df = replaceNullwithmin(df, column)
        if replace_null_df is not None:
            df = replace_null_df
            display_data_and_info(df, tree, info_text_widget)
    except Exception as e:
        print(f"Error: {e}")

def thay_the_null_bang_max(column):
    global df
    try:
        replace_null_df = replaceNullwithmax(df, column)
        if replace_null_df is not None:
            df = replace_null_df
            display_data_and_info(df, tree, info_text_widget)
    except Exception as e:
        print(f"Error: {e}")

def thay_the_null_bang_medium(column):
    global df
    try:
        replace_null_df = replaceNullwithmedium(df, column)
        if replace_null_df is not None:
            df = replace_null_df
            display_data_and_info(df, tree, info_text_widget)
    except Exception as e:
        print(f"Error: {e}")

def replace_null_option():
    root3 = Tk()
    root3.title("Thay Thế Giá Trị Null")
    root3.geometry('400x200')

    label_option = Label(root3, text='Lựa Chọn')
    label_option.place(x=20, y=20)

    label_column = Label(root3, text="Thuộc Tính")
    label_column.place(x=20, y=80)

    global df
    columns = list(df.columns)
    options = list(["Thay Thế Null bằng Giá Trị Nhỏ Nhất", "Thay Thế Null bằng Giá Trị Lớn Nhất", "Thay Thế Null bằng Giá Trị Trung Bình"])
    
    clicked_option = StringVar(root3)
    clicked_option.set(options[0])

    clicked_column = StringVar(root3)
    clicked_column.set(columns[0])

    def thuc_hien_thay_the():
        if clicked_option.get() == options[0]:
            thay_the_null_bang_min(clicked_column.get())
        elif clicked_option.get() == options[1]:
            thay_the_null_bang_max(clicked_column.get())
        elif clicked_option.get() == options[2]:
            thay_the_null_bang_medium(clicked_column.get())
    
    dropdown_option = OptionMenu(root3, clicked_option, *options)
    dropdown_option.config(width=30)
    dropdown_option.pack(pady=20)

    dropdown_column = OptionMenu(root3, clicked_column, *columns)
    dropdown_column.config(width=30)
    dropdown_column.pack(pady=20)

    button_thay_the = Button(root3, text="Thực Hiện Thay Thế", command=thuc_hien_thay_the)
    button_thay_the.place(x=60, y=120)
    button_thay_the.pack()

    root3.mainloop()
def khung_tinh_toan():
    root1 = Tk()
    root1.title("Tính Toán Cơ Bản")
    root1.geometry('400x400')

    label = Label(root1, text='Thuộc tính')
    label.place(x=20, y=20)

    global df
    column = list(df.columns)

    clicked = StringVar(root1)
    clicked.set(column[0])

    def selected(ev):
        selected_column = clicked.get()
        try:
            min_value = find_Min(df, selected_column)
            mylabel = Label(root1, text=f"Min của {selected_column} là: {min_value}").pack()
            max_value = find_Max(df, selected_column)
            mylabel1 = Label(root1, text=f"Max của {selected_column} là: {max_value}").pack()
            average_value = find_Average(df, selected_column)
            mylabel3 = Label(root1, text=f"Trung bình của {selected_column} là: {average_value}").pack()
            Label(root1, text="--------------------------").pack()
        except Exception as e:
            print(f"Lỗi: {e}")
    drop = OptionMenu(root1, clicked, *column, command=selected)
    drop.config(width=30)
    drop.pack(pady=20)
    root1.mainloop()


def khung_add_data():
    global df
    root = Tk()
    root.title("Thêm dữ liệu")
    root.geometry('')

    entry_fields = {}
    for i, column in enumerate(df.columns):
        Label(root, text=column, font=('Arial', 12)).grid(row=i, padx=20, pady=10)
        entry_fields[column] = Entry(root, font=('Arial', 11))
        entry_fields[column].grid(row=i, column=1, padx=20, pady=10)

    Button(root, text='Thêm', command=lambda: add_data(df,root,entry_fields), font=('Arial', 12), bg='blue', fg='white').grid(row=len(df.columns), column=0, columnspan=2, padx=20, pady=20, sticky="ew")
    
    tree = None
    info_text_widget = None
    display_data_and_info(df, tree, info_text_widget)
    
    root.mainloop()

def Khung_delete_data():
    global df
    root = Tk()
    root.title("Xóa dữ liệu")
    root.geometry('')
    frame = Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")
    columns = list(df.columns)
    selected_column = StringVar(root)
    selected_column.set(columns[0])
    
    label = Label(frame, text="Chọn cột:")
    label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    
    column_menu = OptionMenu(frame, selected_column, *columns)
    column_menu.config(width=50)
    column_menu.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    
    label_search = Label(frame, text="Nhập giá trị tìm kiếm:")
    label_search.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    
    search_entry = Entry(frame)
    search_entry.config(width=50)
    search_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    
    tree = Treeview(frame, columns=columns, show='headings', style="mystyle.Treeview")
    for column in columns:
        tree.heading(column, text=column)
        tree.column(column, width=80)  # Set the width of each column to 100
    tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    
    scrollbar_y = Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar_y.grid(row=2, column=2, pady=10, sticky="ns")
    tree.configure(yscrollcommand=scrollbar_y.set)
    
    scrollbar_x = Scrollbar(frame, orient="horizontal", command=tree.xview)
    scrollbar_x.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    tree.configure(xscrollcommand=scrollbar_x.set)
    
    Button(frame, text='Tìm kiếm', command=lambda: search_and_display(df, selected_column.get(), search_entry.get(), tree)).grid(row=4, column=0, pady=10, sticky="ew", columnspan=2)
    
    def on_tree_select(event):
        selected_item = tree.selection()[0]
        selected_data = tuple(tree.item(selected_item)['values'])
        for i, column in enumerate(df.columns):
            entry_field[column].delete(0, END)
            if not df.empty:
                entry_field[column].insert(0, selected_data[i])

    tree.bind('<<TreeviewSelect>>', on_tree_select)
    
    entry_field = {}

    for i, column in enumerate(df.columns):
        Label(root, text=column).grid(row=i + 1)
        entry_field[column] = Entry(root)
        entry_field[column].grid(row=i + 1, column=1)
    Button(root, text='Xóa', command=lambda: delete_data(df,root,entry_field[columns[0]])).grid(row=len(df.columns)+1, column=0)
    root.mainloop()

def Khung_edit_data():
    global df
    root = Tk()
    root.title("Chỉnh sửa dữ liệu")
    root.geometry('')
    frame = Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")
    columns = list(df.columns)
    selected_column = StringVar(root)
    selected_column.set(columns[0])
    
    label = Label(frame, text="Chọn cột:")
    label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    
    column_menu = OptionMenu(frame, selected_column, *columns)
    column_menu.config(width=50)
    column_menu.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    
    label_search = Label(frame, text="Nhập giá trị tìm kiếm:")
    label_search.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    
    search_entry = Entry(frame)
    search_entry.config(width=50)
    search_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    
    tree = Treeview(frame, columns=columns, show='headings', style="mystyle.Treeview")
    for column in columns:
        tree.heading(column, text=column)
        tree.column(column, width=80)  # Set the width of each column to 100
    tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    
    scrollbar_y = Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar_y.grid(row=2, column=2, pady=10, sticky="ns")
    tree.configure(yscrollcommand=scrollbar_y.set)
    
    scrollbar_x = Scrollbar(frame, orient="horizontal", command=tree.xview)
    scrollbar_x.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    tree.configure(xscrollcommand=scrollbar_x.set)
    
    Button(frame, text='Tìm kiếm', command=lambda: search_and_display(df, selected_column.get(), search_entry.get(), tree) ).grid(row=4, column=0, pady=10, sticky="ew", columnspan=2)
    
    def on_tree_select(event):
        selected_item = tree.selection()[0]
        selected_data = tuple(tree.item(selected_item)['values'])
        for i, column in enumerate(df.columns):
            entry_fields[column].delete(0, END)
            if not df.empty:
                entry_fields[column].insert(0, selected_data[i])

    tree.bind('<<TreeviewSelect>>', on_tree_select)
    
    entry_fields = {}

    for i, column in enumerate(df.columns):
        Label(root, text=column).grid(row=i + 1)
        entry_fields[column] = Entry(root)
        entry_fields[column].grid(row=i + 1, column=1)

    Button(root, text='Sửa', command=lambda: edit_data(df,root,entry_fields[df.columns[0]], entry_fields)).grid(row=len(df.columns)+1, column=0)

    root.mainloop()



def Khung_search_data():
    
    root = Tk()
    root.title("Tìm kiếm dữ liệu")
    root.geometry('')
    frame = Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")
    columns = list(df.columns)
    selected_column = StringVar(root)
    selected_column.set(columns[0])
    label = Label(frame, text="Chọn cột:")
    label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    column_menu = OptionMenu(frame, selected_column, *columns)
    column_menu.config(width=50)
    column_menu.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    label_search = Label(frame, text="Nhập giá trị tìm kiếm:")
    label_search.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    search_entry = Entry(frame)
    search_entry.config(width=50)
    search_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    tree = Treeview(frame, columns=columns, show='headings', style="mystyle.Treeview")
    for column in columns:
        tree.heading(column, text=column)
        tree.column(column, width=100)
    tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    scrollbar_y = Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar_y.grid(row=2, column=2, pady=10, sticky="ns")
    tree.configure(yscrollcommand=scrollbar_y.set)
    scrollbar_x = Scrollbar(frame, orient="horizontal", command=tree.xview)
    scrollbar_x.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    tree.configure(xscrollcommand=scrollbar_x.set)
    Button(frame, text='Tìm kiếm', command=lambda: search_and_display(df, selected_column.get(), search_entry.get(), tree)).grid(row=4, column=0, pady=10, sticky="ew", columnspan=2)
    root.mainloop()
    
def load_Dictionary():
    root2=Tk() #
    root2.title("Dictionary") #
    root2.geometry('400x400')

    text1=Text(root2)
    text1.pack()
    
    
    def show():
        global df
        mydict=eval(text1.get("1.0", END))
        df=loadDictionary(mydict)
        display_data_and_info(df, tree, info_text_widget)
    
    button=tk.Button(root2,text="chuyển",command=show)
    button.pack()
    
    root2.mainloop()
def load_list():
    root2=Tk() #
    root2.title("Python list") #
    root2.geometry('400x400')

    text1=Text(root2)
    text1.pack()
    
    
    def show():
        mylist=eval(text1.get("1.0", END))
        newdf=loadDictionary(mylist)
        display_data_and_info(newdf, tree, info_text_widget)
    
    button=tk.Button(root2,text="chuyển",command=show)
    button.pack()
    
    root2.mainloop()

def shuffle_and_display():
    global df
    shuffled_df = shuffle_data(df)
    if shuffled_df is not None:
        df = shuffled_df
        display_data_and_info(df, tree, info_text_widget)
    
def save_data_to_file():
    global df
    save_data(df)
def rename_columns():
    global df

    def update_columns(new_names):
        global df
        df.columns = new_names
        display_data_and_info(df, tree, info_text_widget)
        top.destroy()

    top = Toplevel()
    top.title("Đổi tên cột")
    top.geometry('')

    current_columns = df.columns.tolist()

    label_current_columns = Label(top, text="Các cột hiện tại:")
    label_current_columns.pack(padx=10, pady=10)

    current_columns_text = scrolledtext.ScrolledText(top, width=30, height=5)
    current_columns_text.insert(INSERT, "\n".join(current_columns))
    current_columns_text.pack(padx=10, pady=10)

    label_new_columns = Label(top, text="Nhập tên mới cho các cột (phân tách bằng dấu phẩy):")
    label_new_columns.pack(padx=10, pady=10)

    new_columns_entry = Entry(top)
    new_columns_entry.pack(padx=10, pady=10)

    def perform_rename():
        new_names = [name.strip() for name in new_columns_entry.get().split(',')]
        if len(new_names) != len(current_columns):
            messagebox.showwarning("Lỗi", "Số lượng cột mới không khớp với số lượng cột hiện tại.")
        else:
            update_columns(new_names)

    button_rename = Button(top, text='Đổi tên', command=perform_rename)
    button_rename.pack(pady=10)

root = tk.Tk()
root.title("Quản lý dữ liệu")
root.wm_state('zoomed')

style = Style(theme='darkly')
notebook = ttk.Notebook(root)
notebook.pack(pady=10, padx=10, expand=True, fill='both')

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

file_menu_1 = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Tài Liệu", menu=file_menu_1)
file_menu_1.add_command(label="Tải dữ liệu lên ", command=load_and_display)
file_menu_1.add_command(label="Lưu tài liệu xuống", command=save_data_to_file)
file_menu_1.add_command(label="Chuyển dictionary sang dataFrame",command=load_Dictionary)
file_menu_1.add_command(label="Chuyển list sang dataFrame",command=load_list)
file_menu_1.add_command(label="Nối thêm dữ liệu",command=load_more_data_and_display)


file_menu_2 = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Chức Năng", menu=file_menu_2)
file_menu_2.add_command(label="Xáo trộn tài liệu", command=shuffle_and_display)
file_menu_2.add_command(label="Xóa trùng lặp",command=drop_duplicate_and_display)
file_menu_2.add_command(label="Xóa các dòng có Null",command=remove_Null)
file_menu_2.add_command(label="Tính toán",command=khung_tinh_toan)
file_menu_2.add_command(label="Thay thế giá trị null bằng một giá trị khác",command=replace_null_option)
file_menu_2.add_command(label="Đổi tên cột", command=rename_columns)

add_edit_delete = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Thêm Sửa Xóa", menu=add_edit_delete)
add_edit_delete.add_command(label="Thêm dữ liệu",command=khung_add_data)
add_edit_delete.add_command(label="Chỉnh sửa dữ liệu",command=Khung_edit_data)
add_edit_delete.add_command(label="Xóa dữ liệu",command=Khung_delete_data)


sort_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Sắp xếp", menu=sort_menu)
sort_menu.add_command(label="Sắp xếp", command=sortAscending)


find_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Tìm kiếm dữ liệu", command=Khung_search_data)
reset_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Reset", command=reset_button)
root.mainloop()