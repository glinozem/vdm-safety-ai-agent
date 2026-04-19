"""In-memory document registry for early-stage application flows."""

from uuid import uuid4

from app.schemas.documents import DocumentItem


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

    def add_stub_document(self, source: str, replace_strategy: str) -> DocumentItem:
        """Register a stub document for the current ingest prototype."""
        document = DocumentItem(
            id=str(uuid4()),
            code=f"stub-{len(self._items) + 1:03d}",
            title=f"Ingested from {source}",
            doc_type="stub",
            status="accepted",
        )
        self._items.append(document)
        return document


registry = InMemoryDocumentRegistry()
