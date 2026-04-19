from app.services.ingest_models import SourceKind
from app.services.source_inspector import SourceInspector


def test_source_inspector_classifies_pdf_as_local_file() -> None:
    inspector = SourceInspector()

    result = inspector.inspect("manual.pdf")

    assert result.source == "manual.pdf"
    assert result.source_kind == SourceKind.LOCAL_FILE
