from pydantic import BaseModel, Field


class DocumentItem(BaseModel):
    id: str
    code: str
    title: str
    doc_type: str
    status: str


class DocumentListResponse(BaseModel):
    items: list[DocumentItem] = Field(default_factory=list)


class DocumentIngestRequest(BaseModel):
    source: str
    replace_strategy: str = "new_versions_only"


class DocumentIngestResponse(BaseModel):
    job_id: str
    status: str
    document: DocumentItem
