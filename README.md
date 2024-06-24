# Loan Repayment Competition
---

## Overview
This repo is associated with an old Kaggle competition. The goal of the competition is to predict whether a variety of loan types will default. 
It contains data ETL, some initial data analyses (more to come), and eventually modeling.


## Setup/Installation
1. Presupposes an existing miniconda/conda setup and an environment with `python>3.10` (via `pyproject.toml`)
2. Clone repo and navigate to the root level of the directory housing the repository
3. Within the appropriate conda/python environment, `pip install` or `pip install -e .` if you're actively developing


## Usage

### Data Preparation

1. Get the base data from [kaggle](https://www.kaggle.com/datasets/joebeachcapital/loan-default) and house in `./data` directory
2. With the appropriate conda environment activated, run the following in a python/Ipython terminal:

```python
from loan_repayment.data_flow import data_flow

data_flow()
```

3. The previous snippet of code will generate data and output it to `./data` as `clean_data.pkl`
4. To ensure that the data has been transformed appropriately (as anticipated) you can run integrity checks via a script:

```bash
python src/loan_repayment/etl/integrity_checks.py
```

### Data Analysis
**In Progress** 
Analytical work is in progress. Descriptions of work are to come.
[See analysis.ipynb](./notebooks/analysis.ipynb)
[See analysis_run2.ipynb](./notebooks/analysis_run2.ipynb)

## More Info
See the [project_overview.md](./project_overview.md) for a more detailed overview of work currently done.