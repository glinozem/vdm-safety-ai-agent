"""Service layer for document ingest flows."""

from uuid import uuid4

from app.schemas.documents import DocumentStatus
from app.services.ingest_models import IngestCommand, IngestResult
from app.services.protocols import (
    DocumentRegistryProtocol,
    MetadataExtractorProtocol,
    SourceInspectorProtocol,
)


class IngestService:
    """Coordinate ingest operations and response construction."""

    def __init__(
        self,
        registry: DocumentRegistryProtocol,
        inspector: SourceInspectorProtocol,
        metadata_extractor: MetadataExtractorProtocol,
    ) -> None:
        """Initialize the service with ingest-related collaborators."""
        self._registry = registry
        self._inspector = inspector
        self._metadata_extractor = metadata_extractor

    def ingest(self, command: IngestCommand) -> IngestResult:
        """Process a stub ingest command and return an accepted result."""
        inspection = self._inspector.inspect(command.source)
        metadata = self._metadata_extractor.extract(inspection)

        document = self._registry.add_stub_document(
            source=metadata.source,
            replace_strategy=command.replace_strategy,
        )
        return IngestResult(
            job_id=str(uuid4()),
            status=DocumentStatus.ACCEPTED,
            document=document,
        )
