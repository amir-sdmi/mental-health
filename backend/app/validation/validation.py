from flask import abort

#validate the year range, check if a country exists in the dataset, and validate the query parameters.

#Validate the year range input parameters. If start year is not less than end year or not between 2005 and 2017 then return 404 
def validate_year_range(start_year, end_year):
    if start_year >= end_year:
        abort(400, description="Invalid year range: startDate should be less than endDate")
    if start_year < 2005 or end_year > 2017:
        abort(400, description="Invalid year range: Data is available only between 2005 and 2017")
# check if country is exist 
def validate_country_exists(country_name, available_countries):
    if country_name.lower() not in [country.lower() for country in available_countries]:
        abort(404, description=f"Country '{country_name}' not found in the dataset")
# Validate the query parameters
def validate_query_params(query_params, valid_params):
    for param in query_params.keys():
        if param not in valid_params:
            abort(400, description=f"Invalid query parameter: {param}")