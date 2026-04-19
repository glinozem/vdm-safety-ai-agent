"""Dependency container for service-layer objects."""

from app.services.document_factory import DocumentFactory
from app.services.document_query_service import DocumentQueryService
from app.services.document_registry import registry
from app.services.ingest_service import IngestService
from app.services.metadata_extractor import MetadataExtractor
from app.services.source_inspector import SourceInspector


class ServiceContainer:
    """Create and expose application service instances."""

    def __init__(self) -> None:
        """Initialize service instances with shared collaborators."""
        self.registry = registry
        self.source_inspector = SourceInspector()
        self.metadata_extractor = MetadataExtractor()
        self.document_factory = DocumentFactory()
        self.document_query_service = DocumentQueryService(self.registry)
        self.ingest_service = IngestService(
            self.registry,
            self.source_inspector,
            self.metadata_extractor,
            self.document_factory,
        )


container = ServiceContainer()
