# Domain Values: vdm-safety-ai-agent

## Purpose

This document describes the use of explicit domain values in the project.

The goal is to reduce stringly-typed application behavior and make important model fields safer, clearer, and easier to evolve.

---

## 1. Why domain values matter

String literals are easy to introduce but fragile over time.

Problems with raw string values:
- typo risk
- inconsistent usage across modules
- weak discoverability
- harder refactoring
- harder validation in service and domain logic

For these reasons, the project now uses explicit enums for selected document fields.

---

## 2. Current implemented domain values

### 2.1. DocumentType

Current values:
- `stub`
- `instruction`

Current Python representation:
- `DocumentType.STUB`
- `DocumentType.INSTRUCTION`

### 2.2. DocumentStatus

Current values:
- `accepted`
- `active`

Current Python representation:
- `DocumentStatus.ACCEPTED`
- `DocumentStatus.ACTIVE`

---

## 3. Why StrEnum is used

The project uses `StrEnum` because it provides:

- enum semantics in Python code
- stable string serialization in API responses
- compatibility with pydantic and FastAPI JSON output
- easier transition away from magic strings

This allows internal code to be stricter while preserving external JSON contracts.

---

## 4. Current usage points

Domain values are currently used in:
- `DocumentItem`
- `DocumentIngestResponse`
- registry stub document creation
- ingest service response creation
- unit tests for query and ingest flows

---

## 5. Current external API behavior

Even though enums are used internally, the external API still returns strings such as:

```json
{
  "doc_type": "stub",
  "status": "accepted"
}
```

This is the intended behavior.

---

## 6. Near-term next step

The next structural improvement is to introduce application-level ingest objects:

- `IngestCommand`
- `IngestResult`

Why:
- separate transport schemas from application use-case objects
- make service boundaries clearer
- prepare for future real ingestion pipeline stages
- keep HTTP request/response models from becoming the only application language

---

## 7. Future candidates for explicit domain values

Possible future enum/value-object candidates:
- replace strategy
- ingest status
- document source type
- section type
- risk level
- workflow status
