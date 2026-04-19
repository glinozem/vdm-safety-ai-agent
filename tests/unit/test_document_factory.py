from app.schemas.documents import DocumentStatus, DocumentType
from app.services.document_factory import DocumentFactory
from app.services.ingest_models import (
    MetadataExtractionResult,
    ReplaceStrategy,
    SourceKind,
)


def test_document_factory_creates_stub_document_draft() -> None:
    factory = DocumentFactory()

    draft = factory.create_stub_document_draft(
        MetadataExtractionResult(
            source="docs/manual.pdf",
            source_kind=SourceKind.LOCAL_FILE,
            file_name="manual.pdf",
        ),
        ReplaceStrategy.NEW_VERSIONS_ONLY,
    )

    assert draft.code == "stub"
    assert draft.title == "Ingested from docs/manual.pdf"
    assert draft.doc_type == DocumentType.STUB
    assert draft.status == DocumentStatus.ACCEPTED
