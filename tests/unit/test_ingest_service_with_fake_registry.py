from app.schemas.documents import DocumentItem, DocumentStatus, DocumentType
from app.services.ingest_models import (
    IngestCommand,
    MetadataExtractionResult,
    ReplaceStrategy,
    SourceInspectionResult,
    SourceKind,
)
from app.services.ingest_service import IngestService


class FakeRegistry:
    def __init__(self) -> None:
        self.calls: list[tuple[str, ReplaceStrategy]] = []

    def add_stub_document(
        self,
        source: str,
        replace_strategy: ReplaceStrategy,
    ) -> DocumentItem:
        self.calls.append((source, replace_strategy))
        return DocumentItem(
            id="fake-id-1",
            code="stub-001",
            title=f"Ingested from {source}",
            doc_type=DocumentType.STUB,
            status=DocumentStatus.ACCEPTED,
        )


class FakeInspector:
    def inspect(self, source: str) -> SourceInspectionResult:
        return SourceInspectionResult(
            source=source,
            source_kind=SourceKind.LOCAL_FILE,
        )


class FakeMetadataExtractor:
    def extract(
        self,
        inspection: SourceInspectionResult,
    ) -> MetadataExtractionResult:
        return MetadataExtractionResult(
            source=inspection.source,
            source_kind=inspection.source_kind,
            file_name="fake-protocol-test.pdf",
        )


def test_ingest_service_uses_registry_protocol() -> None:
    registry = FakeRegistry()
    inspector = FakeInspector()
    metadata_extractor = FakeMetadataExtractor()
    service = IngestService(registry, inspector, metadata_extractor)

    command = IngestCommand(
        source="fake-protocol-test.pdf",
        replace_strategy=ReplaceStrategy.NEW_VERSIONS_ONLY,
    )

    response = service.ingest(command)

    assert response.status == DocumentStatus.ACCEPTED
    assert response.job_id
    assert response.document.id == "fake-id-1"
    assert response.document.title == "Ingested from fake-protocol-test.pdf"
    assert response.document.doc_type == DocumentType.STUB
    assert response.document.status == DocumentStatus.ACCEPTED
    assert registry.calls == [
        ("fake-protocol-test.pdf", ReplaceStrategy.NEW_VERSIONS_ONLY)
    ]
