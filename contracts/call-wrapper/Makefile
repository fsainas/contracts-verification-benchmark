SOLCMC_DIR = ./solcmc
SOLCMC_BUILD_DIR = $(SOLCMC_DIR)/build
SOLCMC_OUT = $(SOLCMC_BUILD_DIR)/out.csv
SOLCMC_CM = $(SOLCMC_BUILD_DIR)/cm.csv
CERTORA_DIR = ./certora
CERTORA_BUILD_DIR = $(CERTORA_DIR)/build
CERTORA_OUT = $(CERTORA_BUILD_DIR)/out.csv
CERTORA_CM = $(CERTORA_BUILD_DIR)/cm.csv

VERSIONS_DIR = ./versions
SKELETON = ./skeleton.json
GROUND_TRUTH = ./ground-truth.csv
README = README.md

PYTHON = python

all: plain verif
	$(PYTHON) ../../scripts/cm_gen.py --ground-truth $(GROUND_TRUTH) --results $(SOLCMC_OUT) > $(SOLCMC_CM)
	$(PYTHON) ../../scripts/cm_gen.py --ground-truth $(GROUND_TRUTH) --results $(CERTORA_OUT) > $(CERTORA_CM)
	echo "" >> $(README) 	# new line
	echo "### Experiments" >> $(README)
	echo "" >> $(README)
	echo "### SolCMC" >> $(README)
	$(PYTHON) ../../scripts/mdtable_gen.py --input $(SOLCMC_CM) >> $(README)
	echo "" >> $(README) 	
	echo "" >> $(README) 	
	echo "### Certora" >> $(README)
	$(PYTHON) ../../scripts/mdtable_gen.py --input $(CERTORA_CM) >> $(README)
	
plain: $(VERSIONS_DIR) $(SKELETON) $(GROUND_TRUTH)
	$(PYTHON) ../../scripts/readme_gen.py -d . > $(README)

verif:
	cd $(realpath $(SOLCMC_DIR)) && make
	cd $(realpath $(CERTORA_DIR)) && make
