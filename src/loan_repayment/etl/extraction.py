import pandas as pd

def dataframe_from_csv(filepath):
    return pd.read_csv(filepath, encoding='unicode_escape')
