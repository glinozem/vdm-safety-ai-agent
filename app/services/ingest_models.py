"""Application-level models for ingest use cases."""

from dataclasses import dataclass

from app.schemas.documents import DocumentItem, DocumentStatus


@dataclass(frozen=True)
class IngestCommand:
    """Command object for document ingest operations."""

    source: str
    replace_strategy: str = "new_versions_only"


@dataclass(frozen=True)
class IngestResult:
    """Application-level result for ingest operations."""

    job_id: str
    status: DocumentStatus
    document: DocumentItem
