"""Stub metadata extraction service for ingest flows."""

from app.services.ingest_models import (
    MetadataExtractionResult,
    SourceInspectionResult,
)


class MetadataExtractor:
    """Extract minimal metadata from inspected sources."""

    def extract(
        self,
        inspection: SourceInspectionResult,
    ) -> MetadataExtractionResult:
        """Return a minimal metadata result for the inspected source."""
        file_name = inspection.source.rsplit("/", maxsplit=1)[-1]
        return MetadataExtractionResult(
            source=inspection.source,
            source_kind=inspection.source_kind,
            file_name=file_name,
        )
