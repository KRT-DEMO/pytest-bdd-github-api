import pandas as pd
import pytest
import datacompy


def test_pandas():
    df1 = pd.read_csv('cities.csv')
    df2 = pd.read_csv('cities2.csv')

    compare = datacompy.Compare(
        df1,
        df2,
        join_columns='LatD',  # You can also specify a list of columns
        abs_tol=0,  # Optional, defaults to 0
        rel_tol=0,  # Optional, defaults to 0
        df1_name='Source',  # Optional, defaults to 'df1'
        df2_name='Target'  # Optional, defaults to 'df2'
    )
    compare.matches(ignore_extra_columns=False)
    # False

    # This method prints out a human-readable report summarizing and sampling differences
    print(compare.report())
