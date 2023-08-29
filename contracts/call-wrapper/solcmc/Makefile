VERSIONS_DIR = ../versions/
PROPERTIES_DIR = .
BUILD_DIR = build/
CONTRACTS_DIR = build/contracts/
LOGS_DIR = build/logs/
PYTHON = python

$(CONTRACTS_DIR):
	mkdir -p $(CONTRACTS_DIR)

contracts: $(CONTRACTS_DIR)
	$(PYTHON) ../../../scripts/solcmc_contract_builder.py --version $(VERSIONS_DIR) --property $(PROPERTIES_DIR) --output $(CONTRACTS_DIR)

clean:
	rm -rf build/

