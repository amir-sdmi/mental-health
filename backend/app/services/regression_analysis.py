import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# performs linear regression analysis on the data to find the relationship between GDP and other features.
def perform_regression(data, target_column, gdp_column='GDP'):
    # Check if the data has at least 2 rows
    if len(data) < 2:
        return None, [0], 0
# Drop rows with missing values in the GDP and target columns
    data = data.dropna(subset=[gdp_column, target_column])
# Check again if the data has at least 2 rows after dropping missing values
    if len(data) < 2:
        return None, [0], 0
# Create a linear regression model
    model = LinearRegression()
    X = data[[gdp_column]]
    y = data[target_column]
    # Train the model
    model.fit(X, y)
    # Get the coefficients and intercept of the model
    coefficients = model.coef_
    intercept = model.intercept_
    
    return model, coefficients, intercept
