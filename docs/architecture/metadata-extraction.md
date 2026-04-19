# Metadata Extraction: vdm-safety-ai-agent

## Purpose

This document describes the current metadata extraction layer in the application.

The goal of metadata extraction is to derive structured metadata from an already inspected source before the system grows into a fuller ingestion pipeline.

---

## 1. Why metadata extraction exists

Metadata extraction exists to keep metadata-related logic out of:
- API route handlers
- registry implementations
- generic ingest orchestration

It provides a dedicated collaborator responsible for producing structured metadata that later pipeline stages can consume.

---

## 2. Current implemented concepts

### 2.1. MetadataExtractionResult

Current fields:
- `source`
- `source_kind`
- `file_name`

Role:
- represent the application-level outcome of metadata extraction
- carry structured metadata forward in the ingest flow

---

## 3. Current implemented collaborator

### `MetadataExtractor`

Role:
- accept `SourceInspectionResult`
- return `MetadataExtractionResult`

Current stub behavior:
- derive `file_name` from the source path by taking the last path segment
- preserve `source`
- preserve `source_kind`

This is intentionally minimal and exists to establish the next architectural seam.

---

## 4. Current flow

```text
HTTP request
   |
   v
IngestCommand
   |
   v
IngestService
   |
   +--> SourceInspector.inspect(source)
   |         |
   |         v
   |   SourceInspectionResult
   |
   +--> MetadataExtractor.extract(inspection)
             |
             v
      MetadataExtractionResult
             |
             v
      Registry stub document creation
```

---

## 5. Current limitations

The current metadata extraction layer does not yet:
- compute file hashes
- extract file size
- determine document type
- inspect PDF internals
- extract page count
- extract titles or codes
- produce OCR hints

---

## 6. Near-term next step

The next collaborator should be:

- `DocumentFactory`

Initial responsibility:
- accept extracted metadata
- create a `DocumentItem` in a consistent way

This will remove document construction logic from the registry and improve separation of responsibility.

---

## 7. Future evolution

Possible future metadata extraction capabilities:
- file extension normalization
- source hash calculation
- page count extraction
- document code detection
- title detection
- OCR hint generation
- source validation output
