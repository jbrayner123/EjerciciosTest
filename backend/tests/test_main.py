from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_ok():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello World"}

def test_get_item_ok():
    r = client.get("/items/1")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == 1
    assert data["name"] == "Alpha"

def test_get_item_not_found():
    r = client.get("/items/999")
    assert r.status_code == 404
    assert r.json()["detail"] == "Item not found"

def test_create_item_ok():
    payload = {"id": 3, "name": "Gamma"}
    r = client.post("/items", json=payload)
    assert r.status_code == 201
    assert r.json() == payload

def test_create_item_duplicate():
    payload = {"id": 1, "name": "Dup"}
    r = client.post("/items", json=payload)
    assert r.status_code == 400
    assert r.json()["detail"] == "Item already exists"
