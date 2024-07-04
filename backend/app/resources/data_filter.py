from app.services.data_scaling import filter_and_prepare_data, combine_features
from app.validation.validation import validate_year_range, validate_country_exists, validate_query_params
from flask import abort

def filter_data(country_name, start_year, end_year, query_params, mental_health_data, world_happiness_data, gdp_data, available_countries):
    # Validate the year range to ensure it's valid
    # This checks that the start year is less than or equal to the end year
    validate_year_range(start_year, end_year)
    
    # Validate that the country exists in the available countries list
    # This checks that the country name is in the list of available countries
    validate_country_exists(country_name, available_countries)
    
    # Get the valid parameters by combining the columns of the three dataframes
    # This creates a set of all the column names in the three dataframes, plus 'GDP'
    valid_params = set(mental_health_data.columns) | set(world_happiness_data.columns) | {'GDP'}
    
    # Validate the query parameters to ensure they are valid
    # This checks that the query parameters are in the set of valid parameters
    validate_query_params(query_params, valid_params)
    
    # Convert the country name to lowercase for case-insensitive matching
    country_name_lower = country_name.lower()
    
    # Filter the mental health data for the specified country and year range
    # This uses boolean indexing to select the rows where the country name matches and the year is within the specified range
    # The resulting dataframe is then set to have the 'Year' column as the index
    mh_filtered = mental_health_data[
        (mental_health_data['Country-name'].str.lower() == country_name_lower) &
        (mental_health_data['Year'].between(int(start_year), int(end_year)))
    ].set_index('Year')
    
    # Filter the world happiness data for the specified country and year range
    # This uses boolean indexing to select the rows where the country name matches and the year is within the specified range
    # The resulting dataframe is then set to have the 'Year' column as the index
    wh_filtered = world_happiness_data[
        (world_happiness_data['Country-name'].str.lower() == country_name_lower) &
        (world_happiness_data['Year'].between(int(start_year), int(end_year)))
    ].set_index('Year')
    
    # Filter the GDP data for the specified country and year range
    # This uses boolean indexing to select the rows where the country name matches and the year is within the specified range
    # The resulting dataframe is then set to have the 'Year' column as the index
    gdp_filtered = gdp_data[
        (gdp_data['Country-name'].str.lower() == country_name_lower) &
        (gdp_data['Year'].between(int(start_year), int(end_year)))
    ].set_index('Year')
    
    # If no data is available for the specified country and year range, return a 404 error
    # This checks if all three filtered dataframes are empty, and if so, returns a 404 error with a descriptive message
    if mh_filtered.empty and wh_filtered.empty and gdp_filtered.empty:
        abort(404, description=f"No data available for {country_name} between {start_year} and {end_year}")
    
    # Filter and prepare the data for the specified query parameters
    # This calls the filter_and_prepare_data function, which returns the filtered features and columns for each dataset
    mh_features, wh_features, gdp_features, mh_columns, wh_columns, gdp_column = filter_and_prepare_data(query_params, mh_filtered, wh_filtered, gdp_filtered)
    
    # Combine the filtered features into a single dataframe
    # This calls the combine_features function, which returns a single dataframe with the combined features
    combined_features = combine_features(mh_features, wh_features, gdp_features, start_year, end_year)
    
    # Return the combined features and the individual features for each dataset
    return combined_features, mh_features, wh_features, gdp_features