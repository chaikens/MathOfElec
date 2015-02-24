#!/bin/bash
FILE=Mar2015Talk
pdflatex $FILE
bibtex $FILE
pdflatex $FILE
pdflatex $FILE


