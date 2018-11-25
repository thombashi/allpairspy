DOCS_DIR := docs
BUILD_DIR := _build

.PHONY: clean
clean:
	@rm -rf build dist .eggs/ .pytest_cache/ **/*/__pycache__/ *.egg-info/

.PHONY: fmt
fmt:
	@black $(CURDIR)
	@isort --apply --recursive
