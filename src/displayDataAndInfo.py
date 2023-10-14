import tkinter as tk

def display_data_and_info(df, tree, info_text_widget):
    for i in tree.get_children():
        tree.delete(i)
    tree['columns'] = tuple(df.columns)
    for col in df.columns:
        tree.column(col, anchor='center')
        tree.heading(col, text=col)
    for index, row in df.iterrows():
        tree.insert("", 'end', values=tuple(row))
    if not df.empty:
        info_text = "Shape: {}\n\nColumns: {}\n\nData Types:\n{}".format(df.shape, df.columns.tolist(), df.dtypes)
    else:
        info_text = "No data available."
    info_text_widget.delete('1.0', tk.END)
    info_text_widget.insert('1.0', info_text)
