PYTHON ?= python3

.PHONY: paper verify
paper:
	$(MAKE) -C paper paper

verify:
	$(PYTHON) scripts/verify.py
