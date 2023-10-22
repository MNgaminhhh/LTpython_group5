import pandas as pd
from tkinter import filedialog

def loadDictionary(dict):
    df=pd.DataFrame(dict, index=[0])
    return df