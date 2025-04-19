from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Quote Manager API"}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_post_and_get_quote():
    data = {"author": "Test", "content": "Test quote"}
    post_response = client.post("/quotes", json=data)
    assert post_response.status_code == 200
    assert post_response.json()["message"] == "Quote added successfully."

    get_response = client.get("/quotes")
    assert get_response.status_code == 200
    assert any(q["content"] == "Test quote" for q in get_response.json())
