import pytest
import pandas as pd
from app.services.regression_analysis import perform_regression

# Define a test function for the perform_regression function
def test_perform_regression():
    # Create a sample DataFrame
    data = pd.DataFrame({
        'GDP': [1, 2, 3, 4, 5],
        'Schizophrenia': [2, 3, 4, 5, 6]
    })
 # call the perform_regression function with the sample data
    model, coefficients, intercept = perform_regression(data, 'Schizophrenia')

    assert model is not None
    assert len(coefficients) > 0
    assert intercept is not None
