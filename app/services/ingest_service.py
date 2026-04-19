"""Service layer for document ingest flows."""

from uuid import uuid4

from app.schemas.documents import DocumentItem, DocumentStatus
from app.services.ingest_models import IngestCommand, IngestResult
from app.services.protocols import (
    DocumentFactoryProtocol,
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
        document_factory: DocumentFactoryProtocol,
    ) -> None:
        """Initialize the service with ingest-related collaborators."""
        self._registry = registry
        self._inspector = inspector
        self._metadata_extractor = metadata_extractor
        self._document_factory = document_factory

    def _materialize_document(self, draft) -> DocumentItem:
        """Materialize a stored document item from a draft."""
        if hasattr(self._registry, "build_document_item"):
            return self._registry.build_document_item(draft)
        raise AttributeError("Registry does not support draft materialization")

    def ingest(self, command: IngestCommand) -> IngestResult:
        """Process a stub ingest command and return an accepted result."""
        inspection = self._inspector.inspect(command.source)
        metadata = self._metadata_extractor.extract(inspection)
        draft = self._document_factory.create_stub_document_draft(
            metadata,
            command.replace_strategy,
        )
        document = self._materialize_document(draft)
        stored_document = self._registry.add_document(document)

        return IngestResult(
            job_id=str(uuid4()),
            status=DocumentStatus.ACCEPTED,
            document=stored_document,
        )
