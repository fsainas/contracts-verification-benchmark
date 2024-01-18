# Directories
VERSIONS_DIR = ../versions/
PROPERTIES_DIR = .
BUILD_DIR = build
CONTRACTS_DIR = $(BUILD_DIR)/contracts
LOGS_DIR = $(BUILD_DIR)/logs
LIB_DIR = $(CONTRACTS_DIR)/lib
SPEC_DIR = $(BUILD_DIR)/specs
SPEC_FILES = $(wildcard $(PROPERTIES_DIR)/*.spec)

PYTHON = python

GETTER_FILE = getters.sol
METHODS_FILE = methods.spec

contract = ""
specs = ""

.PHONY = run clean specs

run: clean_specs contracts specs directories 
	@$(PYTHON) ../../../scripts/run_certora.py --contracts $(CONTRACTS_DIR) --specs $(SPEC_DIR) --output $(BUILD_DIR)

one: clean_specs contracts specs directories 
	@$(PYTHON) ../../../scripts/runc.py --contract $(contract) --specs $(specs)

contracts: $(CONTRACTS_DIR) getters
	@$(PYTHON) ../../../scripts/injector.py --base $(VERSIONS_DIR) --inject $(GETTER_FILE) --output $(CONTRACTS_DIR)

specs: $(SPEC_DIR) 
	@for file in $(SPEC_FILES); do \
		if [ "$$file" != $(PROPERTIES_DIR)/"methods.spec" ]; then \
			echo "Processing $$file"; \
			cat $(METHODS_FILE) $$file >> $(SPEC_DIR)/$$file; \
		fi \
	done;

getters: 
	@if ! [ -e $(GETTER_FILE) ] ; then \
    	touch $(GETTER_FILE); \
	fi;

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
