# Source Inspection: vdm-safety-ai-agent

## Purpose

This document describes the current source inspection layer in the application.

The goal of source inspection is to classify an ingest source before the system grows into a real ingestion pipeline.

---

## 1. Why source inspection exists

Source inspection exists to keep source-related logic out of:
- API route handlers
- registry implementations
- generic service orchestration logic

It provides a dedicated collaborator responsible for answering:
- what kind of source was received
- how that source should be treated by later pipeline stages

---

## 2. Current implemented concepts

### 2.1. SourceKind

Current values:
- `local_file`
- `unknown`

Role:
- represent a minimal domain classification for an ingest source

### 2.2. SourceInspectionResult

Current fields:
- `source`
- `source_kind`

Role:
- represent the application-level outcome of source inspection

---

## 3. Current implemented collaborator

### `SourceInspector`

Role:
- inspect a source string
- return a minimal `SourceInspectionResult`

Current stub behavior:
- sources ending with `.pdf` are classified as `local_file`
- all other sources are classified as `unknown`

This is intentionally simple and only exists to establish the architectural seam.

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
   v
SourceInspector.inspect(source)
   |
   v
SourceInspectionResult
   |
   v
Registry stub document creation
```

---

## 5. Current limitations

The current source inspection layer does not yet:
- check file existence
- distinguish archive vs single document
- validate URI schemes
- determine OCR need
- inspect MIME type
- inspect file extension beyond simple suffix logic

---

## 6. Near-term next step

The next collaborator should be:

- `MetadataExtractor`

Initial responsibility:
- accept source inspection output
- return a stub metadata result

This will continue moving the ingest flow toward a pipeline of explicit collaborators.

---

## 7. Future evolution

Possible future source inspection capabilities:
- archive detection
- PDF vs non-PDF classification
- URI source support
- source existence checks
- MIME-aware inspection
- OCR routing hints
