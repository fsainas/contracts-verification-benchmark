SHELL := /bin/bash

.PHONY: init test clean 

default: test

init:
	@if [ -f hardhat.config.js ]; then \
		echo "Skipping: Hardhat already initialized."; \
	else \
		echo "Initializing Hardhat project..."; \
		npm init -y >/dev/null && \
		npm install --save-dev hardhat --silent --no-progress >/dev/null && \
		printf '3\n' | npx hardhat init  && \
		npm install --save-dev @nomicfoundation/hardhat-toolbox --silent --no-progress >/dev/null && \
		if ! grep -q '@nomicfoundation/hardhat-toolbox' hardhat.config.js; then \
			sed -i '1irequire("@nomicfoundation/hardhat-toolbox")\n' hardhat.config.js; \
		fi; \
		echo "Done."; \
	fi

test: init
	npx hardhat test


clean:
	@echo "Cleaning project (preserving Makefile, contracts/, and test/)..."
	@find . -mindepth 1 -maxdepth 1 \
		! -name 'Makefile' \
		! -name 'contracts' \
		! -name 'test' \
		-exec rm -rf {} +
	@echo "Clean complete."
