"""Dependency providers for API routes."""

from app.services.container import container
from app.services.document_query_service import DocumentQueryService
from app.services.ingest_service import IngestService
from app.services.protocols import DocumentRegistryProtocol


def get_document_registry() -> DocumentRegistryProtocol:
    """Return the document registry used by application services."""
    return container.registry


def get_document_query_service() -> DocumentQueryService:
    """Return the document query service used by API routes."""
    return DocumentQueryService(get_document_registry())


def get_ingest_service() -> IngestService:
    """Return the ingest service used by API routes."""
    return IngestService(get_document_registry())
