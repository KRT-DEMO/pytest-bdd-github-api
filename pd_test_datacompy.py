import datetime
import pandas as pd
import datacompy


def test_datacompy():
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


def test_datacompy_excel_to_csv():
    df1 = pd.read_excel('OrderInfo.xlsx', dtype=str)
    df2 = pd.read_csv('OrderInfo.csv', dtype=str)

    df1["OrderDate"] = df1["OrderDate"].apply(
        lambda x: datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d"))
    df2["OrderDate"] = df2["OrderDate"].apply(
        lambda x: datetime.datetime.strptime(x, "%m/%d/%Y").strftime("%Y-%m-%d"))

    # Trim commas from values
    df2["Total"] = df2["Total"].apply(
        lambda x: x.replace(',', ''))

    compare = datacompy.Compare(
        df1,
        df2,
        join_columns='Region',  # You can also specify a list of columns
        abs_tol=0,  # Optional, defaults to 0
        rel_tol=0,  # Optional, defaults to 0
        df1_name='Source',  # Optional, defaults to 'df1'
        df2_name='Target'  # Optional, defaults to 'df2'
    )
    compare.matches(ignore_extra_columns=False)
    # False

    # This method prints out a human-readable report summarizing and sampling differences
    print(compare.report())
