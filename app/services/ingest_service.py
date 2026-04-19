from uuid import uuid4

from app.schemas.documents import (
    DocumentIngestRequest,
    DocumentIngestResponse,
)
from app.services.document_registry import registry


class IngestService:
    def ingest(self, payload: DocumentIngestRequest) -> DocumentIngestResponse:
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
