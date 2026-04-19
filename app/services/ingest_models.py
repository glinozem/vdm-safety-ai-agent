"""Application-level models for ingest use cases."""

from dataclasses import dataclass
from enum import StrEnum

from app.schemas.documents import DocumentItem, DocumentStatus


class ReplaceStrategy(StrEnum):
    """Supported replace strategies for ingest operations."""

    NEW_VERSIONS_ONLY = "new_versions_only"


@dataclass(frozen=True)
class IngestCommand:
    """Command object for document ingest operations."""

    source: str
    replace_strategy: ReplaceStrategy = ReplaceStrategy.NEW_VERSIONS_ONLY


@dataclass(frozen=True)
class IngestResult:
    """Application-level result for ingest operations."""

    job_id: str
    status: DocumentStatus
    document: DocumentItem
