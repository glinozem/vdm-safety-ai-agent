"""Factory for creating document drafts in ingest flows."""

from app.schemas.documents import DocumentStatus, DocumentType
from app.services.ingest_models import (
    DocumentDraft,
    MetadataExtractionResult,
    ReplaceStrategy,
)


class DocumentFactory:
    """Create document drafts from ingest metadata."""

    def create_stub_document_draft(
        self,
        metadata: MetadataExtractionResult,
        replace_strategy: ReplaceStrategy,
    ) -> DocumentDraft:
        """Create a stub draft for the current ingest prototype."""
        return DocumentDraft(
            code="stub",
            title=f"Ingested from {metadata.source}",
            doc_type=DocumentType.STUB,
            status=DocumentStatus.ACCEPTED,
        )
