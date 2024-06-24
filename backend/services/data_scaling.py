

# import pandas as pd
# import numpy as np

# # historical min and max values
# def compute_global_min_max(dataframes, exclude_columns=['Year', 'Country name', 'Entity']):
#     global_min = {}
#     global_max = {}
#     for df in dataframes:
#         for column in df.columns:
#             if column not in exclude_columns:
#                 min_val = df[column].min()
#                 max_val = df[column].max()
#                 if column in global_min:
#                     global_min[column] = min(global_min[column], min_val)
#                     global_max[column] = max(global_max[column], max_val)
#                 else:
#                     global_min[column] = min_val
#                     global_max[column] = max_val
#     return global_min, global_max

# mental_health_data = pd.read_csv('assets/Cleaned_Mental_Health_Data.csv')
# world_happiness_data = pd.read_csv('assets/Cleaned_World_Happiness_Report_2005-2021.csv')
# global_min, global_max = compute_global_min_max([mental_health_data, world_happiness_data])

# def scale_data_with_global_min_max(data, global_min, global_max):

#     data = data.ffill().bfill()
#     scaled_data = pd.DataFrame(index=data.index)

#     for column in data.columns:
#         if column in global_min and column in global_max:
#             min_val = global_min[column]
#             max_val = global_max[column]
#             scaled_data[column] = (data[column] - min_val) / (max_val - min_val)
#         else:
#             scaled_data[column] = data[column]  # Non-numeric data remains unchanged
#     return scaled_data
