import pandas as pd
import tkinter.messagebox as messagebox

def sort_ID_ascending(df):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu", "Vui lòng tải dữ liệu trước khi sắp xếp!")
        return None
    sorted_df = df.sort_values('Student ID')
    return sorted_df

def sort_ID_descending(df):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu", "Vui lòng tải dữ liệu trước khi sắp xếp!")
        return None
    sorted_df = df.sort_values('Student ID',ascending=False)
    return sorted_df

def sort_Name(df):
    # if df is None or df.empty:
    #     messagebox.showwarning("Không có dữ liệu", "Vui lòng tải dữ liệu trước khi sắp xếp!")
    #     return None
    # df['middle_name'] = df['Full Name'].apply(lambda x: ' '.join(x.split()[1:-1]) if len(x.split()) > 2 else None)

    # # Sắp xếp DataFrame theo 'middle_name'
    # sorted_df = df.sort_values('middle_name')

    # # Xóa cột 'middle_name' vì nó chỉ được sử dụng để sắp xếp
    # sorted_df = sorted_df.drop(columns=['middle_name'])
    sorted_df = df.sort_values('Full Name')
    return sorted_df

def sort_Age(df):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu", "Vui lòng tải dữ liệu trước khi sắp xếp!")
        return None
    sorted_df = df.sort_values('Age')
    return sorted_df

def sort_Gender(df):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu", "Vui lòng tải dữ liệu trước khi sắp xếp!")
        return None
    sorted_df = df.sort_values('Gender')
    return sorted_df  

def sort_Class(df):
    if df is None or df.empty:
        messagebox.showwarning("Không có dữ liệu", "Vui lòng tải dữ liệu trước khi sắp xếp!")
        return None
    sorted_df = df.sort_values('Class')
    return sorted_df  