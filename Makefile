PACKAGE := allpairspy
BUILD_DIR := build
BUILD_WORK_DIR := _work


.PHONY: build
build:
	@rm -rf $(BUILD_WORK_DIR)/
	@mkdir -p $(BUILD_WORK_DIR)/
	@cd $(BUILD_WORK_DIR); \
		git clone https://github.com/thombashi/$(PACKAGE).git; \
		cd $(PACKAGE); \
		python setup.py build
	ls $(BUILD_WORK_DIR)/$(PACKAGE)/dist/

.PHONY: clean
clean:
	@rm -rf $(PACKAGE)-*.*.*/ \
		$(BUILD_DIR) \
		$(BUILD_WORK_DIR) \
		dist/ \
		.eggs/ \
		.pytest_cache/ \
		.tox/ \
		**/*/__pycache__/ \
		*.egg-info/

.PHONY: fmt
fmt:
	@black $(CURDIR)
	@isort --apply --recursive

.PHONY: release
release:
	@cd $(BUILD_WORK_DIR)/$(PACKAGE); python setup.py release
	@rm -rf $(BUILD_WORK_DIR)
