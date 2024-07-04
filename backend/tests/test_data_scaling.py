import pytest
import pandas as pd
from app.services.data_scaling import filter_and_prepare_data, combine_features

# Test the filter_and_prepare_data function
def test_filter_and_prepare_data():
    query_params = {'Schizophrenia': 'true'}
    # Create sample dataframes for mental health, world health, and GDP data
    mh_filtered = pd.DataFrame({
        'Year': [2008, 2009],
        'Schizophrenia': [0.1, 0.2]
    }).set_index('Year')
    wh_filtered = pd.DataFrame(columns=['Year']).set_index('Year')
    gdp_filtered = pd.DataFrame(columns=['Year']).set_index('Year')
# Call the filter_and_prepare_data
    mh_features, wh_features, gdp_features, mh_columns, wh_columns, gdp_column = filter_and_prepare_data(query_params, mh_filtered, wh_filtered, gdp_filtered)
# Assert the mental health is not empty
    assert not mh_features.empty
    # Assert that the mental health is correct
    assert mh_columns == {'Schizophrenia'}
# Test the combine_features function
def test_combine_features():
    mh_features = pd.DataFrame({
        'Year': [2008, 2009],
        'Schizophrenia': [0.1, 0.2]
    }).set_index('Year')
    wh_features = pd.DataFrame(columns=['Year']).set_index('Year')
    gdp_features = pd.DataFrame(columns=['Year']).set_index('Year')

    combined_features = combine_features(mh_features, wh_features, gdp_features, 2008, 2009)

    assert 'Schizophrenia' in combined_features.columns
