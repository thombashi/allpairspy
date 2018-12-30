BUILD_DIR := build
DOCS_DIR := docs

.PHONY: build
build:
	@make clean
	@python setup.py build
	@rm -rf $(BUILD_DIR)/

.PHONY: clean
clean:
	@rm -rf $(BUILD_DIR)/ dist/ .eggs/ .pytest_cache/ .tox/ **/*/__pycache__/ *.egg-info/

.PHONY: fmt
fmt:
	@black $(CURDIR)
	@isort --apply --recursive

.PHONY: release
release:
	@python setup.py release
	@rm -rf dist/
