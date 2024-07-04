import pytest
from app import create_app
#Define pytest fixture
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
#tests the data query endpoint
def test_data_query(client):
    # Send a GET reques
    response = client.get('/data/canada/2008/2009?Schizophrenia=true')
    # Assert that the response status code is 200, then get data from response
    assert response.status_code == 200
    data = response.get_json()
    # Assert that the data contains the expected data
    assert 'Country' in data
    assert 'Data' in data
    assert 'Schizophrenia' in data['Data']
