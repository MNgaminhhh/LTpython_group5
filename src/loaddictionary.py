import pandas as pd
from tkinter import filedialog

def loadDictionary(dict):
    df=pd.DataFrame(dict)
    return df