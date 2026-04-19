# Dependency Wiring: vdm-safety-ai-agent

## Purpose

This document describes how dependencies are currently wired in the application.

The goal is to make service construction explicit, reduce direct coupling in route handlers, and prepare the codebase for future dependency injection evolution.

---

## 1. Current wiring model

The current application uses three layers for dependency wiring:

1. registry implementation
2. service container
3. API dependency providers

This creates a simple but explicit flow from shared collaborators to route handlers.

---

## 2. Current components

### 2.1. Registry

Current registry implementation:

- `InMemoryDocumentRegistry`

Role:
- hold in-memory document items
- support current bootstrap and stub flows
- provide collaborator behavior for services

---

### 2.2. Services

Current services:

- `DocumentQueryService`
- `IngestService`

Role:
- coordinate application behavior
- work with collaborators through protocols
- return typed response models

---

### 2.3. Service container

Current container:

- `ServiceContainer`
- exported instance: `container`

Role:
- construct service instances
- share the same registry collaborator
- provide a single wiring location for current application services

---

### 2.4. API dependency providers

Current providers:

- `get_document_registry()`
- `get_document_query_service()`
- `get_ingest_service()`

Role:
- provide route-safe access to dependencies
- decouple route modules from direct container usage
- prepare the codebase for future FastAPI dependency overrides

---

## 3. Current dependency flow

```text
Route handler
   |
   v
API dependency provider
   |
   v
Service container / provider wiring
   |
   v
Service object
   |
   v
Registry collaborator
```

---

## 4. Why this is better than direct globals

This approach is better than direct route-to-global wiring because it:

- keeps route handlers thinner
- makes service creation more explicit
- reduces hidden coupling
- prepares the codebase for overrides in tests
- makes future dependency injection easier

---

## 5. Current limitations

The current approach is still intentionally simple.

Current limitations:
- global `container` instance still exists
- registry is still an in-memory implementation
- service construction is not yet environment-aware
- there is no FastAPI override usage yet
- there is no lifecycle management for shared dependencies

---

## 6. Near-term next step

The next practical model improvement is to reduce stringly-typed domain values.

Current examples:
- `doc_type="stub"`
- `status="accepted"`

Near-term improvement:
- introduce enums for document type and status
- update schemas and tests
- keep JSON responses stable

---

## 7. Future evolution

Possible future evolution:

1. explicit dependency override support in tests
2. environment-aware container creation
3. persistence-backed registry implementation
4. real ingest pipeline collaborators
5. retrieval and policy providers
