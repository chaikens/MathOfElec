

\ProvidesClass{amsproc-sunycstr}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{amsproc}}
\ProcessOptions
\LoadClass{amsproc}

\def\serieslogo@{\vtop to 0pt{%
  \parindent\z@ \fontsize{6}{7\p@}\selectfont
        University at Albany Computer Science Technical Report\newline
	Volume {\bfseries\currentvolume}, \currentyear\endgraf}}

\def\ISSN{0000-0000}
\endinput
