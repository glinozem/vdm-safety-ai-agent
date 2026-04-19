"""Protocols for service-layer collaborators."""

from typing import Protocol

from app.schemas.documents import DocumentItem


class DocumentRegistryProtocol(Protocol):
    """Minimal protocol required by document-related services."""

    def list_documents(self) -> list[DocumentItem]:
        """Return currently registered documents."""

    def add_stub_document(self, source: str, replace_strategy: str) -> DocumentItem:
        """Register a stub document and return the created item."""
