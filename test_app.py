import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test that the homepage loads and says NatWest"""
    response = client.get('/')
    assert response.status_code == 200
    # We check if the word "NatWest" is in the response
    assert b"NatWest" in response.data