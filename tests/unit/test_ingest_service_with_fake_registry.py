from app.schemas.documents import DocumentIngestRequest, DocumentItem
from app.services.ingest_service import IngestService


class FakeRegistry:
    def __init__(self) -> None:
        self.calls: list[tuple[str, str]] = []

    def add_stub_document(self, source: str, replace_strategy: str) -> DocumentItem:
        self.calls.append((source, replace_strategy))
        return DocumentItem(
            id="fake-id-1",
            code="stub-001",
            title=f"Ingested from {source}",
            doc_type="stub",
            status="accepted",
        )


def test_ingest_service_uses_registry_protocol() -> None:
    registry = FakeRegistry()
    service = IngestService(registry)

    payload = DocumentIngestRequest(
        source="fake-protocol-test.pdf",
        replace_strategy="new_versions_only",
    )

    response = service.ingest(payload)

    assert response.status == "accepted"
    assert response.job_id
    assert response.document.id == "fake-id-1"
    assert response.document.title == "Ingested from fake-protocol-test.pdf"
    assert registry.calls == [("fake-protocol-test.pdf", "new_versions_only")]
