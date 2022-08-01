import pytest
import pandas as pd
import datatest as dt


@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def df():
    return pd.read_csv('data.csv')


@pytest.mark.mandatory
def test_columns(df):
    dt.validate(
        df.columns,
        {'Date', 'ID', 'Make', 'Model', 'Price', 'UserID'},

    )







