# file: main.py
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
        mylabel3=Label(root1,text=f"Max của {clicked.get()} là: "+str(find_Average(clicked.get()))).pack()

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
        mydict=eval(text1.get("1.0", END))
        newdf=loadDictionary(mydict)
        display_data_and_info(newdf, tree, info_text_widget)
    
    button=tk.Button(root2,text="chuyển",command=show)
    button.pack()
    
    root2.mainloop()

    

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
file_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Load File", command=load_and_display)
file_menu.add_command(label="loại bỏ trùng lặp",command=drop_duplicate_and_display)
file_menu.add_command(label="Xóa các dòng có Null",command=remove_Null)
file_menu.add_command(label="Tính toán",command=khung_tinh_toan)
file_menu.add_command(label="Chuyển dictionary sang dataFrame",command=load_Dictionary)
root.mainloop()


