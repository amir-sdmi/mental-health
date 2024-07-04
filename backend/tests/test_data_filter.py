import pytest
from app.resources.data_filter import filter_data
from app.resources.data_loader import mental_health_data, world_happiness_data, gdp_data, available_countries

def test_filter_data():
     #test parameters
    country_name = 'Canada'
    start_year = 2008
    end_year = 2009
    # Filter by Schizophrenia
    query_params = {'Schizophrenia': 'true'}
# Call the filter_data with test parameters
    combined_features, mh_features, wh_features, gdp_features = filter_data(
        country_name, start_year, end_year, query_params,
        mental_health_data, world_happiness_data, gdp_data, available_countries
    )
# assert that the resulting dataframes are not empty
    assert not combined_features.empty
    assert not mh_features.empty
    assert not wh_features.empty
    assert not gdp_features.empty
