
import pandas as pd

def concatenate_dataframes(df1, df2):
    # Nối hai DataFrame lại với nhau
    result = pd.concat([df1, df2])
    return result