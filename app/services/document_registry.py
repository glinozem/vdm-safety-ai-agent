from app.schemas.documents import DocumentItem


class InMemoryDocumentRegistry:
    def __init__(self) -> None:
        self._items: list[DocumentItem] = []

    def list_documents(self) -> list[DocumentItem]:
        return list(self._items)


registry = InMemoryDocumentRegistry()
