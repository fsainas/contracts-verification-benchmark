SOLCMC_DIR = ./solcmc
SOLCMC_BUILD_DIR = $(SOLCMC_DIR)/build
SOLCMC_Z3_TABLE = $(SOLCMC_BUILD_DIR)/z3/table.md
SOLCMC_ELD_TABLE = $(SOLCMC_BUILD_DIR)/eld/table.md

CERTORA_DIR = ./certora
CERTORA_BUILD_DIR = $(CERTORA_DIR)/build
CERTORA_TABLE = $(CERTORA_BUILD_DIR)/table.md

VERSIONS_DIR = ./versions
SKELETON = ./skeleton.json
GROUND_TRUTH = ./ground-truth.csv
README = README.md

PYTHON = python

.PHONY: all certora solcmc plain clean cleanr clean-solcmc clean-certora

all: plain solcmc certora
	@echo "Adding Solcmc table to README..."
	@echo "### SolCMC" >> $(README)
	@cat $(SOLCMC_Z3_TABLE) >> $(README)
	@cat $(SOLCMC_ELD_TABLE) >> $(README)
	@echo "" >> $(README)
	@echo "Adding Certora table to README..."
	@cat $(CERTORA_TABLE) >> $(README)

#---------------------------- CERTORA ----------------------------#
certora: $(CERTORA_TABLE)

$(CERTORA_TABLE):
	@cd $(realpath $(CERTORA_DIR)) && make

#---------------------------- SOLCMC -----------------------------#
solcmc: $(SOLCMC_Z3_TABLE) $(SOLCMC_ELD_TABLE)

$(SOLCMC_Z3_TABLE):
	@cd $(realpath $(SOLCMC_DIR)) && make solver=z3

$(SOLCMC_ELD_TABLE):
	@cd $(realpath $(SOLCMC_DIR)) && make solver=eld

#---------------------------- README -----------------------------#
plain: cleanr $(README)
	
$(README): $(VERSIONS_DIR) $(SKELETON) $(GROUND_TRUTH)
	@echo "Generating plain README..."
	@$(PYTHON) ../../scripts/readme_gen.py -d . > $(README)
	@echo "## Experiments" >> $(README)

#---------------------------- CLEAN ------------------------------#
clean: cleanr clean-solcmc clean-certora

cleanr:
	rm -f $(README)

clean-solcmc:
	cd $(realpath $(SOLCMC_DIR)) && make clean

clean-certora:
	cd $(realpath $(CERTORA_DIR)) && make clean
