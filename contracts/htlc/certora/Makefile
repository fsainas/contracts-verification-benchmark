# Directories
VERSIONS_DIR = ../versions/
PROPERTIES_DIR = .
BUILD_DIR = build
CONTRACTS_DIR = $(BUILD_DIR)/contracts
LOGS_DIR = $(BUILD_DIR)/logs
LIB_DIR = $(CONTRACTS_DIR)/lib
SPEC_DIR = $(BUILD_DIR)/specs
SPEC_FILES = $(wildcard $(PROPERTIES_DIR)/p*.spec)

PYTHON = python

GETTER_FILE = getters.sol
METHODS_FILE = methods.spec

.PHONY = run clean specs

run: clean contracts specs directories 
	@$(PYTHON) ../../../scripts/run_certora.py --input $(CONTRACTS_DIR) --spec $(SPEC_DIR) --output $(BUILD_DIR)

contracts: $(CONTRACTS_DIR)
	@$(PYTHON) ../../../scripts/injector.py --base $(VERSIONS_DIR) --inject $(GETTER_FILE) --output $(CONTRACTS_DIR)

specs: $(SPEC_DIR) 
	@for file in $(SPEC_FILES); do \
		echo "Processing $$file"; \
		cat $(METHODS_FILE) $$file >> $(SPEC_DIR)/$$file; \
	done;

directories: $(CONTRACTS_DIR) $(LOGS_DIR) $(LIB_DIR) $(SPEC_DIR)

$(CONTRACTS_DIR):
	@mkdir -p $@

$(SPEC_DIR):
	@mkdir -p $@

$(LOGS_DIR):
	@mkdir -p $@

$(LIB_DIR):
	@cp -r ../../../lib/ $@

clean_specs:
	rm -rf $(SPEC_DIR)

clean:
	rm -rf $(BUILD_DIR)

