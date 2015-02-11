#!/bin/bash

pdflatex solve1.tex
bibtex solve1
pdflatex solve1.tex
pdflatex solve1.tex

