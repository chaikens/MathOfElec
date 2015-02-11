#!/bin/bash

pdflatex solve1.tex
bibtex solve1
pdflatex solve1.tex
pdflatex solve1.tex


pdflatex laplace1.tex
bibtex laplace1
pdflatex laplace1
pdflatex laplace1

