#!/bin/bash

PROJ="SmithMay23"


pdflatex $PROJ.tex
bibtex $PROJ
pdflatex $PROJ.tex
pdflatex $PROJ.tex

