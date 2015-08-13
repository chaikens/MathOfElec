#!/bin/bash
FILE=Lines15
pdflatex $FILE
bibtex $FILE
pdflatex $FILE
pdflatex $FILE


