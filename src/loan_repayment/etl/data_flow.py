import joblib

from .extraction import (
    dataframe_from_csv,
)
from .transformations import (
  drop_col,
  drop_zero_loans,
  drop_large_interest, 
  col_to_str,
  payment_progress_col
)

ANONYMIZE_LOAN_DEFAULT_FILEPATH = "./data/Anonymize_Loan_Default_data.csv"
OUTPUT_FILEPATH = "./data/clean_data.pkl"


def store_data(data, filepath):
    joblib.dump(data, filepath)


def data_flow(loan_data_filepath: str = ANONYMIZE_LOAN_DEFAULT_FILEPATH, output_filepath: str = OUTPUT_FILEPATH, return_data: bool = False):
    # Extraction
    df = dataframe_from_csv(loan_data_filepath)

    # Data processing
    df = drop_col(df, 'Unnamed: 0')  
    df = drop_zero_loans(df, 'loan_amnt')
    df = drop_large_interest(df, 'int_rate')
    df = col_to_str(df, 'id')
    df = col_to_str(df, 'member_id')
    df = payment_progress_col(df, 'prop_funded_amnt_paid')

    # Storing (Load)
    store_data(df, output_filepath)
    if return_data:
        return df
