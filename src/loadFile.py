import pandas as pd
from tkinter import filedialog

def load_file():
    file_path = filedialog.askopenfilename(title="Chọn", filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
    if file_path:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            print("Không hỗ trợ định dạng này !")
            return None
    else:
        print("Không có file nào được chọn.")
        return None
    return df
