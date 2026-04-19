"""Dependency providers for API routes."""

from app.services.container import container
from app.services.document_query_service import DocumentQueryService
from app.services.ingest_service import IngestService


def get_document_query_service() -> DocumentQueryService:
    """Return the document query service used by API routes."""
    return container.document_query_service


def get_ingest_service() -> IngestService:
    """Return the ingest service used by API routes."""
    return container.ingest_service
