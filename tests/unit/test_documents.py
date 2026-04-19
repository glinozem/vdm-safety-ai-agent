from fastapi.testclient import TestClient

from app.api.main import app

client = TestClient(app)


def test_documents_endpoint_returns_empty_list() -> None:
    response = client.get("/api/v1/documents")

    assert response.status_code == 200
    assert response.json() == {"items": []}
