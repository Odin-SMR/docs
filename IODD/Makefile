IODD.pdf: IODD.tex Makefile *.tex ../Common/*.tex ../Common/*.bib q_fields.pdf
	pdflatex $(@:%.pdf=%)
	bibtex $(@:%.pdf=%)
	pdflatex $(@:%.pdf=%)
	pdflatex $(@:%.pdf=%)
	pdflatex $(@:%.pdf=%)

q_fields.pdf: q_fields.rst
	rst2pdf q_fields.rst q_fields.pdf

clean:
	rm -f *.log *.blg *.bbl *.aux *.dvi *.out *.toc

clean-all: clean
	rm -f IODD.pdf 

