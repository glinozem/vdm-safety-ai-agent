# API Contracts: vdm-safety-ai-agent

## Overview

This document defines the initial HTTP API contracts for the project.

Current status:
- implemented: root endpoint
- implemented: versioned health endpoint
- planned: document registry endpoints
- planned: ingest stub endpoint

Base assumptions:
- API is served by FastAPI
- versioned routes use `/api/v1`
- all responses are JSON
- user-facing retrieval endpoints will later require citation-aware response schemas

---

## 1. Root endpoint

### Request

`GET /`

### Response

Status: `200 OK`

```json
{
  "service": "vdm-safety-ai-agent",
  "status": "ok"
}
```

### Notes

This endpoint is intended for a simple browser check and very basic service presence verification.

---

## 2. Health endpoint

### Request

`GET /api/v1/health`

### Response

Status: `200 OK`

```json
{
  "status": "ok"
}
```

### Notes

This endpoint is intended for:
- health checks
- local smoke tests
- infrastructure probes

---

## 3. Planned document registry endpoint

### Request

`GET /api/v1/documents`

### Initial response

Status: `200 OK`

```json
{
  "items": []
}
```

### Planned query parameters

- `status`
- `doc_type`
- `limit`
- `offset`

### Notes

Initial implementation may return an empty list until persistence is introduced.

---

## 4. Planned ingest stub endpoint

### Request

`POST /api/v1/documents/ingest`

### Initial request body

```json
{
  "source": "local-file-or-uri",
  "replace_strategy": "new_versions_only"
}
```

### Initial response

Status: `202 Accepted`

```json
{
  "job_id": "stub-job-id",
  "status": "accepted"
}
```

### Notes

Initial implementation may be a stub and does not need to perform real ingestion yet.

---

## 5. Response design rules

The following response rules should hold as the API grows:

- JSON only
- stable top-level object responses
- explicit field names
- no hidden citations for retrieval endpoints
- risky answer endpoints must later include evidence metadata

---

## 6. Error design rules

Planned error response format:

```json
{
  "error": {
    "code": "string_code",
    "message": "human-readable message"
  }
}
```

Examples of future error codes:
- `validation_error`
- `not_found`
- `unsupported_operation`
- `ingest_failed`
- `policy_blocked`

---

## 7. Near-term implementation order

1. `GET /api/v1/documents`
2. `POST /api/v1/documents/ingest`
3. document schemas
4. service layer behind registry endpoints

