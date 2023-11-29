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

all: cleanr solcmc certora

certora: $(README)
	cd $(realpath $(CERTORA_DIR)) && make
	$(PYTHON) ../../scripts/cm_gen.py --ground-truth $(GROUND_TRUTH) --results $(CERTORA_OUT) > $(CERTORA_CM)
	echo "" >> $(README) 	
	echo "### Certora" >> $(README)
	$(PYTHON) ../../scripts/mdtable_gen.py --input $(CERTORA_CM) >> $(README)

solcmc: $(README)
	cd $(realpath $(SOLCMC_DIR)) && make
	$(PYTHON) ../../scripts/cm_gen.py --ground-truth $(GROUND_TRUTH) --results $(SOLCMC_OUT) > $(SOLCMC_CM)
	echo "" >> $(README)
	echo "### SolCMC" >> $(README)
	$(PYTHON) ../../scripts/mdtable_gen.py --input $(SOLCMC_CM) >> $(README)
	echo "" >> $(README) 	

plain: $(README)
	
$(README): $(VERSIONS_DIR) $(SKELETON) $(GROUND_TRUTH)
	$(PYTHON) ../../scripts/readme_gen.py -d . > $(README)
	echo "" >> $(README) 	# new line
	echo "## Experiments" >> $(README)

cleanr:
	rm -f $(README)

clean:
	cd $(realpath $(SOLCMC_DIR)) && make clean
	cd $(realpath $(CERTORA_DIR)) && make clean
