import pandas as pd
import tkinter.messagebox as messagebox

def findMin(df,a):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu")
        return None 
    x=df[a].min()
    return x
def findMax(df,a):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu")
        return None 
    x=df[a].max()
    return x
def findAverage(df,a):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu")
        return None 
    x=df[a].mean()
    return x
def findCountNoCondition(df,a):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu")
        return None 
    x=df[a].count()
    print(f"Số lượng phần tử của {a} là: {x}")
#def findCountHaveCondition(df,a):
#    if df is None or df.empty:
#        messagebox.showwarning("Không có dữ liệu")
#        return None 
#    x=df[a].count()
#    print(f"Số lượng phần tử của {a} là: {x}")



    