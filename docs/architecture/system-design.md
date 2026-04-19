# System Design: vdm-safety-ai-agent

## Purpose

`vdm-safety-ai-agent` is a retrieval-first safety and compliance assistant for internal production instructions, occupational safety, and fire safety documents.

The system must provide grounded answers with citations and preserve auditability for risky flows.

## Scope

Initial MVP scope:

- ingest PDF archives and individual PDF documents
- detect text PDFs vs scanned PDFs
- run OCR where needed
- extract text and metadata
- store document versions
- support hybrid retrieval
- answer questions with citations
- provide auditability for risky flows

## Architecture principles

- retrieval-first, not free-form generative-first
- grounded answers only for user-facing responses
- citation metadata must be preserved end-to-end
- ingestion, retrieval, policy, and API layers must stay separated
- version-aware document handling
- explicit and testable business rules

## High-level architecture

```text
[Client / Web UI / Bot]
          |
          v
[FastAPI API Layer]
          |
          v
[Orchestrator Layer]
   |        |        |
   v        v        v
[Policy] [Retrieval] [Workflows]
          |
          v
   [Search Facade]
     |         |
     v         v
[Full-text] [Vector]
          |
          v
   [Knowledge Store]
     |          |
     v          v
[Object Storage] [Metadata DB]

[Ingestion Pipeline]
unpack -> OCR -> parse -> metadata -> chunking -> indexing
```

## Repository mapping

- `app/api/` — FastAPI entrypoints and routers
- `app/orchestrator/` — request orchestration
- `app/policy/` — policy and guardrails
- `app/retrieval/` — retrieval interfaces and logic
- `app/workflows/` — checklist, briefing, quiz workflows
- `ingestion/` — unpacking, OCR, parsing, metadata, indexing
- `search/` — full-text, vector search, reranking
- `docs/` — architecture, product, and operational documentation
- `tests/` — unit, integration, and eval tests

## Current implemented state

Implemented now:

- FastAPI application bootstrap
- root endpoint `/`
- versioned health endpoint `/api/v1/health`
- settings via `app/config.py`
- pytest-based health check

Not implemented yet:

- document registry
- ingestion pipeline
- OCR pipeline
- search layer
- policy engine
- workflow builders
- persistence layer
- audit trail

## Next implementation steps

1. Add architecture documents:
   - `docs/architecture/api-contracts.md`
   - `docs/architecture/data-model.md`

2. Introduce document registry skeleton:
   - schemas
   - service layer
   - list endpoint
   - ingest stub endpoint

3. Add first domain tests.

## Definition of architectural safety

The following must remain true as the codebase grows:

- no user-facing safety answer without explicit retrieval evidence
- no bypass of the policy layer for risky flows
- no tight coupling between OCR/parsing and web handlers
- no hidden mutation of citation metadata

