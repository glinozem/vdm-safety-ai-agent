from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.dependencies import (
    get_document_query_service,
    get_ingest_service,
)
from app.schemas.documents import (
    DocumentIngestRequest,
    DocumentIngestResponse,
    DocumentListResponse,
)
from app.services.document_query_service import DocumentQueryService
from app.services.ingest_models import IngestCommand
from app.services.ingest_service import IngestService

router = APIRouter()


@router.get("/documents", response_model=DocumentListResponse)
def list_documents(
    service: Annotated[DocumentQueryService, Depends(get_document_query_service)],
) -> DocumentListResponse:
    return service.list_documents()


@router.post(
    "/documents/ingest",
    response_model=DocumentIngestResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
def ingest_document(
    payload: DocumentIngestRequest,
    service: Annotated[IngestService, Depends(get_ingest_service)],
) -> DocumentIngestResponse:
    command = IngestCommand(
        source=payload.source,
        replace_strategy=payload.replace_strategy,
    )
    result = service.ingest(command)
    return DocumentIngestResponse(
        job_id=result.job_id,
        status=result.status,
        document=result.document,
    )
