#! /bin/sh -v
latex TutteEx
bibtex TutteEx
latex TutteEx
latex TutteEx
dvips -t Letter -o TutteEx.ps TutteEx
ps2pdf TutteEx.ps TutteEx.pdf
