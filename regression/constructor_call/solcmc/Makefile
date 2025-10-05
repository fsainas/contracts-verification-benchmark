PYTHON          := python3
VERSIONS_DIR    := ../versions
PROPERTIES_DIR  := .
CONTRACTS_DIR   := generated

.PHONY: build clean
.DEFAULT_GOAL := build

$(CONTRACTS_DIR):
	@mkdir -p $@

build: clean $(CONTRACTS_DIR)
	@echo "> running builder.py …"
	@$(PYTHON) ../../../scripts/builder.py \
	    --versions   $(VERSIONS_DIR) \
	    --properties $(PROPERTIES_DIR) \
	    --output     $(CONTRACTS_DIR)
	@echo "files written to $(CONTRACTS_DIR)/"

clean:
	@rm -rf $(CONTRACTS_DIR)