import pandas as pd

def calculate_percentage_change(data, column):
    data[column] = data[column].pct_change() * 100
    return data

def filter_and_prepare_data(query_params, mh_filtered, wh_filtered, gdp_filtered):
    if 'GDP' in query_params:
        gdp_filtered = calculate_percentage_change(gdp_filtered, 'GDP')

    mh_columns = set(query_params.keys()).intersection(mh_filtered.columns)
    wh_columns = set(query_params.keys()).intersection(wh_filtered.columns)
    gdp_column = 'GDP' if 'GDP' in query_params else None

    mh_features = mh_filtered[list(mh_columns)] if mh_columns else pd.DataFrame()
    wh_features = wh_filtered[list(wh_columns)] if wh_columns else pd.DataFrame()
    gdp_features = gdp_filtered[[gdp_column]] if gdp_column else pd.DataFrame()

    return mh_features, wh_features, gdp_features, mh_columns, wh_columns, gdp_column

def combine_features(mh_features, wh_features, gdp_features, start_year, end_year):
    # Create a DataFrame with all years and fill missing values with column mean
    all_years = pd.DataFrame(index=pd.RangeIndex(start_year, end_year + 1))
    mh_features = all_years.join(mh_features, how='left').fillna(method='ffill')
    wh_features = all_years.join(wh_features, how='left').fillna(method='ffill')
    gdp_features = all_years.join(gdp_features, how='left').fillna(method='ffill')

    combined_features = pd.concat([mh_features, wh_features, gdp_features], axis=1)

    # Fill NaN values with column mean
    combined_features = combined_features.apply(lambda x: x.fillna(x.mean()), axis=0)

    return combined_features
