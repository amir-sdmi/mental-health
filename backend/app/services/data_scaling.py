
import pandas as pd

# Calculate percentage change in a column
def calculate_percentage_change(data, column):
    # Calculate percentage change for column
    data[column] = data[column].pct_change() * 100
    return data

#filter and prepare data based on query parameters
def filter_and_prepare_data(query_params, mh_filtered, wh_filtered, gdp_filtered):
    # calculate percentage change in GDP column
    if 'GDP' in query_params:
        gdp_filtered = calculate_percentage_change(gdp_filtered, 'GDP')

    # Find common columns between query parameters and filtered data
    mh_columns = set(query_params.keys()).intersection(mh_filtered.columns)
    wh_columns = set(query_params.keys()).intersection(wh_filtered.columns)
    gdp_column = 'GDP' if 'GDP' in query_params else None

    # Select relevant columns from filtered data
    mh_features = mh_filtered[list(mh_columns)] if mh_columns else pd.DataFrame()
    wh_features = wh_filtered[list(wh_columns)] if wh_columns else pd.DataFrame()
    gdp_features = gdp_filtered[[gdp_column]] if gdp_column else pd.DataFrame()

    return mh_features, wh_features, gdp_features, mh_columns, wh_columns, gdp_column

# Combine features 
def combine_features(mh_features, wh_features, gdp_features, start_year, end_year):

    all_years = pd.DataFrame(index=pd.RangeIndex(start_year, end_year + 1))

    # Join features with all years and fill missing values so we can have an average data for missing columns which
    # allows us to do regression analysis
    mh_features = all_years.join(mh_features, how='left').ffill()
    wh_features = all_years.join(wh_features, how='left').ffill()
    gdp_features = all_years.join(gdp_features, how='left').ffill()

    # Concat features 
    combined_features = pd.concat([mh_features, wh_features, gdp_features], axis=1)

    # Fill missing values with mean of each column
    combined_features = combined_features.apply(lambda x: x.fillna(x.mean()), axis=0)

    # Return combined features
    return combined_features