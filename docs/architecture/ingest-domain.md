# Ingest Domain: vdm-safety-ai-agent

## Purpose

This document describes the current ingest-related domain language in the application.

The goal is to make ingest behavior explicit and prepare the codebase for a future real ingestion pipeline.

---

## 1. Current ingest domain concepts

The current ingest flow already uses explicit application-level concepts:

- `IngestCommand`
- `IngestResult`
- `ReplaceStrategy`

These concepts are part of the application language and should remain independent from direct HTTP transport concerns.

---

## 2. Current ingest input language

### 2.1. IngestCommand

Represents the application intent to ingest a source.

Current fields:
- `source`
- `replace_strategy`

Role:
- created by the API layer
- passed to `IngestService`
- should evolve as ingest capabilities grow

### 2.2. ReplaceStrategy

Represents how ingest should behave with respect to existing versions.

Current values:
- `new_versions_only`

Role:
- explicit domain value
- safer than a raw string
- ready for future extension

---

## 3. Current ingest output language

### 3.1. IngestResult

Represents the application result of an ingest operation.

Current fields:
- `job_id`
- `status`
- `document`

Role:
- returned by `IngestService`
- converted to transport response in the API layer

---

## 4. Current ingest behavior

Current behavior is still a stub workflow:

1. API request arrives
2. request is converted into `IngestCommand`
3. `IngestService` receives the command
4. registry creates a stub document
5. service returns `IngestResult`
6. API maps result to HTTP response

This is intentionally small but structurally sound.

---

## 5. Current limitations

The current ingest domain is still incomplete.

Limitations:
- no source inspection
- no file type classification
- no OCR decision
- no metadata extraction
- no section extraction
- no chunk generation
- no async job model

---

## 6. Near-term next step

The next structural step should introduce a dedicated collaborator for source inspection.

Planned collaborator:
- `SourceInspector`

Initial responsibility:
- inspect a source string
- classify source kind in a minimal stub form
- prepare the service layer for future real inspection logic

This allows ingest orchestration to grow without pushing infrastructure logic back into route handlers or registries.

---

## 7. Future ingest-domain candidates

Possible future ingest-domain concepts:
- `SourceKind`
- `SourceInspectionResult`
- `IngestJobStatus`
- `OCRDecision`
- `MetadataExtractionResult`
- `ChunkingPlan`
- `VersionRegistrationResult`
