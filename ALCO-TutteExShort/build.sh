#!/bin/bash

touch gitcommit

pdflatex ExtAlgNew.tex || exit

bibtex ExtAlgNew.aux || exit

cat > gitcommit <<EOF
\begin{verbatim}

EOF

git log -1 >> gitcommit

cat >> gitcommit <<EOF
\end{verbatim}

EOF

pdflatex ExtAlgNew.tex
pdflatex ExtAlgNew.tex






