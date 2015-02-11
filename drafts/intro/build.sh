#!/bin/bash

pdflatex intro1.tex
bibtex intro1
pdflatex intro1.tex
pdflatex intro1.tex

