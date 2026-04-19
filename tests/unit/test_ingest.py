from fastapi.testclient import TestClient

from app.api.main import app
from app.services.document_registry import registry

client = TestClient(app)


def setup_function() -> None:
    registry.reset()


def test_ingest_endpoint_accepts_stub_document() -> None:
    response = client.post(
        "/api/v1/documents/ingest",
        json={
            "source": "sample.pdf",
            "replace_strategy": "new_versions_only",
        },
    )

    assert response.status_code == 202

    payload = response.json()
    assert payload["status"] == "accepted"
    assert payload["job_id"]
    assert payload["document"]["title"] == "Ingested from sample.pdf"
    assert payload["document"]["doc_type"] == "stub"
    assert payload["document"]["status"] == "accepted"


def test_documents_endpoint_returns_item_after_ingest() -> None:
    ingest_response = client.post(
        "/api/v1/documents/ingest",
        json={
            "source": "sample.pdf",
            "replace_strategy": "new_versions_only",
        },
    )
    assert ingest_response.status_code == 202

    list_response = client.get("/api/v1/documents")

    assert list_response.status_code == 200
    payload = list_response.json()
    assert len(payload["items"]) == 1
    assert payload["items"][0]["title"] == "Ingested from sample.pdf"
