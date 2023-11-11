import pandas as pd 
import tkinter as tk
from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk
from tkinter import Menu
from src.loadFile import load_file
from src.displayDataAndInfo import display_data_and_info
from src.dropduplicate import dropDuplicate
from src.removeNullValue import removeNullValue
from src.basiccalculations import findMin
from src.basiccalculations import findMax
from src.basiccalculations import findAverage
from src.basiccalculations import findCountNoCondition
from src.loaddictionary import loadDictionary
from src.replaceNullValue import replaceNullwithmax
from src.replaceNullValue import replaceNullwithmedium
from src.replaceNullValue import replaceNullwithmin
from src.shuffleData import shuffle_data
from src.saveFile import save_data
def load_and_display():
    global df
    df = load_file()
    display_data_and_info(df, tree, info_text_widget)
def drop_duplicate_and_display():
    global df
    drop_duplicates_df = dropDuplicate(df)
    if drop_duplicates_df is not None:
        df = drop_duplicates_df  # Cập nhật df sau khi loại bỏ dòng trùng lặp
        display_data_and_info(df, tree, info_text_widget)
def remove_Null():
    global df
    remove_null_df = removeNullValue(df)
    if remove_null_df is not None:
        df = remove_null_df  # Cập nhật df sau khi loại bỏ dòng có giá trị null
        display_data_and_info(df, tree, info_text_widget)
def find_Min(column):
    global df
    a=findMin(df,column)
    return a
def find_Max(column):
    global df
    a=findMax(df,column)
    return a
def find_Average(column):
    global df
    a=findAverage(df,column)
    return a
def replace_null_with_min(column):
    global df
    replace_null_df = replaceNullwithmin(df, column)
    if replace_null_df is not None:
        df = replace_null_df
        display_data_and_info(df, tree, info_text_widget)
def replace_null_with_max(column):
    global df
    replace_null_df = replaceNullwithmax(df, column)
    if replace_null_df is not None:
        df = replace_null_df
        display_data_and_info(df, tree, info_text_widget)
def replace_null_with_medium(column):
    global df
    replace_null_df = replaceNullwithmedium(df, column)
    if replace_null_df is not None:
        df = replace_null_df
        display_data_and_info(df, tree, info_text_widget)
def replace_null_option():
    root3=Tk() #
    root3.title("Basic Caculations") #
    root3.geometry('400x200')
    
    label=Label(root3,text='Option')
    label.place(x=20,y=20)

    label1=Label(root3,text="Thuộc tính")
    label1.place(x=20,y=80)

    global df
    column=list(df.columns)
    option=list(["Replace Null with Min","Replace Null with Max","Replace Null with Medium"])
    
    clicked1=StringVar(root3)
    clicked1.set(option[0])

    clicked2=StringVar(root3)
    clicked2.set(column[0])

    def selected():
        if clicked1.get()==option[0]:
            replace_null_with_min(clicked2.get())
        elif clicked1.get()==option[1]:
            replace_null_with_max(clicked2.get())
        elif clicked1.get()==option[2]:
            replace_null_with_medium(clicked2.get())
    drop=OptionMenu(root3,clicked1,*option)
    drop.config(width=30)
    drop.pack(pady=20)

    drop=OptionMenu(root3,clicked2,*column)
    drop.config(width=30)
    drop.pack(pady=20)

    button=tk.Button(root3,text="Thay thế",command=selected)
    button.place(x=60,y=60)
    button.pack()
    root3.mainloop()
def khung_tinh_toan():
    root1=Tk() #
    root1.title("Basic Caculations") #
    root1.geometry('400x400')
    
    label=Label(root1,text='Thuộc tính')
    label.place(x=20,y=20)

    global df
    column=list(df.columns)
    
    clicked=StringVar(root1)
    clicked.set(column[0])

    def selected(ev):
        mylabel=Label(root1,text=f"Min của {clicked.get()} là: "+str(find_Min(clicked.get()))).pack()
        mylabel1=Label(root1,text=f"Max của {clicked.get()} là: "+str(find_Max(clicked.get()))).pack()
        mylabel3=Label(root1,text=f"Giá trị trung bình của {clicked.get()} là: "+str(find_Average(clicked.get()))).pack()

    drop=OptionMenu(root1,clicked,*column,command=selected)
    drop.config(width=30)
    drop.pack(pady=20)
    root1.mainloop()
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
        df = shuffled_df  # Cập nhật df sau khi xáo trộn dữ liệu
        display_data_and_info(df, tree, info_text_widget)
    
def save_data_to_file():
    global df
    save_data(df)

root = tk.Tk()
root.title("Quản lý dữ liệu học tập")
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

file_menu_2 = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Chức Năng", menu=file_menu_2)
file_menu_2.add_command(label="Xáo trộn tài liệu", command=shuffle_and_display)
file_menu_2.add_command(label="loại bỏ trùng lặp",command=drop_duplicate_and_display)
file_menu_2.add_command(label="Xóa các dòng có Null",command=remove_Null)
file_menu_2.add_command(label="Tính toán",command=khung_tinh_toan)
file_menu_2.add_command(label="Thay thế giá trị null bằng một giá trị khác",command=replace_null_option)
root.mainloop()


