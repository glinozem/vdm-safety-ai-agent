from app.schemas.documents import DocumentIngestRequest
from app.services.document_registry import registry
from app.services.ingest_service import IngestService


def setup_function() -> None:
    registry.reset()


def test_ingest_service_returns_accepted_response_and_registers_document() -> None:
    service = IngestService(registry)

    payload = DocumentIngestRequest(
        source="service-test.pdf",
        replace_strategy="new_versions_only",
    )

    response = service.ingest(payload)

    assert response.status == "accepted"
    assert response.job_id
    assert response.document.title == "Ingested from service-test.pdf"
    assert response.document.doc_type == "stub"
    assert response.document.status == "accepted"

    documents = registry.list_documents()
    assert len(documents) == 1
    assert documents[0].title == "Ingested from service-test.pdf"
