# Directories
VERSIONS_DIR = ../versions/
PROPERTIES_DIR = .
BUILD_DIR = build
CONTRACTS_DIR = $(BUILD_DIR)/contracts
LOGS_DIR = $(BUILD_DIR)/logs
LIB_DIR = $(CONTRACTS_DIR)/lib

to = 0
contract = ""

PYTHON = python

.PHONY = run clean

run: contracts directories
	@$(PYTHON) ../../../scripts/run_solcmc.py --contracts $(CONTRACTS_DIR) --output $(BUILD_DIR) --timeout $(to)

one: contracts directories
	@$(PYTHON) ../../../scripts/runs.py --contract $(contract) --timeout $(to)

contracts: $(CONTRACTS_DIR)
	@$(PYTHON) ../../../scripts/builder.py --versions $(VERSIONS_DIR) --properties $(PROPERTIES_DIR) --output $(CONTRACTS_DIR)

directories: $(CONTRACTS_DIR) $(LOGS_DIR) $(LIB_DIR)

$(CONTRACTS_DIR):
	@mkdir -p $@

$(LOGS_DIR):
	@mkdir -p $@

$(LIB_DIR):
	@cp -r ../../../lib/ $@

clean:
	rm -rf build/

