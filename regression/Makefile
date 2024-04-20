TEMPLATE_DIR = ./template

PYTHON = python

target = ""

.PHONY: scores init update update-all

scores:
	@$(PYTHON) ../scripts/score.py -d . -o .

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
	cp $(TEMPLATE_DIR)/Makefile $(target)

update-all:
	@for dir in $(wildcard */); do \
		if [ ./$$dir != $(TEMPLATE_DIR)/ ]; then \
			cp $(TEMPLATE_DIR)/Makefile "$$dir"; \
			echo cp $(TEMPLATE_DIR)/Makefile "$$dir"; \
		fi; \
    done

