PDFLATEX ?= pdflatex

.PHONY: paper render
paper:
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex

render: paper
	mkdir -p qa
	pdftoppm -r 95 -png main.pdf qa/page
