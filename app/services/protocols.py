"""Protocols for service-layer collaborators."""

from typing import Protocol

from app.schemas.documents import DocumentItem
from app.services.ingest_models import (
    DocumentDraft,
    MetadataExtractionResult,
    ReplaceStrategy,
    SourceInspectionResult,
)


class DocumentRegistryProtocol(Protocol):
    """Minimal protocol required by document-related services."""

    def list_documents(self) -> list[DocumentItem]:
        """Return currently registered documents."""

    def add_document(self, document: DocumentItem) -> DocumentItem:
        """Store a prepared document item and return it."""


class SourceInspectorProtocol(Protocol):
    """Minimal protocol required by ingest-related services."""

    def inspect(self, source: str) -> SourceInspectionResult:
        """Inspect a source string and return minimal source metadata."""


class MetadataExtractorProtocol(Protocol):
    """Minimal protocol required by ingest-related services."""

    def extract(
        self,
        inspection: SourceInspectionResult,
    ) -> MetadataExtractionResult:
        """Extract minimal metadata from a source inspection result."""


class DocumentFactoryProtocol(Protocol):
    """Minimal protocol required by ingest-related services."""

    def create_stub_document_draft(
        self,
        metadata: MetadataExtractionResult,
        replace_strategy: ReplaceStrategy,
    ) -> DocumentDraft:
        """Create a document draft from extracted metadata."""
