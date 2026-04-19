from app.api.dependencies import (
    get_document_query_service,
    get_document_registry,
    get_ingest_service,
)
from app.services.container import container
from app.services.document_query_service import DocumentQueryService
from app.services.ingest_service import IngestService


def test_get_document_registry_returns_container_registry() -> None:
    registry = get_document_registry()

    assert registry is container.registry


def test_get_document_query_service_returns_query_service() -> None:
    service = get_document_query_service()

    assert isinstance(service, DocumentQueryService)


def test_get_ingest_service_returns_ingest_service() -> None:
    service = get_ingest_service()

    assert isinstance(service, IngestService)
