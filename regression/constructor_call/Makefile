MAKEFLAGS = --no-print-directory

# CHANGE THIS PATHS
# Original contract path
CONTRACT = ./versions/
# Contract with solcmc instrumentation path
SOLCMC_CONTRACT = ./solcmc/generated
# Certora specifications path
CERTORA_SPEC = ./certora

SKELETON = ./skeleton.json
GROUND_TRUTH = ./ground-truth.csv
README = ./README.md
BUILD_DIR = ./build

# SOLCMC params
to = 10m
Z3_DIR = $(BUILD_DIR)/z3
Z3_OUT = $(Z3_DIR)/out.csv
Z3_CM = $(Z3_DIR)/cm.csv
Z3_TABLE = $(Z3_DIR)/table.md
Z3_LOGS = $(Z3_DIR)/logs
ELD_DIR = $(BUILD_DIR)/eld
ELD_OUT = $(ELD_DIR)/out.csv
ELD_CM = $(ELD_DIR)/cm.csv
ELD_TABLE = $(ELD_DIR)/table.md
ELD_LOGS = $(ELD_DIR)/logs

# Certora params
CERTORA_DIR = $(BUILD_DIR)/certora
CERTORA_OUT = $(CERTORA_DIR)/out.csv
CERTORA_CM = $(CERTORA_DIR)/cm.csv
CERTORA_TABLE = $(CERTORA_DIR)/table.md
CERTORA_LOGS = $(CERTORA_DIR)/logs

PYTHON = python3

.PHONY: all certora solcmc solcmc-contracts plain clean cleanr

all: plain solcmc certora
	@echo "Adding Solcmc table to README..."
	@echo "### SolCMC" >> $(README)
	@cat $(Z3_TABLE) >> $(README)
	@cat $(ELD_TABLE) >> $(README)
	@echo "" >> $(README)
	@echo "Adding Certora table to README..."
	@cat $(CERTORA_TABLE) >> $(README)

#---------------------------- CERTORA ----------------------------#
certora: $(CERTORA_TABLE)

$(CERTORA_TABLE): $(CERTORA_CM)
	@echo "Generating Certora results table ($(CERTORA_TABLE))..."
	@echo "### Certora" > $(CERTORA_TABLE)
	@$(PYTHON) ../../scripts/mdtable_gen.py --input $(CERTORA_CM) >> $(CERTORA_TABLE)

$(CERTORA_CM): $(GROUND_TRUTH) $(CERTORA_OUT) 
	@echo "Generating Certora confusion matrix ($(CERTORA_CM))..."
	@$(PYTHON) ../../scripts/cm_gen.py --ground-truth $(GROUND_TRUTH) --results $(CERTORA_OUT) > $(CERTORA_CM)

$(CERTORA_OUT): setup
	@echo "Running Certora experiments..."
	@$(PYTHON) ../../scripts/run_certora.py --contracts $(CONTRACT) --specs $(CERTORA_SPEC) --output $(CERTORA_DIR)

#---------------------------- SOLCMC -----------------------------#
solcmc: solcmc-contracts $(Z3_TABLE) $(ELD_TABLE)

solcmc-contracts:
	$(MAKE) -C solcmc build

# Solcmc with Z3
# Make markdown table
$(Z3_TABLE): $(Z3_CM)
	@echo "Generating SolCMC results table ($(Z3_TABLE))..."
	echo "#### Z3" > $(Z3_TABLE)
	@$(PYTHON) ../../scripts/mdtable_gen.py --input $(Z3_CM) >> $(Z3_TABLE)

# Build confusion matrix with ground truths
$(Z3_CM): $(GROUND_TRUTH) $(Z3_OUT)
	@echo "Generating Solcmc confusion matrix ($(Z3_CM))..."
	@$(PYTHON) ../../scripts/cm_gen.py --ground-truth $(GROUND_TRUTH) --results $(Z3_OUT) > $(Z3_CM)

# Run experiments
$(Z3_OUT): setup
	@echo "Running SolCMC ($(solver)) experiments..."
	@$(PYTHON) ../../scripts/run_solcmc.py --contracts $(SOLCMC_CONTRACT) --output $(Z3_DIR) --timeout $(to) --solver z3

# Solcmc with eldarica
# Make markdown table
$(ELD_TABLE): $(ELD_CM)
	@echo "Generating SolCMC results table ($(ELD_TABLE))..."
	echo "#### ELD" > $(ELD_TABLE)
	@$(PYTHON) ../../scripts/mdtable_gen.py --input $(ELD_CM) >> $(ELD_TABLE)

# Build confusion matrix with ground truths
$(ELD_CM): $(GROUND_TRUTH) $(ELD_OUT)
	@echo "Generating Solcmc confusion matrix ($(ELD_CM))..."
	@$(PYTHON) ../../scripts/cm_gen.py --ground-truth $(GROUND_TRUTH) --results $(ELD_OUT) > $(ELD_CM)

# Run experiments
$(ELD_OUT): setup
	@echo "Running SolCMC ($(solver)) experiments..."
	@$(PYTHON) ../../scripts/run_solcmc.py --contracts $(SOLCMC_CONTRACT) --output $(ELD_DIR) --timeout $(to) --solver eld

#---------------------------- SETUP ------------------------------#
setup: $(Z3_LOGS) $(ELD_LOGS) $(CERTORA_LOGS)

# Create build logs/ dirs, and build/ dirs with them
$(Z3_LOGS):
	@mkdir -p $@

$(ELD_LOGS):
	@mkdir -p $@

$(CERTORA_LOGS):
	@mkdir -p $@

#---------------------------- README -----------------------------#
plain: cleanr $(README)
	
# Create plain README, without experiments results
$(README): $(VERSIONS_DIR) $(SKELETON) $(GROUND_TRUTH)
	@echo "Generating plain README..."
	@$(PYTHON) ../../scripts/readme_gen.py -d . > $(README)
	@echo "## Experiments" >> $(README)

#---------------------------- CLEAN ------------------------------#
clean: cleanr
	@echo "Removing $(BUILD_DIR)..."
	@rm -rf $(BUILD_DIR)

# Remove README.md
cleanr:
	@echo "Removing README..."
	@rm -f $(README)