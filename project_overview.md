# Summary

## Goal of Project
The goal of this project is to predict if a loan will default.

---

## Data Provided
* Anonymize_Loan_Default_data.csv - anonymised loan default data with 37 columns

---

## Data Handling

### Loading Data
I loaded in the data provided by Kaggle.

### Transforming Data
After inspecting the data, I wrote the following functions to clean up and do feature enginering on the data:
- drop_col() -- drops specified column such as the "Unnamed: 0" column that was created when reading the data in
- drop_zero_loans() -- drops rows with loans that are $0
- drop_large_interest() -- drops rows with interest rates greater than 100%
- col_to_str() -- converts all cells in specified column to string type, applied to "id" and "member_id"
- payment_progress_col() -- creates a column representing payment progress

### Storing Data
I exported the cleaned dataframe to the "data" folder using a third party package (joblib).

### Testing Transformations
I created a file to verify that the transformations done in data_flow resulted in the anticipated dataframe.

1) I created functions to:
- test that each trasformation was successful when cleaning the data
- if the transformation was unsuccessful, raise a Type Error 

2) I created a dictionary of all tests & results
- if anything in dict is false, print test name & fail
- if entire list dict keys are true, print("Date Flow successful!")

---

## Data Exploration

### Loading Data
I loaded in the data I had cleaned up, did feature engineering on and ran integrity checks on during data handing.

### Analysis
**TODO** Analytical work is in progress. Descriptions of work are to come.
[See analysis.ipynb](./notebooks/analysis.ipynb)
[See analysis_run2.ipynb](./notebooks/analysis_run2.ipynb)