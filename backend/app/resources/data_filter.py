from app.services.data_scaling import filter_and_prepare_data, combine_features
from app.validation.validation import validate_year_range, validate_country_exists, validate_query_params
from flask import abort

def filter_data(country_name, start_year, end_year, query_params, mental_health_data, world_happiness_data, gdp_data, available_countries):
    validate_year_range(start_year, end_year)
    validate_country_exists(country_name, available_countries)

    valid_params = set(mental_health_data.columns) | set(world_happiness_data.columns) | {'GDP'}
    validate_query_params(query_params, valid_params)

    country_name_lower = country_name.lower()

    mh_filtered = mental_health_data[
        (mental_health_data['Country-name'].str.lower() == country_name_lower) &
        (mental_health_data['Year'].between(int(start_year), int(end_year)))
    ].set_index('Year')

    wh_filtered = world_happiness_data[
        (world_happiness_data['Country-name'].str.lower() == country_name_lower) &
        (world_happiness_data['Year'].between(int(start_year), int(end_year)))
    ].set_index('Year')

    gdp_filtered = gdp_data[
        (gdp_data['Country-name'].str.lower() == country_name_lower) &
        (gdp_data['Year'].between(int(start_year), int(end_year)))
    ].set_index('Year')

    if mh_filtered.empty and wh_filtered.empty and gdp_filtered.empty:
        abort(404, description=f"No data available for {country_name} between {start_year} and {end_year}")

    mh_features, wh_features, gdp_features, mh_columns, wh_columns, gdp_column = filter_and_prepare_data(query_params, mh_filtered, wh_filtered, gdp_filtered)
    combined_features = combine_features(mh_features, wh_features, gdp_features, start_year, end_year)

    return combined_features, mh_features, wh_features, gdp_features
