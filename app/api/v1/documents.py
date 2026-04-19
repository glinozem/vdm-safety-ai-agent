from fastapi import APIRouter, status

from app.schemas.documents import (
    DocumentIngestRequest,
    DocumentIngestResponse,
    DocumentListResponse,
)
from app.services.document_registry import registry
from app.services.ingest_service import ingest_service

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
    return ingest_service.ingest(payload)
