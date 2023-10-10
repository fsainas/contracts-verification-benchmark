TEMPLATE_DIR = ./template

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
