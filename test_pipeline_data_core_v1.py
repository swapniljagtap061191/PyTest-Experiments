import pytest
import pandas as pd
import numpy as np
from numpy import nan

@pytest.fixture

def df():
    df = pd.read_excel(r'C:\Users\MK416SE\Downloads\Product.xlsx')
    return df

def test_col_exists(df):
    col_name = "ProductKey"
    assert col_name in df.columns

def test_null_check(df):
    assert df['ProductKey'].notnull().all()

def test_unique_check(df):
    assert pd.Series(df['ProductKey']).is_unique

def test_productkey_dtype_int(df):
    assert (df['ProductKey'].dtype == int or df['ProductKey'].dtype == np.int64)

def test_range_val(df):
    assert df['SafetyStockLevel'].between(0,1000).any()

def test_range_val_str(df):
    assert set(df.Color.unique()) == {nan, 'Black', 'Silver', 'Red', 'White', 'Blue', 'Multi', 'Yellow','Grey', 'Silver/Black'}