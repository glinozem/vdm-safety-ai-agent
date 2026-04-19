"""Service layer for document ingest flows."""

from uuid import uuid4

from app.schemas.documents import DocumentStatus
from app.services.ingest_models import IngestCommand, IngestResult
from app.services.protocols import DocumentRegistryProtocol


class IngestService:
    """Coordinate ingest operations and response construction."""

    def __init__(self, registry: DocumentRegistryProtocol) -> None:
        """Initialize the service with a document registry collaborator."""
        self._registry = registry

    def ingest(self, command: IngestCommand) -> IngestResult:
        """Process a stub ingest command and return an accepted result."""
        document = self._registry.add_stub_document(
            source=command.source,
            replace_strategy=command.replace_strategy,
        )
        return IngestResult(
            job_id=str(uuid4()),
            status=DocumentStatus.ACCEPTED,
            document=document,
        )
