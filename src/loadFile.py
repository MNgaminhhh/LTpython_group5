import pandas as pd
from tkinter import filedialog

def load_file():
    file_path = filedialog.askopenfilename(title="Select File", filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
    if file_path:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
    return df
