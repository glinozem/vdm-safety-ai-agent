"""Dependency providers for API routes."""

from app.services.container import container
from app.services.document_query_service import DocumentQueryService
from app.services.ingest_service import IngestService
from app.services.protocols import (
    DocumentFactoryProtocol,
    DocumentRegistryProtocol,
    MetadataExtractorProtocol,
    SourceInspectorProtocol,
)


def get_document_registry() -> DocumentRegistryProtocol:
    """Return the document registry used by application services."""
    return container.registry


def get_source_inspector() -> SourceInspectorProtocol:
    """Return the source inspector used by ingest services."""
    return container.source_inspector


def get_metadata_extractor() -> MetadataExtractorProtocol:
    """Return the metadata extractor used by ingest services."""
    return container.metadata_extractor


def get_document_factory() -> DocumentFactoryProtocol:
    """Return the document factory used by ingest services."""
    return container.document_factory


def get_document_query_service() -> DocumentQueryService:
    """Return the document query service used by API routes."""
    return DocumentQueryService(get_document_registry())


def get_ingest_service() -> IngestService:
    """Return the ingest service used by API routes."""
    return IngestService(
        get_document_registry(),
        get_source_inspector(),
        get_metadata_extractor(),
        get_document_factory(),
    )
