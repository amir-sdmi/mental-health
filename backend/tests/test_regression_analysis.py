import pytest
import pandas as pd
from app.services.regression_analysis import perform_regression

def test_perform_regression():
    data = pd.DataFrame({
        'GDP': [1, 2, 3, 4, 5],
        'Schizophrenia': [2, 3, 4, 5, 6]
    })

    model, coefficients, intercept = perform_regression(data, 'Schizophrenia')

    assert model is not None
    assert len(coefficients) > 0
    assert intercept is not None
