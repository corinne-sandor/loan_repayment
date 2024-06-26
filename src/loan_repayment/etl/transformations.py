import pandas as pd
from typing import Union


def drop_col(df: pd.DataFrame, col: str) -> pd.DataFrame:
    filtered = df.drop(col, axis = 1)
    return filtered


def drop_zero_loans(df: pd.DataFrame, loan_col: str = "loan_amnt") -> pd.DataFrame:
    drop_inds = df[loan_col] <= 0
    filtered = df[~drop_inds].reset_index(drop=True)
    return filtered


def drop_large_interest(df: pd.DataFrame, interest_col: str = "int_rate") -> pd.DataFrame:
    drop_inds = df[interest_col] > 100
    filtered = df[~drop_inds].reset_index(drop=True)
    return filtered


def col_to_str(df: pd.DataFrame, col: Union[str, dict]) -> pd.DataFrame:
    if type(col) == str:
        df[col] = df[col].astype(str)
    elif type(col) == dict:
        df = df.astype(col)
    return df

  
def payment_progress_col(df: pd.DataFrame, output_col: str = "prop_funded_amnt_paid") -> pd.DataFrame:
    """Create a column representing payment progress
    
    Args:
        df: A DataFrame that must necessarily contain columns 'total_pymnt' and 'funded_amnt'
    
    Returns:
        A DataFrame with a new column with same name as output_col arg
    """
    # Perform checks to see if columns in DF exist
    necessary_cols = {"total_pymnt", "funded_amnt"}
    if necessary_cols.intersection(set(df.columns)) != necessary_cols:
        raise ValueError("Necessary columns both not present. Check data")
    else:
        df[output_col] = df['total_pymnt'] / df['funded_amnt']
    return df
