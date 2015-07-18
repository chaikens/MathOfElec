#!/bin/bash
FILE=PosterJul2015
pdflatex $FILE
bibtex $FILE
pdflatex $FILE
pdflatex $FILE


