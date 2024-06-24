from flask import request
from flask_restful import Resource
import pandas as pd
import numpy as np

def load_data(filepath):
    return pd.read_csv(filepath)

mental_health_data = load_data('assets/Cleaned_Mental_Health_Data.csv')
world_happiness_data = load_data('assets/Cleaned_World_Happiness_Report_2005-2021.csv')

class DataQuery(Resource):
    def get(self, countryName, startDate, endDate):
        query_params = request.args
        years = list(range(startDate, endDate + 1))

        mh_filtered = mental_health_data[
            (mental_health_data['Entity'] == countryName)
        ].set_index('Year').reindex(years)

        wh_filtered = world_happiness_data[
            (world_happiness_data['Country name'] == countryName)
        ].set_index('Year').reindex(years)

        mh_columns = set(query_params.keys()).intersection(mh_filtered.columns)
        wh_columns = set(query_params.keys()).intersection(wh_filtered.columns)

        mh_features = mh_filtered[list(mh_columns)]
        wh_features = wh_filtered[list(wh_columns)]

        combined_features = pd.concat([mh_features, wh_features], axis=1, join='outer')

        for col in mh_columns.union(wh_columns):
            if col not in combined_features:
                combined_features[col] = np.nan

        combined_features = combined_features.fillna(np.nan)

        result_data = {
            "Disorders": {col: combined_features[col].tolist() for col in mh_columns},
            "Happiness": {col: combined_features[col].tolist() for col in wh_columns}
        }

        result = {
            'Country': countryName,
            'Start Year': startDate,
            'End Year': endDate,
            'Years': years,
            'Data': result_data
        }

        return result
