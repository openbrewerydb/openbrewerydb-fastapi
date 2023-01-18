"""
Python main module testing definitions
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_breweries():
    response = client.get("/breweries")
    assert response.status_code == 200
    assert response.json() == {"endpoint": "breweries"}
