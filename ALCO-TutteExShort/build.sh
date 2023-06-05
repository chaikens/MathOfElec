#!/bin/bash

touch gitcommit

pdflatex ExtAlgTFLMatPairs.tex || exit

bibtex ExtAlgTFLMatPairs.aux || exit

cat > gitcommit <<EOF
\begin{verbatim}

EOF

git log -1 >> gitcommit

cat >> gitcommit <<EOF
\end{verbatim}

EOF

pdflatex ExtAlgTFLMatPairs.tex
pdflatex ExtAlgTFLMatPairs.tex





