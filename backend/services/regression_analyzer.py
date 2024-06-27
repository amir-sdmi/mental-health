import pandas as pd
from sklearn.linear_model import LinearRegression

def perform_regression(data, target_column, gdp_column='GDP'):
    if len(data) < 2:
        # Not enough data points for regression
        return None, [0], 0

    model = LinearRegression()
    X = data[[gdp_column]]
    y = data[target_column]
    
    model.fit(X, y)
    coefficients = model.coef_
    intercept = model.intercept_
    
    return model, coefficients, intercept
