# Directories
VERSIONS_DIR = ../versions/
PROPERTIES_DIR = .
BUILD_DIR = build
CONTRACTS_DIR = $(BUILD_DIR)/contracts
LOGS_DIR = $(BUILD_DIR)/logs
LIB_DIR = $(CONTRACTS_DIR)/lib

PYTHON = python

GETTER_FILE = getters.sol

.PHONY = run clean

#run: directories contracts 
#	$(PYTHON) ../../../scripts/run_solcmc.py --input $(CONTRACTS_DIR) --output $(BUILD_DIR)

directories: $(CONTRACTS_DIR) $(LOGS_DIR) $(LIB_DIR)

$(CONTRACTS_DIR):
	mkdir -p $@

$(LOGS_DIR):
	mkdir -p $@

$(LIB_DIR):
	cp -r ../../../lib/ $@

contracts: $(CONTRACTS_DIR)
	$(PYTHON) ../../../scripts/contract_builder.py --base $(VERSIONS_DIR) --inject $(GETTER_FILE) --output $(CONTRACTS_DIR)

clean:
	rm -rf build/

