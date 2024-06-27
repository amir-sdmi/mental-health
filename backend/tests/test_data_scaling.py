import pytest
import pandas as pd
from app.services.data_scaling import filter_and_prepare_data, combine_features

def test_filter_and_prepare_data():
    query_params = {'Schizophrenia': 'true'}
    mh_filtered = pd.DataFrame({
        'Year': [2008, 2009],
        'Schizophrenia': [0.1, 0.2]
    }).set_index('Year')
    wh_filtered = pd.DataFrame(columns=['Year']).set_index('Year')
    gdp_filtered = pd.DataFrame(columns=['Year']).set_index('Year')

    mh_features, wh_features, gdp_features, mh_columns, wh_columns, gdp_column = filter_and_prepare_data(query_params, mh_filtered, wh_filtered, gdp_filtered)

    assert not mh_features.empty
    assert mh_columns == {'Schizophrenia'}

def test_combine_features():
    mh_features = pd.DataFrame({
        'Year': [2008, 2009],
        'Schizophrenia': [0.1, 0.2]
    }).set_index('Year')
    wh_features = pd.DataFrame(columns=['Year']).set_index('Year')
    gdp_features = pd.DataFrame(columns=['Year']).set_index('Year')

    combined_features = combine_features(mh_features, wh_features, gdp_features, 2008, 2009)

    assert 'Schizophrenia' in combined_features.columns
