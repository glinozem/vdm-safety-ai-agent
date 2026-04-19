from fastapi import APIRouter

from app.schemas.documents import DocumentListResponse
from app.services.document_registry import registry

router = APIRouter()


@router.get("/documents", response_model=DocumentListResponse)
def list_documents() -> DocumentListResponse:
    return DocumentListResponse(items=registry.list_documents())
