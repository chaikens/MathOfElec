#!/bin/bash

latex TutteEx.tex
latex TutteEx.tex
latex TutteEx.tex
dvips TutteEx.dvi
ps2pdf TutteEx.ps TutteEx.pdf
