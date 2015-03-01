#!/bin/bash

latex OMPEMech.tex
bibtex OMPEMech
latex OMPEMech.tex
latex OMPEMech.tex

dvips OMPEMech
ps2pdf OMPEMech.ps OMPEMech.pdf

