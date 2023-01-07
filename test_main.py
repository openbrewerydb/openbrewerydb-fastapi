from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_healthcheck():
    response = client.get("/v1/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
