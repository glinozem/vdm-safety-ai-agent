from uuid import uuid4

from fastapi import APIRouter, status

from app.schemas.documents import (
    DocumentIngestRequest,
    DocumentIngestResponse,
    DocumentListResponse,
)
from app.services.document_registry import registry

router = APIRouter()


@router.get("/documents", response_model=DocumentListResponse)
def list_documents() -> DocumentListResponse:
    return DocumentListResponse(items=registry.list_documents())


@router.post(
    "/documents/ingest",
    response_model=DocumentIngestResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
def ingest_document(payload: DocumentIngestRequest) -> DocumentIngestResponse:
    document = registry.add_stub_document(
        source=payload.source,
        replace_strategy=payload.replace_strategy,
    )
    return DocumentIngestResponse(
        job_id=str(uuid4()),
        status="accepted",
        document=document,
    )
