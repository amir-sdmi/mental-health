from flask_restful import Resource
from flask import request
from app.resources.data_loader import mental_health_data, world_happiness_data, gdp_data, available_countries
from app.resources.data_filter import filter_data
from app.services.regression_analysis import perform_regression
import logging

logging.basicConfig(level=logging.DEBUG)

class DataQuery(Resource):
    def get(self, countryName, startDate, endDate):
        query_params = request.args

        combined_features, mh_features, wh_features, gdp_features = filter_data(
            countryName, startDate, endDate, query_params, 
            mental_health_data, world_happiness_data, gdp_data, available_countries
        )

        logging.debug(f"Querying data for country: {countryName}, years: {startDate}-{endDate}")
        logging.debug(f"Combined features: {combined_features.head()}")

        regression_results = {}
        if 'GDP' in query_params and not combined_features.empty:
            for col in combined_features.columns:
                if col != 'GDP':
                    model, coefficients, intercept = perform_regression(combined_features, col)
                    if model is not None:
                        regression_results[col] = {
                            'coefficients': coefficients.tolist(),
                            'intercept': intercept
                        }

        result_data = {col: combined_features[col].tolist() for col in combined_features.columns}

        result = {
            'Country': countryName.capitalize(),
            'Start Year': startDate,
            'End Year': endDate,
            'Data': result_data,
            'Regression': regression_results
        }

        return result