ifeq (${MAKECMDGOALS},docs)
	WEBPATH=docs/index.html
endif

ifeq (${MAKECMDGOALS},coverage)
	WEBPATH=htmlcov/index.html
endif

# --------------------------------------------

define BROWSER_PYSCRIPT
import webbrowser
from pathlib import Path
p = Path('.').resolve()/'${WEBPATH}'
webbrowser.open(f'file://{p}', new=2)
endef

export BROWSER_PYSCRIPT
BROWSER?=python3 -c "$$BROWSER_PYSCRIPT"

# --------------------------------------------

all: help

# --------------------------------------------

.PHONY: setup
setup: ## setup project with runtime dependencies
ifeq (,$(wildcard .init/setup))
	@(which uv > /dev/null 2>&1) || \
	(echo "parser201 requires uv. See README for instructions."; exit 1)
	mkdir .init
	touch .init/setup
	uv sync --no-dev --frozen
else
	@echo "Initial setup is already complete. If you are having issues, run:"
	@echo
	@echo "make reset"
	@echo "make setup"
	@echo
endif

# --------------------------------------------

.PHONY: dev
dev: ## add development dependencies (run make setup first)
ifneq (,$(wildcard .init/setup))
	uv sync --frozen
	@touch .init/dev
else
	@echo "Please run \"make setup\" first"
endif

# --------------------------------------------

.PHONY: upgrade
upgrade: ## upgrade project dependencies
ifeq (,$(wildcard .init/dev))
	uv sync --no-dev --upgrade
else
	uv sync --upgrade
endif

# --------------------------------------------

.PHONY: reset
reset: clean ## reinitialize the project
	@echo Resetting project state
	rm -rf .init .mypy_cache .ruff_cache .venv

# --------------------------------------------

.PHONY: clean
clean: ## Purge build artifacts
	@echo Cleaning project build artifacts
	@rm -rf build/
	@rm -rf dist/
	@find . -type d -name __pycache__ -exec rm -rf {} \; -prune
	@find . -type d -name .pytest_cache -exec rm -rf {} \; -prune
	@find . -type d -name .eggs -exec rm -rf {} \; -prune
	@find . -type d -name htmlcov -exec rm -rf {} \; -prune
	@find . -type d -name *.egg-info -exec rm -rf {} \; -prune
	@find . -type f -name *.egg -delete
	@find . -type f -name *.pyc -delete
	@find . -type f -name *.pyo -delete
	@find . -type f -name *.coverage -delete

# --------------------------------------------

.PHONY: coverage
coverage: ## Generate an html code coverage report
	coverage run -m pytest
	coverage report -m
	coverage html
	${BROWSER}

# --------------------------------------------

.PHONY: docs
docs: ## Generate project documentation
	pdoc -o docs -t templates -d numpy --no-include-undocumented src/*
	${BROWSER}

# --------------------------------------------

.PHONY: test
test: ## Run pytest with --tb=short option
	pytest --tb=short

# --------------------------------------------

.PHONY: help
help: ## Show help
	@echo Please specify a target. Choices are:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk \
	'BEGIN {FS = ":.*?## "}; \
	{printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
