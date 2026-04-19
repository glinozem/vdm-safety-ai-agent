# Application Models: vdm-safety-ai-agent

## Purpose

This document describes application-level models used inside service-layer use cases.

The goal is to separate:
- transport-level HTTP schemas
- application-level use-case models

This keeps service boundaries cleaner and makes future pipeline evolution easier.

---

## 1. Why application models exist

HTTP request and response schemas are useful at the API boundary, but they should not become the only language of the application.

Problems when transport models leak everywhere:
- tighter coupling to HTTP shape
- harder refactoring of service internals
- weaker separation of concerns
- more difficult transition to non-HTTP entry points
- harder evolution of internal workflows

Application models solve this by representing use-case intent directly.

---

## 2. Current application-level models

### 2.1. IngestCommand

Role:
- represent the application intent to ingest a document source

Current fields:
- `source`
- `replace_strategy`

Current behavior:
- created in the API route
- passed into `IngestService`

### 2.2. IngestResult

Role:
- represent the application result of an ingest operation

Current fields:
- `job_id`
- `status`
- `document`

Current behavior:
- returned by `IngestService`
- mapped back to HTTP response schema in the API route

---

## 3. Current flow

```text
HTTP request schema
   |
   v
IngestCommand
   |
   v
IngestService
   |
   v
IngestResult
   |
   v
HTTP response schema
```

---

## 4. Why this is useful

This separation gives the project:

- clearer service boundaries
- easier future non-HTTP reuse
- better testability of application behavior
- easier transition to multi-stage ingestion workflows
- cleaner route handlers

---

## 5. Current implementation boundary

The current application model layer is intentionally small.

Implemented:
- `IngestCommand`
- `IngestResult`

Not implemented yet:
- query command objects
- retrieval result objects
- policy decision objects
- pipeline stage result objects

---

## 6. Near-term next step

The next improvement should make `replace_strategy` explicit as a domain value.

Current limitation:
- `replace_strategy` is still a raw string

Near-term improvement:
- introduce `ReplaceStrategy`
- use it in `IngestCommand`
- keep HTTP JSON stable

---

## 7. Future candidates for application-level models

Possible future models:
- `ListDocumentsQuery`
- `RetrieveAnswerCommand`
- `PolicyDecision`
- `IngestJobStatus`
- `ChunkingResult`
- `IndexingResult`
