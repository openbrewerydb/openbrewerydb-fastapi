from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_v1_root():
    response = client.get("/v1")
    assert response.status_code == 200
    assert response.json() == {"version": 1}
