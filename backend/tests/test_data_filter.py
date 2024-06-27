import pytest
from app.resources.data_filter import filter_data
from app.resources.data_loader import mental_health_data, world_happiness_data, gdp_data, available_countries

def test_filter_data():
    country_name = 'Canada'
    start_year = 2008
    end_year = 2009
    query_params = {
        'Schizophrenia': 'true',
        'Life-Ladder': 'true',
        'GDP': 'true'
    }

    filtered_data, mh_features, wh_features, gdp_features = filter_data(
        country_name, start_year, end_year, query_params, 
        mental_health_data, world_happiness_data, gdp_data, available_countries
    )

    assert not filtered_data.empty
    assert 'Schizophrenia' in mh_features.columns
    assert 'Life-Ladder' in wh_features.columns
    assert 'GDP' in gdp_features.columns
