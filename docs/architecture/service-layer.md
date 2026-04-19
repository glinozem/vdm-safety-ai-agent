# Service Layer: vdm-safety-ai-agent

## Purpose

This document defines the role of the service layer in the project.

The service layer is responsible for coordinating application behavior without embedding transport concerns directly into business logic.

It sits between:
- API route handlers
- domain-oriented services and registries
- future ingestion, retrieval, and policy pipelines

---

## 1. Why a service layer exists

The service layer exists to keep route handlers thin and to prevent application logic from leaking into HTTP endpoints.

Route handlers should:
- parse input
- call the appropriate service
- return the response model

Service classes should:
- coordinate application use cases
- call registries or lower-level services
- assemble response objects
- remain testable outside of HTTP

---

## 2. Current implemented services

Currently implemented:

- `InMemoryDocumentRegistry`
- `IngestService`

Current responsibilities:

### `InMemoryDocumentRegistry`
- hold document items in memory
- list current documents
- reset test state
- create stub document entries

### `IngestService`
- receive ingest request payload
- delegate document creation to the registry
- construct the ingest response

---

## 3. Route handler rules

Route handlers must remain thin.

They should not:
- generate IDs directly unless unavoidable
- implement orchestration logic inline
- mutate registry internals directly
- contain future OCR or parsing logic
- contain indexing logic

They may:
- validate input through schemas
- call service methods
- return response models
- set HTTP status codes

---

## 4. Service layer rules

Services should:
- expose explicit methods for use cases
- return typed schema objects where appropriate
- avoid direct dependency on HTTP-specific objects
- remain easy to unit test
- keep side effects explicit

Services should not:
- read from request objects directly
- depend on FastAPI request handlers
- perform hidden state mutations outside owned collaborators

---

## 5. Current dependency direction

Current dependency flow:

```text
API route
   |
   v
Service layer
   |
   v
Registry / lower-level collaborator
   |
   v
Schemas / state objects
```

Desired future direction:

```text
API route
   |
   v
Application service
   |
   +--> registry
   +--> ingest pipeline
   +--> retrieval service
   +--> policy service
   |
   v
Typed response
```

---

## 6. Immediate next evolution

The next structural improvement should introduce explicit interfaces or protocols for collaborators.

Examples:
- registry protocol
- ingest coordinator protocol
- retrieval protocol

This will make the codebase easier to extend and safer to evolve with Codex or other contributors.

---

## 7. Near-term implementation intent

Near-term service layer goals:

1. keep `IngestService` as the single entry point for ingest use cases
2. avoid placing future pipeline logic into route handlers
3. prepare for dependency injection
4. keep registry behavior testable in isolation
