# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A Python client SDK for the **actinia** REST API (the GRASS REST API for scalable, distributed geospatial processing). The package name is `actinia_openapi_python_client`.

**Almost all of the code in this repository is auto-generated** by [OpenAPI Generator](https://openapi-generator.tech) (generator version 7.2.0-SNAPSHOT, `PythonClientCodegen`) from an Actinia Swagger/OpenAPI spec. This is the single most important fact about the repo: do not hand-edit generated files to add features or fix API-shape bugs — regenerate from the spec instead. Hand-editing is only appropriate for files the generator is told to leave alone (see `.openapi-generator-ignore`) or for the packaging/CI metadata described below.

## Regenerating the client

The source of truth is the OpenAPI spec file in the repo root (`actinia_swagger_x.x.x.json`; an older `actinia_swagger.json` is also present). Generation is configured by `config.yaml` (package name, version, author, install requires). The output is the `actinia_openapi_python_client/`, `test/`, and `docs/` trees plus `README.md`.

Note: `generate.sh` in the repo root invokes the `kotlin-spring` generator, not the Python client generator — it does **not** reproduce this package and should not be used to regenerate it. The actual Python client is produced with the `python` generator driven by `config.yaml`. When regenerating, run `openapi-generator-cli` with `-g python -c config.yaml -i actinia_swagger_x.x.x.json` and bump `packageVersion` in `config.yaml` to match.

When changing the package version, keep these in sync: `config.yaml` (`packageVersion`), `pyproject.toml` (`version`), and `setup.py` (`VERSION`).

## Commands

Install for development and testing:
```sh
pip install -r requirements.txt
pip install -r test-requirements.txt
```

Run the full test suite:
```sh
pytest
```

Run a single test file / test:
```sh
pytest test/test_api_log_api.py
pytest test/test_api_log_api.py::TestAPILogApi::test_api_log_user_id_get
```
Note: `pytest-randomly` is installed, so test ordering is randomized by default. Use `pytest -p no:randomly` for a fixed order.

Run with coverage (as CI does):
```sh
pytest --cov=actinia_openapi_python_client
```

Lint (matches the GitHub Actions check):
```sh
# Fails the build on real errors:
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
# Style warnings only (never fails):
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```
`setup.cfg` sets `max-line-length=99` for editor/flake8 defaults, but CI uses `--max-line-length=127`.

Build the distribution (as the publish workflow does):
```sh
python -m build
```

## Architecture

The generated SDK follows the standard OpenAPI `python` client layout. Understanding these few pieces lets you navigate the ~28 API classes and ~98 models without reading them all:

- **`actinia_openapi_python_client/__init__.py`** — the package facade. Re-exports every `*Api` class and every model, so users do `actinia_openapi_python_client.ProcessingApi`, etc.
- **`api/`** — one module per API tag (e.g. `processing_api.py`, `raster_management_api.py`, `location_management_api.py`). Each holds a single `*Api` class whose methods correspond 1:1 to REST endpoints. Method names are derived from the path + verb (e.g. `locations_location_name_mapsets_get`). Every endpoint method has three variants: the plain call, `*_with_http_info`, and `*_without_preload_content`.
- **`models/`** — one Pydantic v2 model per module (the SDK requires `pydantic >= 2`). These are the request/response body schemas.
- **`api_client.py`** (`ApiClient`) — the engine. Handles serialization/deserialization between models and JSON, parameter substitution, auth, and dispatching to the REST layer. The `*Api` classes are thin wrappers that build call params and hand them to `ApiClient`.
- **`configuration.py`** (`Configuration`) — host, credentials, TLS, and other settings. The only auth scheme defined is HTTP basic auth (`basicAuth`); construct with `username=`/`password=`. Default host is `http://localhost`.
- **`rest.py`** (`RESTClientObject`) — the urllib3-based HTTP transport.
- **`exceptions.py`** — exception hierarchy rooted at `OpenApiException` / `ApiException`, with subclasses by status family (`BadRequestException`, `UnauthorizedException`, `NotFoundException`, `ForbiddenException`, `ServiceException`).

Domain concepts that recur throughout the API surface (from Actinia/GRASS GIS): **locations** contain **mapsets**, which contain **raster_layers**, **vector_layers**, and **STRDS** (space-time raster datasets). Long-running operations are **resources** with async (`*_async`) and sync variants and status-polling endpoints.

The `test/` tree mirrors the generated code: one `test_*.py` per API class and per model. These are generator-produced stubs (`pass` bodies) — they verify importability/instantiation rather than behavior.

## CI

GitHub Actions (`.github/workflows/python.yml`) runs flake8 + pytest on Python 3.11–3.12 for every push and PR. `.github/workflows/python-publish.yml` builds and publishes to PyPI on a published GitHub release (uses `PYPI_API_TOKEN`). A parallel GitLab CI config (`.gitlab-ci.yml`) runs the same pytest matrix. Supported Python is **3.11+**.
