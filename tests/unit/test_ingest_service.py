from app.services.document_registry import registry
from app.services.ingest_models import IngestCommand
from app.services.ingest_service import IngestService


def setup_function() -> None:
    registry.reset()


def test_ingest_service_returns_accepted_response_and_registers_document() -> None:
    service = IngestService(registry)

    command = IngestCommand(
        source="service-test.pdf",
        replace_strategy="new_versions_only",
    )

    response = service.ingest(command)

    assert response.status.value == "accepted"
    assert response.job_id
    assert response.document.title == "Ingested from service-test.pdf"
    assert response.document.doc_type.value == "stub"
    assert response.document.status.value == "accepted"

    documents = registry.list_documents()
    assert len(documents) == 1
    assert documents[0].title == "Ingested from service-test.pdf"
