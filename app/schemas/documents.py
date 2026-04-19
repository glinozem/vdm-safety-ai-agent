from enum import StrEnum

from pydantic import BaseModel, Field


class DocumentType(StrEnum):
    STUB = "stub"
    INSTRUCTION = "instruction"


class DocumentStatus(StrEnum):
    ACCEPTED = "accepted"
    ACTIVE = "active"


class DocumentItem(BaseModel):
    id: str
    code: str
    title: str
    doc_type: DocumentType
    status: DocumentStatus


class DocumentListResponse(BaseModel):
    items: list[DocumentItem] = Field(default_factory=list)


class DocumentIngestRequest(BaseModel):
    source: str
    replace_strategy: str = "new_versions_only"


class DocumentIngestResponse(BaseModel):
    job_id: str
    status: DocumentStatus
    document: DocumentItem
