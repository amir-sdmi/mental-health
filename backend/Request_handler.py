

# from flask import request
# from flask_restful import Resource
# import pandas as pd
# from services.data_scaling import scale_data_with_global_min_max, global_min, global_max

# def load_data(filepath):
#     return pd.read_csv(filepath)

# # Load data
# mental_health_data = load_data('assets/Cleaned_Mental_Health_Data.csv')
# world_happiness_data = load_data('assets/Cleaned_World_Happiness_Report_2005-2021.csv')

# class DataQuery(Resource):
#     def get(self, countryName, startDate, endDate):
#         
#         query_params = request.args
#         mh_filtered = mental_health_data[
#             (mental_health_data['Entity'] == countryName) &
#             (mental_health_data['Year'].between(int(startDate), int(endDate)))
#         ].set_index('Year')

#         wh_filtered = world_happiness_data[
#             (world_happiness_data['Country name'] == countryName) &
#             (world_happiness_data['Year'].between(int(startDate), int(endDate)))
#         ].set_index('Year')
#         mh_columns = set(query_params.keys()).intersection(mh_filtered.columns)
#         wh_columns = set(query_params.keys()).intersection(wh_filtered.columns)
        
#         mh_features = mh_filtered[list(mh_columns)]
#         wh_features = wh_filtered[list(wh_columns)]

#         combined_features = pd.concat([mh_features, wh_features], axis=1, join='inner')
#         scaled_data = scale_data_with_global_min_max(combined_features, global_min, global_max)
#         result_data = {col: scaled_data[col].to_dict() for col in scaled_data.columns}

#         result = {
#             'Country': countryName,
#             'Start Year': startDate,
#             'End Year': endDate,
#             'Data': result_data
#         }

#         return result

from flask import request
from flask_restful import Resource
import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)


mental_health_data = load_data('assets/Cleaned_Mental_Health_Data.csv')
world_happiness_data = load_data('assets/Cleaned_World_Happiness_Report_2005-2021.csv')

class DataQuery(Resource):
    def get(self, countryName, startDate, endDate):
 
        query_params = request.args

        mh_filtered = mental_health_data[
            (mental_health_data['Entity'] == countryName) &
            (mental_health_data['Year'].between(int(startDate), int(endDate)))
        ].set_index('Year')

        wh_filtered = world_happiness_data[
            (world_happiness_data['Country name'] == countryName) &
            (world_happiness_data['Year'].between(int(startDate), int(endDate)))
        ].set_index('Year')

        mh_columns = set(query_params.keys()).intersection(mh_filtered.columns)
        wh_columns = set(query_params.keys()).intersection(wh_filtered.columns)
        
        mh_features = mh_filtered[list(mh_columns)]
        wh_features = wh_filtered[list(wh_columns)]

        combined_features = pd.concat([mh_features, wh_features], axis=1, join='inner')

        result_data = {col: combined_features[col].to_dict() for col in combined_features.columns}

        result = {
            'Country': countryName,
            'Start Year': startDate,
            'End Year': endDate,
            'Data': result_data
        }

        return result
