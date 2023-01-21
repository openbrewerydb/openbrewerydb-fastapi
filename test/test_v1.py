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


def test_breweries_meta():
    response = client.get("/v1/breweries/meta")
    assert response.status_code == 200
    assert response.json() == {"endpoint": "metadata"}


def test_breweries_delete_id():
    response = client.delete("/v1/breweries/1")
    assert response.status_code == 501
    assert response.json() == {"endpoint": "delete_brewery_by_id"}


def test_post_breweries():
    response = client.post("/v1/breweries")
    assert response.status_code == 201
    assert response.json() == {"endpoint": "post_breweries"}


def test_get_brewery_by_id():
    response = client.get("/v1/breweries/1")
    assert response.status_code == 200
    assert response.json() == {"endpoint": "get_brewery_by_id"}


def test_get_random_brewery():
    response = client.get("/v1/breweries/random")
    assert response.status_code == 200
    assert response.json() == {"endpoint": "get_random_brewery"}


def test_get_all_breweries():
    response = client.get("/v1/breweries")
    assert response.status_code == 200
    assert response.json() == {"endpoint": "get_all_breweries"}
