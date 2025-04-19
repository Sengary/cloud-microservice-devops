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

def test_add_get_update_delete_quote():
    # Create
    quote_data = {"author": "DevOps", "content": "Automation is power."}
    post_response = client.post("/quotes", json=quote_data)
    assert post_response.status_code == 200
    quote = post_response.json()
    assert quote["author"] == quote_data["author"]
    assert quote["content"] == quote_data["content"]
    quote_id = quote["id"]

    # Read
    get_response = client.get(f"/quotes/{quote_id}")
    assert get_response.status_code == 200
    assert get_response.json()["id"] == quote_id

    # Update
    updated_data = {"author": "DevOps Engineer", "content": "CI/CD is essential."}
    put_response = client.put(f"/quotes/{quote_id}", json=updated_data)
    assert put_response.status_code == 200
    assert put_response.json()["author"] == "DevOps Engineer"

    # Delete
    delete_response = client.delete(f"/quotes/{quote_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Quote deleted"

    # Confirm deletion
    get_deleted = client.get(f"/quotes/{quote_id}")
    assert get_deleted.status_code == 404
