from app.schemas.documents import DocumentItem, DocumentStatus, DocumentType
from app.services.ingest_models import (
    DocumentDraft,
    IngestCommand,
    MetadataExtractionResult,
    ReplaceStrategy,
    SourceInspectionResult,
    SourceKind,
)
from app.services.ingest_service import IngestService


class FakeRegistry:
    def __init__(self) -> None:
        self.calls: list[DocumentItem] = []

    def add_document(self, document: DocumentItem) -> DocumentItem:
        self.calls.append(document)
        return document

    def build_document_item(self, draft: DocumentDraft) -> DocumentItem:
        return DocumentItem(
            id="fake-id-1",
            code="stub-001",
            title=draft.title,
            doc_type=draft.doc_type,
            status=draft.status,
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


class FakeDocumentFactory:
    def create_stub_document_draft(
        self,
        metadata: MetadataExtractionResult,
        replace_strategy: ReplaceStrategy,
    ) -> DocumentDraft:
        return DocumentDraft(
            code="stub",
            title=f"Ingested from {metadata.source}",
            doc_type=DocumentType.STUB,
            status=DocumentStatus.ACCEPTED,
        )


def test_ingest_service_uses_registry_protocol() -> None:
    registry = FakeRegistry()
    inspector = FakeInspector()
    metadata_extractor = FakeMetadataExtractor()
    document_factory = FakeDocumentFactory()
    service = IngestService(
        registry,
        inspector,
        metadata_extractor,
        document_factory,
    )

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
    assert len(registry.calls) == 1
    assert registry.calls[0].title == "Ingested from fake-protocol-test.pdf"
