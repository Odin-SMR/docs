L2_DATA.pdf: L2_DATA.tex Makefile *.tex ../Common/*.tex ../Common/*.bib
	pdflatex $(@:%.pdf=%)
	bibtex $(@:%.pdf=%)
	pdflatex $(@:%.pdf=%)
	pdflatex $(@:%.pdf=%)
	pdflatex $(@:%.pdf=%)

clean:
	rm -f *.log *.blg *.bbl *.aux *.dvi *.out *.toc

clean-all: clean
	rm -f L2_DATA.pdf 

