TEMPLATE_DIR = ./template
CERTORA_DIR = certora
SOLCMC_DIR = solcmc

init:
ifdef name 
	@if [ -d "./$(name)" ]; \
	then echo "Use case dir already exists"; \
	else cp -r $(TEMPLATE_DIR) $(name); \
	echo "$(name) dir created."; \
	fi
else
	@echo "Error: specify a name"
	@echo "Usage: $ make init name=<use_case_name>"
endif

update:
	@for dir in $(wildcard */); do \
		if [ ./$$dir != $(TEMPLATE_DIR)/ ]; then \
			cp $(TEMPLATE_DIR)/Makefile "$$dir"; \
			echo cp $(TEMPLATE_DIR)/Makefile "$$dir"; \
			cp $(TEMPLATE_DIR)/certora/Makefile "$$dir"$(CERTORA_DIR); \
			echo cp $(TEMPLATE_DIR)/certora/Makefile "$$dir"$(CERTORA_DIR); \
			cp $(TEMPLATE_DIR)/solcmc/Makefile "$$dir"$(SOLCMC_DIR); \
			echo cp $(TEMPLATE_DIR)/solcmc/Makefile "$$dir"$(SOLCMC_DIR); \
		fi; \
    done

