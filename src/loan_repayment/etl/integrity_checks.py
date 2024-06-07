# this file is to check that the transformations done in data_flow resulted in 
# the anticipated dataframe

import joblib
from pandas import DataFrame, Series
from typing import Union


def drop_col_test(post_process_cols, col: str = 'Unnamed: 0'):
    # test to see if 'Unnamed: 0" column was dropped
    return col not in post_process_cols


def drop_zero_loans_test(loan_amnt_data: Series):
    # test to see if zero loans were dropped
    if not isinstance(loan_amnt_data, Series):
        raise TypeError(f'Must pass a Pandas Series. Passed {type(loan_amnt_data)}')
    return loan_amnt_data.min() > 0


def drop_large_interest_test(int_rate_data: Series):
    # test to see if int_rates > 100 were dropped
    if not isinstance(int_rate_data, Series):
        raise TypeError(f'Must pass a Pandas Series. Passed {type(int_rate_data)}')
    return int_rate_data.min() < 100
    
    
def to_str_test(id_data: Series):
    # test to see if 'id' and 'member id' columns are objects
    if not isinstance(id_data, Series):
        raise TypeError(f'Must pass a Pandas Series. Passed {type(id_data)}')
    return id_data.dtype == "O"


def in_col_test(post_process_cols, col: str = 'prop_funded_amnt_paid'):
    # test to see if payment progress column was created
    return col in post_process_cols

        
if __name__ == "__main__":
    OUTPUT_FILEPATH = "./data/clean_data.pkl"
    df = joblib.load(OUTPUT_FILEPATH)
    post_process_cols = df.columns


#create dict of all tests & results
#if anything in dict is false, print test name & fail
#if entire list dict keys are true, print("Date Flow successful!")

QA_tests = {'drop_col_test': drop_col_test(post_process_cols),
            'drop_zero_loans_test': drop_zero_loans_test(df.loan_amnt),
            'drop_large_interest_test': drop_large_interest_test(df.int_rate),
            'id_to_str_test': to_str_test(df.id),
            'member_id_to_str_test': to_str_test(df.member_id),
            'in_col_test': in_col_test(post_process_cols)}

flow_successful = True
for key, value in QA_tests.items():
    if QA_tests[key] == False:
        flow_successful = False
        print(f'Test failed for {key}')

if flow_successful:
    print('Data Flow Successful! :D')
