import pytest
from flask import Flask
from app.validation.validation import validate_year_range, validate_country_exists, validate_query_params

app = Flask(__name__)
#Test function for the validate_year_range
def test_validate_year_range():
    with app.test_request_context():
        with pytest.raises(Exception) as e:
            validate_year_range(2011, 2008)
        assert e.type.code == 400

        with pytest.raises(Exception) as e:
            validate_year_range(2003, 2004)
        assert e.type.code == 400
# Test function for the validate_country_exists
def test_validate_country_exists():
    available_countries = ['Afghanistan', 'Canada']
    with app.test_request_context():
        with pytest.raises(Exception) as e:
            validate_country_exists('UnknownCountry', available_countries)
        assert e.type.code == 404
# Test function for the validate_query_params
def test_validate_query_params():
    valid_params = {'Schizophrenia', 'Life-Ladder', 'GDP'}
    with app.test_request_context():
        with pytest.raises(Exception) as e:
            validate_query_params({'InvalidParam': 'true'}, valid_params)
        assert e.type.code == 400
