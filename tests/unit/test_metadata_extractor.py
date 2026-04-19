from app.services.ingest_models import SourceInspectionResult, SourceKind
from app.services.metadata_extractor import MetadataExtractor


def test_metadata_extractor_returns_file_name_from_source() -> None:
    extractor = MetadataExtractor()

    result = extractor.extract(
        SourceInspectionResult(
            source="docs/manual.pdf",
            source_kind=SourceKind.LOCAL_FILE,
        )
    )

    assert result.source == "docs/manual.pdf"
    assert result.source_kind == SourceKind.LOCAL_FILE
    assert result.file_name == "manual.pdf"
