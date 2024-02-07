# Params 
contract = ""
specs = ""
version = ""
property = ""

# Input Files
VERSIONS_DIR = ../versions/
PROPERTIES_DIR = .
GROUND_TRUTH = ../ground-truth.csv
SPEC_FILES = $(wildcard $(PROPERTIES_DIR)/*.spec)
GETTER_FILE = getters.sol
METHODS_FILE = methods.spec
VERSIONS_FILES = $(wildcard $(VERSIONS_DIR)/*.sol)

# Output Files
BUILD_DIR = build
OUTPUT_DIR = $(BUILD_DIR)
CONTRACTS_DIR = $(OUTPUT_DIR)/contracts
LOGS_DIR = $(OUTPUT_DIR)/logs
SPEC_DIR = $(OUTPUT_DIR)/specs
LIB_DIR = $(CONTRACTS_DIR)/lib
OUT = $(OUTPUT_DIR)/out.csv
CM = $(OUTPUT_DIR)/cm.csv
TABLE = $(OUTPUT_DIR)/table.md

PYTHON = python

.PHONY: run one setup contracts specs getters directories clean-specs clean

#---------------------------- RUN --------------------------------#
run: $(TABLE)

$(TABLE): $(CM)
	@echo "Generating Certora results table ($(TABLE))..."
	@echo "### Certora" > $(TABLE)
	@$(PYTHON) ../../../scripts/mdtable_gen.py --input $(CM) >> $(TABLE)

$(CM): $(GROUND_TRUTH) $(OUT) 
	@echo "Generating Certora confusion matrix ($(CM))..."
	@$(PYTHON) ../../../scripts/cm_gen.py --ground-truth $(GROUND_TRUTH) --results $(OUT) > $(CM)

$(OUT): clean-specs setup $(VERSIONS_FILES) $(SPEC_FILES) $(GETTER_FILE) 
	@echo "Running Certora experiments..."
	@$(PYTHON) ../../../scripts/run_certora.py --contracts $(CONTRACTS_DIR) --specs $(SPEC_DIR) --output $(OUTPUT_DIR) --version $(version) --property $(property)

one: clean-specs contracts specs directories 
	@$(PYTHON) ../../../scripts/run_certora.py --contracts $(contract) --specs $(specs)

#---------------------------- SETUP ------------------------------#
setup: contracts specs getters directories

contracts: $(CONTRACTS_DIR) getters
	@$(PYTHON) ../../../scripts/inject_getters.py --contracts $(VERSIONS_DIR) --getters $(GETTER_FILE) --output $(CONTRACTS_DIR)

specs: $(SPEC_DIR) 
	@for file in $(SPEC_FILES); do \
		if [ "$$file" != $(PROPERTIES_DIR)/"methods.spec" ]; then \
			echo "Processing $$file"; \
			cat $(METHODS_FILE) $$file >> $(SPEC_DIR)/$$file; \
		fi \
	done;

getters: 
	@if ! [ -e $(GETTER_FILE) ]; then touch $(GETTER_FILE); fi;

directories: $(CONTRACTS_DIR) $(LOGS_DIR) $(LIB_DIR) $(SPEC_DIR)

$(CONTRACTS_DIR):
	@mkdir -p $@

$(SPEC_DIR):
	@mkdir -p $@

$(LOGS_DIR):
	@mkdir -p $@

$(LIB_DIR):
	@cp -r ../../../lib/ $@

#---------------------------- CLEAN ------------------------------#
clean-specs:
	@echo "Cleaning specs..."
	@rm -rf $(SPEC_DIR)

clean:
	@echo "Deleting \"certora/build/\"..."
	@rm -rf $(BUILD_DIR)

