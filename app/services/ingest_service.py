"""Service layer for document ingest flows."""

from uuid import uuid4

from app.schemas.documents import DocumentStatus
from app.services.ingest_models import IngestCommand, IngestResult
from app.services.protocols import (
    DocumentRegistryProtocol,
    SourceInspectorProtocol,
)


class IngestService:
    """Coordinate ingest operations and response construction."""

    def __init__(
        self,
        registry: DocumentRegistryProtocol,
        inspector: SourceInspectorProtocol,
    ) -> None:
        """Initialize the service with registry and source inspector collaborators."""
        self._registry = registry
        self._inspector = inspector

    def ingest(self, command: IngestCommand) -> IngestResult:
        """Process a stub ingest command and return an accepted result."""
        inspection = self._inspector.inspect(command.source)
        document = self._registry.add_stub_document(
            source=inspection.source,
            replace_strategy=command.replace_strategy,
        )
        return IngestResult(
            job_id=str(uuid4()),
            status=DocumentStatus.ACCEPTED,
            document=document,
        )
