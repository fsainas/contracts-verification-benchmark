SOLCMC_DIR = ./solcmc
SOLCMC_BUILD_DIR = $(SOLCMC_DIR)/build
SOLCMC_OUT = $(SOLCMC_BUILD_DIR)/out.csv
SOLCMC_CM = $(SOLCMC_BUILD_DIR)/cm.csv
SOLCMC_TABLE = $(SOLCMC_BUILD_DIR)/table.md
CERTORA_DIR = ./certora
CERTORA_BUILD_DIR = $(CERTORA_DIR)/build
CERTORA_OUT = $(CERTORA_BUILD_DIR)/out.csv
CERTORA_CM = $(CERTORA_BUILD_DIR)/cm.csv
CERTORA_TABLE = $(CERTORA_BUILD_DIR)/table.md

VERSIONS_DIR = ./versions
SKELETON = ./skeleton.json
GROUND_TRUTH = ./ground-truth.csv
README = README.md

PYTHON = python

all: plain solcmc certora
	@echo "Adding Solcmc table to README..."
	@cat $(SOLCMC_TABLE) >> $(README)
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

$(CERTORA_OUT): $(wildcard $(CERTORA_DIR)/*.spec) $(wildcard $(CERTORA_DIR)/*.sol) $(wildcard $(VERSIONS_DIR)/*.sol)
	@echo "Running Certora experiments..."
	@cd $(realpath $(CERTORA_DIR)) && make

#---------------------------- SOLCMC ----------------------------#
solcmc: $(SOLCMC_TABLE)

$(SOLCMC_TABLE): $(SOLCMC_CM)
	@echo "Generating Solcmc results table ($(SOLCMC_TABLE))..."
	@echo "### SolCMC" > $(SOLCMC_TABLE)
	@$(PYTHON) ../../scripts/mdtable_gen.py --input $(SOLCMC_CM) >> $(SOLCMC_TABLE)

$(SOLCMC_CM): $(GROUND_TRUTH) $(SOLCMC_OUT)
	@echo "Generating Solcmc confusion matrix ($(SOLCMC_CM))..."
	@$(PYTHON) ../../scripts/cm_gen.py --ground-truth $(GROUND_TRUTH) --results $(SOLCMC_OUT) > $(SOLCMC_CM)

$(SOLCMC_OUT): $(wildcard $(SOLCMC_DIR)/*.sol) $(wildcard $(VERSIONS_DIR)/*.sol)
	@echo "Running Solcmc experiments..."
	@cd $(realpath $(SOLCMC_DIR)) && make

#---------------------------- README ----------------------------#
plain: cleanr $(README)
	
$(README): $(VERSIONS_DIR) $(SKELETON) $(GROUND_TRUTH)
	@echo "Generating plain README..."
	@$(PYTHON) ../../scripts/readme_gen.py -d . > $(README)
	@echo "## Experiments" >> $(README)

#---------------------------- CLEAN ----------------------------#
cleanr:
	rm -f $(README)

clean:
	cd $(realpath $(SOLCMC_DIR)) && make clean
	cd $(realpath $(CERTORA_DIR)) && make clean