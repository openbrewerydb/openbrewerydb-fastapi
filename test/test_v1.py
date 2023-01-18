"""
API v1 testing Python definitions
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_v1_root():
    response = client.get("/v1")
    assert response.status_code == 200
    assert response.json() == {"version": 1}

def test_breweries():
    response = client.get("/v1/breweries")
    assert response.status_code == 200
    assert response.json() == {"endpoint": "breweries"}
