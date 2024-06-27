from flask import abort

def validate_year_range(start_year, end_year):
    if start_year >= end_year:
        abort(400, description="Invalid year range: startDate should be less than endDate")
    if start_year < 2005 or end_year > 2017:
        abort(400, description="Invalid year range: Data is available only between 2005 and 2017")

def validate_country_exists(country_name, available_countries):
    if country_name.lower() not in [country.lower() for country in available_countries]:
        abort(404, description=f"Country '{country_name}' not found in the dataset")

def validate_query_params(query_params, valid_params):
    for param in query_params.keys():
        if param not in valid_params:
            abort(400, description=f"Invalid query parameter: {param}")
