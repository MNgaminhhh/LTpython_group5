import pandas as pd
import tkinter.messagebox as messagebox

def replaceNullwithmedium(df,a):
    tb = df[a].mean()
    df[a] = df[a].fillna(tb)
    return df
def replaceNullwithmin(df,a):
    mindf = df[a].min()
    df[a] = df[a].fillna(mindf)
    return df
def replaceNullwithmax(df,a):
    maxdf= df[a].max()
    df[a] = df[a].fillna(maxdf)
    return df
