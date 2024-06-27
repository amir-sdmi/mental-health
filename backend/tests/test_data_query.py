import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_data_query(client):
    response = client.get('/data/canada/2008/2009?Schizophrenia=true')
    assert response.status_code == 200
    data = response.get_json()
    assert 'Country' in data
    assert 'Data' in data
    assert 'Schizophrenia' in data['Data']
