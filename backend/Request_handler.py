from flask import request
from flask_restful import Resource
import pandas as pd
from services.data_scaling import filter_and_prepare_data

def load_data(filepath):
    return pd.read_csv(filepath)

# Load data
mental_health_data = load_data('./assets/Cleaned_Mental_Health_Data.csv')
world_happiness_data = load_data('./assets/Cleaned_World_Happiness_Report_2005-2021.csv')
gdp_data = load_data('./assets/GDP_per_cap.csv')

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

        mh_features, wh_features, gdp_features, mh_columns, wh_columns, gdp_column = filter_and_prepare_data(query_params, mh_filtered, wh_filtered, gdp_filtered)

        combined_features = pd.concat([mh_features, wh_features, gdp_features], axis=1, join='outer')

        result_data = {col: combined_features[col].to_list() for col in combined_features.columns}

        result = {
            'Country': countryName.capitalize(),
            'Start Year': startDate,
            'End Year': endDate,
            'Data': result_data
        }

        return result
