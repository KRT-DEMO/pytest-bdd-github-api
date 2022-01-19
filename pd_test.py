import pandas as pd
import pytest
from pytest_check import equal,is_true

def test_pandas():
    df = pd.read_csv('cities.csv')
    df2 = pd.read_csv('cities2.csv')

    # Does DF1 == DF2 True/False
    equal_result = df.equals(df2)
    is_true(equal_result)
    print(equal_result)

    # Does DF1 compare to DF2? if not the differences are exported in a DataFrame
    compare_result = df.compare(df2)
    print(compare_result)