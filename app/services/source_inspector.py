"""Stub source inspection service for ingest flows."""

from app.services.ingest_models import SourceInspectionResult, SourceKind


class SourceInspector:
    """Classify sources in a minimal, stub-friendly way."""

    def inspect(self, source: str) -> SourceInspectionResult:
        """Inspect a source string and return a minimal classification."""
        if source.lower().endswith(".pdf"):
            return SourceInspectionResult(
                source=source,
                source_kind=SourceKind.LOCAL_FILE,
            )
        return SourceInspectionResult(
            source=source,
            source_kind=SourceKind.UNKNOWN,
        )
