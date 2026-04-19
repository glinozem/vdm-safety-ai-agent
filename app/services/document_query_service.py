"""Service layer for document query flows."""

from app.schemas.documents import DocumentListResponse
from app.services.protocols import DocumentRegistryProtocol


class DocumentQueryService:
    """Coordinate document read operations."""

    def __init__(self, registry: DocumentRegistryProtocol) -> None:
        """Initialize the service with a document registry collaborator."""
        self._registry = registry

    def list_documents(self) -> DocumentListResponse:
        """Return a typed response with all currently registered documents."""
        return DocumentListResponse(items=self._registry.list_documents())
