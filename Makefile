OWNER := thombashi
PACKAGE := allpairspy
BUILD_WORK_DIR := _work
DIST_DIR := $(BUILD_WORK_DIR)/$(PACKAGE)/dist
PKG_BUILD_DIR := $(BUILD_WORK_DIR)/$(PACKAGE)
PYTHON := python3


.PHONY: build
build: clean
	@$(PYTHON) -m tox -e build
	ls -lh dist/*

.PHONY: build-remote
build-remote: clean
	@mkdir -p $(BUILD_WORK_DIR)
	@cd $(BUILD_WORK_DIR) && \
		git clone --depth 1 https://github.com/$(OWNER)/$(PACKAGE).git && \
		cd $(PACKAGE) && \
		$(PYTHON) -m tox -e build
	ls -lh $(PKG_BUILD_DIR)/dist/*

.PHONY: check
check:
	@$(PYTHON) -m tox -e lint

.PHONY: clean
clean:
	@rm -rf $(BUILD_WORK_DIR)
	@$(PYTHON) -m tox -e clean

.PHONY: fmt
fmt:
	$(PYTHON) -m tox -e fmt

.PHONY: release
release:
	@cd $(PKG_BUILD_DIR) && @$(PYTHON) setup.py release --verbose
	@$(MAKE) clean

.PHONY: setup-ci
setup-ci:
	@$(PYTHON) -m pip install -q --disable-pip-version-check --upgrade tox

.PHONY: setup
setup: setup-ci
	@$(PYTHON) -m pip install -q --disable-pip-version-check --upgrade -e .[test] releasecmd
	@$(PYTHON) -m pip check
