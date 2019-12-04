CAD.pdf: CAD.tex Makefile *.tex ../Common/*.tex ../Common/*.bib
	pdflatex $(@:%.pdf=%)
	bibtex $(@:%.pdf=%)
	pdflatex $(@:%.pdf=%)
	pdflatex $(@:%.pdf=%)
	pdflatex $(@:%.pdf=%)

clean:
	rm -f *.log *.blg *.bbl *.aux *.dvi *.out *.toc

clean-all: clean
	rm -f CAD.pdf

