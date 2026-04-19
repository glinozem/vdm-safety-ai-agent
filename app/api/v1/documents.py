from fastapi import APIRouter, status

from app.schemas.documents import (
    DocumentIngestRequest,
    DocumentIngestResponse,
    DocumentListResponse,
)
from app.services.container import container

router = APIRouter()


@router.get("/documents", response_model=DocumentListResponse)
def list_documents() -> DocumentListResponse:
    return container.document_query_service.list_documents()


@router.post(
    "/documents/ingest",
    response_model=DocumentIngestResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
def ingest_document(payload: DocumentIngestRequest) -> DocumentIngestResponse:
    return container.ingest_service.ingest(payload)
