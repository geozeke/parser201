PROJNAME=parser201
VER=patch
DRY=y

ifeq (${DRY},n)
	BUMPCMD?=bump2version ${VER}
else
	BUMPCMD?=bump2version ${VER} --dry-run --verbose
endif

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

.PHONY: clean
clean: ## Purge project build artifacts
	@echo Cleaning project artifacts
# @find . -type d -name .mypy_cache -exec rm -rf {} \; -prune
	@find . -type d -name __pycache__ -exec rm -rf {} \; -prune
	@find . -type d -name .pytest_cache -exec rm -rf {} \; -prune
	@find . -type d -name build -exec rm -rf {} \; -prune
	@find . -type d -name dist -exec rm -rf {} \; -prune
	@find . -type d -name .eggs -exec rm -rf {} \; -prune
	@find . -type d -name htmlcov -exec rm -rf {} \; -prune
	@find . -type d -name *.egg-info -exec rm -rf {} \; -prune
	@find . -type f -name *.egg -delete
	@find . -type f -name *.pyc -delete
	@find . -type f -name *.pyo -delete
	@find . -type f -name *.coverage -delete
	@echo Cleaning complete

# --------------------------------------------

.PHONY: coverage
coverage: ## Generate an html code coverage report
	coverage run -m pytest
	coverage report -m
	coverage html
	${BROWSER}

# --------------------------------------------

.PHONY: dist
dist: clean ## Build (but don't upload) distribution products
	python3 -m build
	twine check dist/*

# --------------------------------------------

.PHONY: docs
docs: ## Generate project documentation
	pdoc3 --html --template-dir=docs -o docs src/${PROJNAME} --force
	${BROWSER}

# --------------------------------------------

.PHONY: test
test: ## Run pytest with --tb=short option
	pytest --tb=short

# --------------------------------------------

.PHONY: uptest
uptest: dist ## Upload a build to test.pypi.org
	twine upload dist/* --repository ${PROJNAME}-test

# --------------------------------------------

.PHONY: bump
bump: ## Bump version. VER=major|minor|patch, DRY=Y|N
	${BUMPCMD}

# --------------------------------------------

.PHONY: release
release: dist ## Upload release version to pypi
	twine upload dist/* --repository ${PROJNAME}-release


# --------------------------------------------
.PHONY: help
help: ## Show help
	@echo Please specify a target. Choices are:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk \
	'BEGIN {FS = ":.*?## "}; \
	{printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
