from flask import request, abort
from flask_restful import Resource
import pandas as pd
from app.services.data_scaling import filter_and_prepare_data, combine_features
from app.services.regression_analysis import perform_regression
import logging

logging.basicConfig(level=logging.DEBUG)

def load_data(filepath):
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        abort(404, description=f"File not found: {filepath}")

# Load data
mental_health_data = load_data('./app/assets/Cleaned_Mental_Health_Data.csv')
world_happiness_data = load_data('./app/assets/Cleaned_World_Happiness_Report_2005-2021.csv')
gdp_data = load_data('./app/assets/GDP_per_cap.csv')

# Preprocess GDP data
gdp_data = gdp_data.melt(id_vars=['Country-name'], var_name='Year', value_name='GDP')
gdp_data['Year'] = gdp_data['Year'].astype(int)

class DataQuery(Resource):
    def get(self, countryName, startDate, endDate):
        query_params = request.args
        countryName_lower = countryName.lower()

        mh_filtered = mental_health_data[
            (mental_health_data['Country-name'].str.lower() == countryName_lower) &
            (mental_health_data['Year'].between(int(startDate), int(endDate)))
        ].set_index('Year')

        wh_filtered = world_happiness_data[
            (world_happiness_data['Country-name'].str.lower() == countryName_lower) &
            (world_happiness_data['Year'].between(int(startDate), int(endDate)))
        ].set_index('Year')

        gdp_filtered = gdp_data[
            (gdp_data['Country-name'].str.lower() == countryName_lower) &
            (gdp_data['Year'].between(int(startDate), int(endDate)))
        ].set_index('Year')

        logging.debug(f"Querying data for country: {countryName_lower}, years: {startDate}-{endDate}")
        logging.debug(f"Mental health features: {mh_filtered.head()}")
        logging.debug(f"World happiness features: {wh_filtered.head()}")
        logging.debug(f"GDP features: {gdp_filtered.head()}")

        mh_features, wh_features, gdp_features, mh_columns, wh_columns, gdp_column = filter_and_prepare_data(query_params, mh_filtered, wh_filtered, gdp_filtered)

        combined_features = combine_features(mh_features, wh_features, gdp_features, startDate, endDate)

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
