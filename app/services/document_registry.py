"""In-memory document registry for early-stage application flows."""

from uuid import uuid4

from app.schemas.documents import DocumentItem
from app.services.ingest_models import DocumentDraft


class InMemoryDocumentRegistry:
    """Store document items in memory for bootstrap and stub flows."""

    def __init__(self) -> None:
        """Initialize an empty in-memory document collection."""
        self._items: list[DocumentItem] = []

    def list_documents(self) -> list[DocumentItem]:
        """Return a snapshot of currently registered documents."""
        return list(self._items)

    def reset(self) -> None:
        """Clear registry state to keep tests isolated."""
        self._items.clear()

    def add_document(self, document: DocumentItem) -> DocumentItem:
        """Store a prepared document item and return it."""
        self._items.append(document)
        return document

    def build_document_item(self, draft: DocumentDraft) -> DocumentItem:
        """Convert a draft into a stored document item."""
        return DocumentItem(
            id=str(uuid4()),
            code=f"{draft.code}-{len(self._items) + 1:03d}",
            title=draft.title,
            doc_type=draft.doc_type,
            status=draft.status,
        )


registry = InMemoryDocumentRegistry()
