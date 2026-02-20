import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test home page loads"""
    rv = client.get('/')
    assert rv.status_code == 200

def test_health_endpoint(client):
    """Test health check endpoint"""
    rv = client.get('/health')
    assert rv.status_code in [200, 503]
    assert b'status' in rv.data

def test_about_page(client):
    """Test about page loads"""
    rv = client.get('/about')
    assert rv.status_code == 200

def test_predict_empty_message(client):
    """Test prediction with empty message"""
    rv = client.post('/predict', data={'message': ''})
    assert rv.status_code == 400

def test_predict_long_message(client):
    """Test prediction with too long message"""
    rv = client.post('/predict', data={'message': 'a' * 1001})
    assert rv.status_code == 400
