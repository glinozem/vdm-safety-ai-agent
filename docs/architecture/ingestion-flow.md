# Ingestion Flow: vdm-safety-ai-agent

## Purpose

This document defines the initial ingestion flow for the project.

The ingestion flow is responsible for accepting source documents, preparing them for retrieval, and preserving enough metadata for future traceability.

---

## 1. Ingestion goals

The ingestion subsystem must eventually support:

- archive ingestion
- single PDF ingestion
- text PDF detection
- scanned PDF detection
- OCR where needed
- metadata extraction
- section extraction
- chunk generation
- indexing
- version-aware document registration

At the current stage, only a stub flow is implemented.

---

## 2. Current implemented state

Current behavior:

1. API accepts `POST /api/v1/documents/ingest`
2. request contains:
   - `source`
   - `replace_strategy`
3. system creates a stub document entry in the in-memory registry
4. system returns:
   - `job_id`
   - `status=accepted`
   - stub `document`

Current limitations:

- no real file reading
- no archive unpacking
- no OCR
- no persistence
- no indexing
- no section extraction
- no asynchronous job execution

---

## 3. Target future flow

Planned target flow:

```text
Input source
   |
   v
Validate request
   |
   v
Resolve source type
   |
   +--> archive
   |       |
   |       v
   |   unpack files
   |
   +--> single pdf
           |
           v
      inspect pdf type
           |
           +--> text pdf
           |
           +--> scanned pdf -> OCR
           |
           v
      extract metadata
           |
           v
      split into sections
           |
           v
      generate chunks
           |
           v
      register document version
           |
           v
      index for retrieval
           |
           v
      return accepted / completed status
```

---

## 4. Planned ingestion stages

### Stage 1: request validation
Validate request schema and basic source presence.

### Stage 2: source resolution
Determine whether the source refers to:
- a single file
- an archive
- a local path
- a future external URI

### Stage 3: source inspection
Inspect file type and determine whether OCR is required.

### Stage 4: metadata extraction
Extract basic metadata such as:
- filename
- hash
- source type
- file size
- detected document type
- ingestion timestamp

### Stage 5: content extraction
Extract raw text and intermediate structure.

### Stage 6: normalization
Normalize sections, headings, and internal metadata.

### Stage 7: retrieval preparation
Generate chunks and attach retrieval metadata.

### Stage 8: registry and persistence
Register the document and version.

### Stage 9: indexing
Send prepared chunks into full-text and vector indexing.

---

## 5. Design constraints

The ingestion subsystem must follow these constraints:

- API handlers must stay thin
- ingestion orchestration must not live directly in route functions
- OCR must remain separable from parsing logic
- metadata generation must be explicit
- version registration must remain traceable
- future indexing must be decoupled from request parsing

---

## 6. Near-term implementation boundary

The next implementation step is not real ingestion yet.

The next code step should introduce an ingestion service layer that:
- accepts the ingest request
- delegates stub document creation
- returns a structured ingest response

This keeps route handlers thin and prepares the codebase for future real ingestion stages.

---

## 7. Immediate next coding step

Introduce:

- `app/services/ingest_service.py`

Responsibilities:
- receive `source` and `replace_strategy`
- call registry service
- construct ingest response
- keep API layer minimal
