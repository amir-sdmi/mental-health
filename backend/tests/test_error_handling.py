import pytest
from app import create_app

# Define a pytest fixture
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
# Test function to test invalid year range
def test_invalid_year_range(client):
    response = client.get('/data/canada/2011/2008?Schizophrenia=true')
    assert response.status_code == 400
    data = response.get_json()
    assert 'message' in data
    assert data['message'] == 'Invalid year range: startDate should be less than endDate'
# Define a test function to test year ranges out of bound
def test_year_out_of_range(client):
    response = client.get('/data/canada/2003/2004?Schizophrenia=true')
    assert response.status_code == 400
    data = response.get_json()
    assert 'message' in data
    assert data['message'] == 'Invalid year range: Data is available only between 2005 and 2017'
# Define a test function to test invalid query parameters
def test_invalid_query_param(client):
    response = client.get('/data/canada/2008/2009?InvalidParam=true')
    assert response.status_code == 400
    data = response.get_json()
    assert 'message' in data
    assert data['message'] == 'Invalid query parameter: InvalidParam'
