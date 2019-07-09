PACKAGE := allpairspy
BUILD_WORK_DIR := _work
DIST_DIR := $(BUILD_WORK_DIR)/$(PACKAGE)/dist
VENV_PATH := .venv


.PHONY: build
build:
	@rm -rf $(BUILD_WORK_DIR)/
	@mkdir -p $(BUILD_WORK_DIR)/
	@cd $(BUILD_WORK_DIR); \
		git clone https://github.com/thombashi/$(PACKAGE).git; \
		cd $(PACKAGE); \
		python setup.py sdist bdist_wheel
	@twine check $(DIST_DIR)/*
	ls -lh $(DIST_DIR)/*

.PHONY: clean
clean:
	@rm -rf $(PACKAGE)-*.*.*/ \
		$(BUILD_WORK_DIR) \
		dist/ \
		pip-wheel-metadata/ \
		.eggs/ \
		.pytest_cache/ \
		.tox/ \
		**/*/__pycache__/ \
		*.egg-info/
	@python setup.py clean --all
	@find . -not -path '*/\.*' -type f | grep -E .+\.py\.[a-z0-9]{32,}\.py$ | xargs -r rm

.PHONY: fmt
fmt:
	@black $(CURDIR)
	@autoflake --in-place --recursive --remove-all-unused-imports --exclude "__init__.py" .
	@isort --apply --recursive

.PHONY: release
release:
	@cd $(BUILD_WORK_DIR)/$(PACKAGE); python setup.py release --sign
	@make clean

.PHONY: venv
venv:
	virtualenv --version >/dev/null || pip3 install --user virtualenv
	test -d "$(VENV_PATH)"          || virtualenv --no-site-packages "$(VENV_PATH)"
	. "$(VENV_PATH)/bin/activate"   && pip3 install --quiet -r requirements/requirements.txt -r requirements/test_requirements.txt
	. "$(VENV_PATH)/bin/activate"   && pip3 install .
