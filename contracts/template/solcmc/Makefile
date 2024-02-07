# Params
solver = z3
to = 10m
contract = ""
version = ""
property = ""

# Input files
VERSIONS_DIR = ../versions/
PROPERTIES_DIR = .
GROUND_TRUTH = ../ground-truth.csv
PROPERTIES_FILES = $(wildcard $(PROPERTIES_DIR)/*.sol)
VERSIONS_FILES = $(wildcard $(VERSIONS_DIR)/*.sol)

# Output files
BUILD_DIR = build
OUTPUT_DIR = $(BUILD_DIR)/$(solver)
CONTRACTS_DIR = $(BUILD_DIR)/contracts
LOGS_DIR = $(OUTPUT_DIR)/logs
LIB_DIR = $(CONTRACTS_DIR)/lib
OUT = $(OUTPUT_DIR)/out.csv
CM = $(OUTPUT_DIR)/cm.csv
TABLE = $(OUTPUT_DIR)/table.md

PYTHON = python

.PHONY: run one setup contracts directories clean

#---------------------------- RUN --------------------------------#
run: $(TABLE)

$(TABLE): $(CM)
	@echo "Generating SolCMC results table ($(TABLE))..."
	@if [ $(solver) = "z3" ]; then echo "#### Z3" > $(TABLE); \
	elif [ $(solver) = "eld" ]; then echo "#### Eldarica" > $(TABLE); fi
	@$(PYTHON) ../../../scripts/mdtable_gen.py --input $(CM) >> $(TABLE)

$(CM): $(GROUND_TRUTH) $(OUT)
	@echo "Generating Solcmc confusion matrix ($(CM))..."
	@$(PYTHON) ../../../scripts/cm_gen.py --ground-truth $(GROUND_TRUTH) --results $(OUT) > $(CM)

$(OUT): setup $(PROPERTIES_FILES) $(VERSIONS_FILES)
	@echo "Running SolCMC ($(solver)) experiments..."
	@$(PYTHON) ../../../scripts/run_solcmc.py --contracts $(CONTRACTS_DIR)/ --output $(OUTPUT_DIR) --timeout $(to) --solver $(solver) --version $(version) --property $(property)

one: setup
	@$(PYTHON) ../../../scripts/run_solcmc.py --contracts $(contract) --timeout $(to)

#---------------------------- SETUP ------------------------------#
setup: contracts directories

contracts: $(VERSIONS_FILES) $(PROPERTIES_FILES) $(CONTRACTS_DIR)
	@echo "Building contracts..."
	@$(PYTHON) ../../../scripts/builder.py --versions $(VERSIONS_DIR) --properties $(PROPERTIES_DIR) --output $(CONTRACTS_DIR)

directories: $(CONTRACTS_DIR) $(LOGS_DIR) $(LIB_DIR)

$(CONTRACTS_DIR):
	@mkdir -p $@

$(LOGS_DIR):
	@mkdir -p $@

$(LIB_DIR):
	@cp -r ../../../lib/ $@

#---------------------------- CLEAN ------------------------------#
clean:
	@echo "Deleting \"solcmc/build/\"..."
	@rm -rf $(BUILD_DIR)
