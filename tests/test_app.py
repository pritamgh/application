import pytest
from src.app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    """Test the hello_world route."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Testing after 2 months, Date: 09-04-2025"
