"""Service layer for document ingest flows."""

from uuid import uuid4

from app.schemas.documents import (
    DocumentIngestRequest,
    DocumentIngestResponse,
)
from app.services.document_registry import registry


class IngestService:
    """Coordinate ingest operations and response construction."""

    def ingest(self, payload: DocumentIngestRequest) -> DocumentIngestResponse:
        """Process a stub ingest request and return an accepted response."""
        document = registry.add_stub_document(
            source=payload.source,
            replace_strategy=payload.replace_strategy,
        )
        return DocumentIngestResponse(
            job_id=str(uuid4()),
            status="accepted",
            document=document,
        )


ingest_service = IngestService()
