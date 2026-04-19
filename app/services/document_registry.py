from uuid import uuid4

from app.schemas.documents import DocumentItem


class InMemoryDocumentRegistry:
    def __init__(self) -> None:
        self._items: list[DocumentItem] = []

    def list_documents(self) -> list[DocumentItem]:
        return list(self._items)

    def reset(self) -> None:
        self._items.clear()

    def add_stub_document(self, source: str, replace_strategy: str) -> DocumentItem:
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
