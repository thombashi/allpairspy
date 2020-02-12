PACKAGE := allpairspy
BUILD_WORK_DIR := _work
DIST_DIR := $(BUILD_WORK_DIR)/$(PACKAGE)/dist


.PHONY: build
build:
	@make clean
	@tox -e build
	ls -lh dist/*

.PHONY: build-remote
build-remote:
	@rm -rf $(BUILD_WORK_DIR)/
	@mkdir -p $(BUILD_WORK_DIR)/
	@cd $(BUILD_WORK_DIR); \
		git clone https://github.com/thombashi/$(PACKAGE).git; \
		cd $(PACKAGE); \
		python setup.py sdist bdist_wheel
	@twine check $(DIST_DIR)/*
	ls -lh $(DIST_DIR)/*

.PHONY: check
check:
	@tox -e lint
	travis lint

.PHONY: clean
clean:
	@tox -e clean

.PHONY: fmt
fmt:
	tox -e fmt

.PHONY: release
release:
	@cd $(BUILD_WORK_DIR)/$(PACKAGE); python setup.py release --sign
	@make clean
