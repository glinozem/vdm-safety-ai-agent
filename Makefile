PYTHON ?= python
UVICORN ?= uvicorn
APP_MODULE ?= app.api.main:app

.PHONY: install lint test run

install:
	$(PYTHON) -m pip install -e .[dev]

lint:
	ruff check .

test:
	pytest

run:
	$(UVICORN) $(APP_MODULE) --reload
