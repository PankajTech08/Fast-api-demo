from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_read_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert "Hello FastAPI Project!" in response.json()["message"]


def test_read_item() -> None:
    response = client.get("/items/7", params={"q": "sample"})

    assert response.status_code == 200
    assert response.json() == {"item_id": 7, "query": "sample"}


def test_create_item() -> None:
    response = client.post("/items/", params={"name": "book", "price": 12.5})

    assert response.status_code == 200
    assert response.json() == {"name": "book", "price": 12.5}


def test_display_fruit() -> None:
    response = client.get("/fruit")

    assert response.status_code == 200
    assert response.json()["name"] == "Apple"


def test_read_user() -> None:
    response = client.get("/users/42")

    assert response.status_code == 200
    assert response.json() == {
        "id": 42,
        "name": "Example User",
        "email": "user@example.com",
    }
