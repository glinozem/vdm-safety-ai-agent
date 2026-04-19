# AGENTS.md

## Project

This repository implements a retrieval-first safety/compliance assistant for internal production instructions.
The system must prefer grounded answers with citations over broad generative behavior.

## Core principles

- Never invent requirements that are not grounded in repository docs, tests, or explicit issue scope.
- Prefer minimal, reviewable changes over broad refactors.
- Preserve auditability and traceability.
- For risky code paths, add tests before changing behavior when practical.

## Architecture constraints

- Keep ingestion, search, policy, and API layers separated.
- Do not couple OCR/parsing logic directly to web handlers.
- Do not bypass the policy layer for end-user answers.
- All answer-producing flows must preserve citation metadata.
- Keep risky business rules explicit and testable.

## Code expectations

- Use Python 3.12+.
- Prefer typed code where practical.
- Prefer small functions and explicit interfaces.
- Use structured logging.
- Avoid hidden side effects.
- Add or update tests for new business logic.

## Safe tasks for autonomous work

- repository scaffolding
- documentation
- typed schemas
- non-breaking refactors
- test generation
- API stubs
- CI improvements
- helper scripts

## Tasks requiring explicit human review

- auth and RBAC logic
- destructive migrations
- data deletion workflows
- secrets handling
- policy/guardrail weakening
- production infra changes
- changes to retention, audit, or citation behavior

## Working style

- Before editing, inspect relevant files and existing patterns.
- Keep diffs focused.
- Update docs when behavior changes.
- When introducing a new module, add a short module-level docstring.
- Do not rename files or move directories without a clear reason.

## Validation commands

Run these before considering a task done:

```bash
make lint
make test
```
