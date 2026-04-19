from app.schemas.documents import DocumentItem, DocumentStatus, DocumentType
from app.services.document_query_service import DocumentQueryService


class FakeRegistry:
    def list_documents(self) -> list[DocumentItem]:
        return [
            DocumentItem(
                id="doc-1",
                code="IOT-001",
                title="Sample instruction",
                doc_type=DocumentType.INSTRUCTION,
                status=DocumentStatus.ACTIVE,
            )
        ]

    def add_stub_document(self, source: str, replace_strategy: str) -> DocumentItem:
        raise NotImplementedError


def test_document_query_service_returns_typed_document_list() -> None:
    service = DocumentQueryService(FakeRegistry())

    response = service.list_documents()

    assert len(response.items) == 1
    assert response.items[0].id == "doc-1"
    assert response.items[0].code == "IOT-001"
    assert response.items[0].title == "Sample instruction"
    assert response.items[0].doc_type == DocumentType.INSTRUCTION
    assert response.items[0].status == DocumentStatus.ACTIVE
