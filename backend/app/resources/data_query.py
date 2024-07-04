# from flask_restful import Resource
# from flask import request, jsonify
# import pandas as pd
# from app.resources.data_loader import mental_health_data, world_happiness_data, gdp_data, available_countries
# from app.resources.data_filter import filter_data
# from app.services.regression_analysis import perform_regression
# import logging
# import numpy as np

# logging.basicConfig(level=logging.DEBUG)

# class DataQuery(Resource):
#     def get(self, countryName, startDate, endDate):
#         query_params = request.args

#         combined_features, mh_features, wh_features, gdp_features = filter_data(
#             countryName, startDate, endDate, query_params, 
#             mental_health_data, world_happiness_data, gdp_data, available_countries
#         )

#         logging.debug(f"Querying data for country: {countryName}, years: {startDate}-{endDate}")
#         logging.debug(f"Combined features: {combined_features.head()}")

#         regression_results = {}
#         if 'GDP' in query_params and not combined_features.empty:
#             for col in combined_features.columns:
#                 if col != 'GDP':
#                     model, coefficients, intercept = perform_regression(combined_features, col)
#                     if model is not None:
#                         regression_results[col] = {
#                             'coefficients': coefficients.tolist(),
#                             'intercept': intercept
#                         }

#         # Convert DataFrame to dict and replace NaN with None (null in JSON)
#         result_data = combined_features.replace({np.nan: None}).to_dict(orient='list')

#         result = {
#             'Country': countryName.capitalize(),
#             'Start Year': startDate,
#             'End Year': endDate,
#             'Data': result_data,
#             'Regression': regression_results
#         }

#         return jsonify(result)




from flask_restful import Resource
from flask import request, jsonify  
import pandas as pd  
from app.resources.data_loader import (
    mental_health_data, 
    world_happiness_data, 
    gdp_data, 
    available_countries
)
from app.resources.data_filter import filter_data
from app.services.regression_analysis import perform_regression
import logging 
import numpy as np



class DataQuery(Resource):
    # handle GET request
    def get(self, countryName, startDate, endDate):
        query_params = request.args

        # Filter data based on country name, start date, end date, and query parameters
        combined_features, mh_features, wh_features, gdp_features = filter_data(
            countryName, startDate, endDate, query_params, 
            mental_health_data, world_happiness_data, gdp_data, available_countries
        )


        

        # Initialize regression results dictionary
        regression_results = {}

        # analysis if 'GDP' is in query parameters and combined features is not empty
        if 'GDP' in query_params and not combined_features.empty:
            for col in combined_features.columns:
                if col!= 'GDP':
                    # analysis for each column (except 'GDP')
                    model, coefficients, intercept = perform_regression(combined_features, col)
                    if model is not None:
                        regression_results[col] = {
                            'coefficients': coefficients.tolist(),
                            'intercept': intercept
                        }

        # Convert combined features DataFrame to a dictionary, replacing NaN with None 
        # With this I can convert The NaN values to null so front end can use it in response JSON
        result_data = combined_features.replace({np.nan: None}).to_dict(orient='list')

        # Create the result dictionary
        result = {
            'Country': countryName.capitalize(),
            'Start Year': startDate,
            'End Year': endDate,
            'Data': result_data,
            'Regression': regression_results
        }

        # Return the result as a JSON response
        return jsonify(result)