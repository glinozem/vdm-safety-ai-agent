"""Application-level models for ingest use cases."""

from dataclasses import dataclass
from enum import StrEnum

from app.schemas.documents import DocumentItem, DocumentStatus, DocumentType


class ReplaceStrategy(StrEnum):
    """Supported replace strategies for ingest operations."""

    NEW_VERSIONS_ONLY = "new_versions_only"


class SourceKind(StrEnum):
    """Minimal source classification for ingest inputs."""

    LOCAL_FILE = "local_file"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class IngestCommand:
    """Command object for document ingest operations."""

    source: str
    replace_strategy: ReplaceStrategy = ReplaceStrategy.NEW_VERSIONS_ONLY


@dataclass(frozen=True)
class SourceInspectionResult:
    """Application-level result of source inspection."""

    source: str
    source_kind: SourceKind


@dataclass(frozen=True)
class MetadataExtractionResult:
    """Application-level result of metadata extraction."""

    source: str
    source_kind: SourceKind
    file_name: str


@dataclass(frozen=True)
class DocumentDraft:
    """Application-level draft used before a document item is finalized."""

    code: str
    title: str
    doc_type: DocumentType
    status: DocumentStatus


@dataclass(frozen=True)
class IngestResult:
    """Application-level result for ingest operations."""

    job_id: str
    status: DocumentStatus
    document: DocumentItem
