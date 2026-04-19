# Data Model: vdm-safety-ai-agent

## Overview

This document defines the initial logical data model for the project.

The model is version-aware and designed for:
- document ingestion
- OCR-aware processing
- section and chunk extraction
- retrieval with metadata
- future auditability and feedback loops

---

## 1. Core entities

### 1.1. Document

Represents a logical document identity across versions.

Fields:
- `id`
- `code`
- `title`
- `doc_type`
- `status`
- `owner_department`
- `current_version_id`
- `created_at`
- `updated_at`

Notes:
- a document may have multiple versions
- `code` is expected to be human-recognizable, for example an internal instruction code

---

### 1.2. DocumentVersion

Represents a concrete ingested version of a document.

Fields:
- `id`
- `document_id`
- `version_label`
- `effective_date`
- `expiry_date`
- `source_file_uri`
- `source_hash`
- `is_ocr`
- `ocr_quality_score`
- `ingest_status`
- `metadata_json`
- `created_at`

Notes:
- every ingest creates or updates a version record
- OCR-related fields must remain explicit

---

### 1.3. Section

Represents a structured section extracted from a document version.

Fields:
- `id`
- `version_id`
- `parent_section_id`
- `section_path`
- `section_title`
- `section_type`
- `page_from`
- `page_to`
- `raw_text`
- `normalized_text`

Notes:
- sections may form a hierarchy
- `section_type` should later be normalized for safety-related instructions

---

### 1.4. Chunk

Represents a retrieval unit derived from a section.

Fields:
- `id`
- `section_id`
- `chunk_index`
- `text`
- `embedding_vector`
- `fts_vector`
- `metadata_json`

Notes:
- chunks are the main retrieval units
- citation metadata must be recoverable from chunk metadata

---

### 1.5. NormativeRef

Represents a reference from the document to an external or internal norm.

Fields:
- `id`
- `version_id`
- `ref_type`
- `ref_code`
- `ref_title`
- `issuer`
- `effective_to`
- `confidence`

---

### 1.6. Tag

Represents normalized classification metadata.

Fields:
- `id`
- `tag_type`
- `tag_value`

Examples:
- risk tags
- work type tags
- role tags
- equipment tags

---

### 1.7. ChunkTag

Join entity between chunks and tags.

Fields:
- `chunk_id`
- `tag_id`

---

## 2. Audit entities

### 2.1. QASession

Represents a user interaction session.

Fields:
- `id`
- `user_id`
- `channel`
- `started_at`
- `ended_at`

---

### 2.2. QATrace

Represents a trace of a user query and the system behavior.

Fields:
- `id`
- `session_id`
- `user_query`
- `classified_intent`
- `risk_class`
- `retrieval_json`
- `answer_json`
- `policy_json`
- `created_at`

Notes:
- this entity is critical for auditability
- risky flows must be reproducible

---

### 2.3. Feedback

Represents user or reviewer feedback on an answer or trace.

Fields:
- `id`
- `trace_id`
- `verdict`
- `comment`
- `reviewer_id`
- `created_at`

---

## 3. High-level relationships

- `Document 1 -> N DocumentVersion`
- `DocumentVersion 1 -> N Section`
- `Section 1 -> N Chunk`
- `DocumentVersion 1 -> N NormativeRef`
- `Chunk N -> M Tag` through `ChunkTag`
- `QASession 1 -> N QATrace`
- `QATrace 1 -> N Feedback` or reviewer comments over time

---

## 4. Initial implementation boundary

For the first implementation stage, only a subset is required in code:

- document response schemas
- ingest request schema
- simple in-memory registry service
- list documents endpoint
- ingest stub endpoint

Persistence is not required yet.

---

## 5. Near-term coding order

1. API schemas for documents
2. in-memory registry service
3. `GET /api/v1/documents`
4. `POST /api/v1/documents/ingest`
5. tests for registry behavior
