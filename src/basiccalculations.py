import pandas as pd
import tkinter.messagebox as messagebox

def findMin(df,a):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu")
        return None 
    x=df[a].min()
    print(f"Giá trị nhỏ nhất của {a} là: {x}")
def findMax(df,a):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu")
        return None 
    x=df[a].max()
    print(f"Giá trị lớn nhất của {a} là: {x}")
def findAverage(df,a):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu")
        return None 
    x=df[a].mean()
    print(f"Giá trị trung bình của {a} là: {x}")
def findCountNoCondition(df,a):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu")
        return None 
    x=df[a].count()
    print(f"Số lượng phần tử của {a} là: {x}")
def findCountHaveCondition(df,a):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu")
        return None 
    x=df[a].count()
    print(f"Số lượng phần tử của {a} là: {x}")



    