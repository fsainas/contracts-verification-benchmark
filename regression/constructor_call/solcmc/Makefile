# ─── Paths ───────────────────────────────────────────────────────────
PYTHON          := python3
VERSIONS_DIR    := ../versions        # PaymentSplitter_v*.sol originali
PROPERTIES_DIR  := .                  # i file *.sol con le proprietà CVL
CONTRACTS_DIR   := generated          # output finale

.PHONY: build clean
.DEFAULT_GOAL := build

# ─── Regole ──────────────────────────────────────────────────────────
# 1. assicura che la cartella di output esista
$(CONTRACTS_DIR):
	@mkdir -p $@

# 2. esegue “clean” PRIMA di compilare tutti i (version, property)
#    (lo script crea i file, quindi basta fare ‘touch’ su CONTRACTS_DIR )
build: clean $(CONTRACTS_DIR)
	@echo "▶ running builder.py …"
	@$(PYTHON) ../../../scripts/builder.py \
	    --versions   $(VERSIONS_DIR) \
	    --properties $(PROPERTIES_DIR) \
	    --output     $(CONTRACTS_DIR)
	@echo "✔  files written to $(CONTRACTS_DIR)/"

# 3. pulizia
clean:
	@rm -rf $(CONTRACTS_DIR)