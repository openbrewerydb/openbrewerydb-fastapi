from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)

#
# ENDPOINTS
#


@app.get("/")
async def root():
    return {"message": "Hello World"}

#
# TESTS
#


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
