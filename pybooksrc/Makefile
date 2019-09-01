.SUFFIXES= .lyx .tex .pdf
DESTDIR=

all: mapy.pdf

clean:
	rm -f *~ *.tex *.aux *.log *.pdf *.toc pics/*.eps

install:

%.tex: %.lyx
	tmpHome=$$(mktemp -d); \
	HOME=$${tmpHome} lyx --export latex $<; \
	rm -rf $${tmpHome}

%.pdf: %.tex
	pdflatex $<
	logfile=$$(echo $< | sed 's/tex/log/'); \
	while (grep  Warning $${logfile}| grep -iq run); do \
	  pdflatex $<; \
	done
