# vdm-safety-ai-agent

Retrieval-first safety and compliance assistant for internal production instructions, occupational safety, and fire safety documents.

## Purpose

This project implements an internal AI assistant that works with a controlled corpus of production instructions and related safety documents. The system must prefer grounded answers with citations over broad generative behavior.

## MVP scope

- ingest PDF archives and individual PDFs
- detect text PDFs vs scans
- run OCR when needed
- store document versions and metadata
- support hybrid retrieval (full-text + vector)
- answer user questions with citations
- produce checklists, briefing cards, and short summaries
- keep an audit trail for risky flows

## Repository layout

```text
.github/           GitHub templates and CI
app/               API, orchestrator, retrieval, policy, workflow code
ingestion/         archive unpacking, OCR, parsing, metadata, indexing
search/            full-text, vector retrieval, reranking
docs/              product, architecture, runbooks, ADRs
infra/             local/dev/prod infrastructure
scripts/           helper scripts
tests/             unit, integration, retrieval, eval tests
```

## Local setup

### Requirements

- Python 3.12+
- pip or uv
- make

### Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
make test
make run
```

Application will start on `http://127.0.0.1:8000`.

## Initial API

- `GET /health` — service health check

## Development workflow

1. create an issue
2. create a branch from `main`
3. make a small focused change
4. run lint and tests
5. open a pull request
6. request review

## Definition of done

A change is considered complete only if:

- code is focused and reviewable
- tests are added or updated when behavior changes
- docs are updated when the public behavior changes
- lint and test checks pass in CI
- architecture constraints from `AGENTS.md` are respected

## Next documents to add

- `docs/architecture/system-design.md`
- `docs/architecture/data-model.md`
- `docs/architecture/api-contracts.md`
- `docs/architecture/security-guardrails.md`
- `docs/product/vision.md`
- `docs/product/scope.md`
