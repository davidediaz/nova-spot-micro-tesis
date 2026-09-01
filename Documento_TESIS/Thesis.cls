% This is class based on 'ECSthesis.cls' made by by Steve R. Gunn
% It was modified by: 	Jhon E. Navarrete Gómez
%						jhonnavarrete@usantotomas.edu.co

\NeedsTeXFormat{LaTeX2e}[1996/12/01]
\ProvidesClass{Thesis}
              [2007/22/02 v1.0
   LaTeX document class]
\def\baseclass{book}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{\baseclass}}
\def\@checkoptions#1#2{
	\edef\@curroptions{\@ptionlist{\@currname.\@currext}}
	\@tempswafalse
	\@tfor\@this:=#2\do{
		\@expandtwoargs\in@{,\@this,}{,\@curroptions,}
		\ifin@ \@tempswatrue \@break@tfor \fi}
	\let\@this\@empty
	\if@tempswa \else \PassOptionsToClass{#1}{\baseclass}\fi
}
\@checkoptions{11pt}{{10pt}{11pt}{12pt}}
\PassOptionsToClass{a4paper}{\baseclass}
\ProcessOptions\relax
\LoadClass{\baseclass}
\newcommand\bhrule{\typeout{------------------------------------------------------------------------------}}

% ---------------------------------------------------------------------
% ------------------------- Required Packages -------------------------
% ---------------------------------------------------------------------

\usepackage{vmargin}
	% Set various page dimensions
\setmarginsrb {2.5cm}	% Left margin
              {2.5cm}	% Top margin
              {2.5cm}	% Right margin
              {2.5cm}	% Bottom margin
              {20pt}	% Head height
              {0.8cm}	% Head sep
              {9pt}		% Foot height
              {0.8cm}	% Foot sep

\usepackage{fancyhdr}
	% The package provides extensive facilities, both for constructing headers and footers, and for controlling their use 
	\lhead[\rm\thepage]{\fancyplain{}{\sl{\rightmark}}}
	\rhead[\fancyplain{}{\sl{\leftmark}}]{\rm\thepage}
	\chead{}\lfoot{}\rfoot{}\cfoot{}
	\pagestyle{fancy}
	\renewcommand{\chaptermark}[1]{\btypeout{\thechapter\space #1}\markboth{\@chapapp\ \thechapter\ #1}{\@chapapp\ \thechapter\ #1}}
	\renewcommand{\sectionmark}[1]{}
	\renewcommand{\subsectionmark}[1]{}

\usepackage{amsmath,amsfonts,amssymb,amscd,amsthm,xspace}
	% AMS mathematical facilities for LaTeX
	% TeX fonts from the American Mathematical Society
	% AMS-LaTeX commutative diagrams
	% Typesetting theorems (AMS style)
	% Define commands that appear not to eat spaces

\usepackage{hyperref}
	% Without colours hyperlinks
\hypersetup{
    colorlinks=true,
    linkcolor=black,
    filecolor=black,      
    urlcolor=black,
}
\pdfstringdefDisableCommands{\let\\\space}

\usepackage{graphicx}
	% Required to include images
\graphicspath{{Figures/}{./}}
	% Specifies where to look for included images
	% Location of the graphics files
	
\usepackage{epstopdf}
	% Convert EPS to PDF using Ghostscript
	
\usepackage{booktabs} 
	% Required for better table rules
	
\usepackage{rotating}
	% Rotation tools, including rotated full-page floats

\usepackage{listings}
	% Typeset source code listings using LaTeX
	
\usepackage{caption} 
	% Required for customising the captions
\captionsetup{justification=centerlast,font=small,labelfont=sc,margin=50pt}

\usepackage[utf8]{inputenc} 
	% Required for inputting international characters
	
\usepackage[T1]{fontenc} 
	% Output font encoding for international characters

\usepackage{palatino} 
	% Use the Palatino font by default
	
\usepackage[table]{xcolor}	
	% The package starts from the basic facilities of the color package, and provides easy driver-independent access to several kinds of color tints, shades, tones, and mixes of arbitrary colors.
	
\usepackage[american,cuteinductors,RPvoltages]{circuitikz}
	% The package gets widely used by engineers for typesetting electronic circuits for articles and publications all over the world.

\usepackage{csquotes} 
	% Required to generate language-dependent quotes in the bibliography
	
\usepackage{ifthen}
	% Conditional commands in LaTeX documents

\usepackage{footnote}
	% The footnote package provides commands for handling footnotes rather more fluently than LaTeX manages. 
	
\usepackage{array}
	% An extended implementation of the array and tabular environments which extends the options for column formats, and provides "programmable" format specifications.

\usepackage{longtable}
	% Longtable allows you to write tables that continue to the next page. 
	
\usepackage{pgfgantt}
	% The package provides an environment for drawing Gantt charts that contain various elements (titles, bars, milestones, groups and links).
	
\usepackage[backend=biber, style=ieee, sorting=none]{biblatex} 
	% Use the biber backend with the authoryear citation style
	% Use biber %
\addbibresource{ProyectoGradoBib.bib} 
	% The filename of the bibliography

\usepackage[main=spanish,english]{babel}
% Multilingual support for Plain TeX or LaTeX
\usepackage{datetime}
% Change format of \today with commands for current time
 \def\today{\ifcase\month\or
    Enero\or Febrero\or Marzo\or Abril\or Mayo\or Junio\or
    Julio\or Agosto\or Septiembre\or Octubre\or Noviembre\or
    Diciembre\fi\space de\space\number\year}
    
\usepackage{setspace}

\usepackage{chngcntr}
\counterwithout{figure}{chapter}
\counterwithout{table}{chapter}
	% Change the resetting of counters

% Spanish Section
\renewcommand{\contentsname}{Contenido}
\renewcommand{\chaptername}{Capítulo}

\renewcommand{\indexname}{Índice}
\renewcommand{\listfigurename}{Lista de Figuras}
\renewcommand{\listtablename}{Lista de Figuras}

\renewcommand{\figurename}{Figura}
\renewcommand{\tablename}{Tabla}

\renewcommand{\bibname}{Bibliografía}
	
% ---------------------------------------------------------------------
% ----------------------- General Configuration -----------------------
% ---------------------------------------------------------------------

\onehalfspacing
\setlength{\parindent}{0pt}
\setlength{\parskip}{2.0ex plus0.5ex minus0.2ex}

\raggedbottom
\setlength{\topskip}{1\topskip \@plus 5\p@}
\doublehyphendemerits=10000       
	% No consecutive line hyphens.
\brokenpenalty=10000              
	% No broken words across columns/pages.
\widowpenalty=9999                
	% Almost no widows at bottom of page.
\clubpenalty=9999                 
	% Almost no orphans at top of page.
\interfootnotelinepenalty=9999    
	% Almost never break footnotes.

% ---------------------------------------------------------------------
% ------------------------- General Definitions -----------------------
% ---------------------------------------------------------------------
\newcommand*{\ProyectodeGrado}[1]{\def\ProjectName{#1}}

\newcommand*{\director}[1]{\def\dirname{#1}}
\newcommand*{\codirector}[1]{\def\codirname{#1}}
\newcommand*{\degree}[1]{\def\degreename{#1}}
\newcommand*{\authors}[1]{\def\authornames{#1}}
\newcommand*{\addresses}[1]{\def\addressnames{#1}}
\newcommand*{\university}[1]{\def\univname{#1}}

\newcommand*{\department}[1]{\def\deptname{#1}}
\newcommand*{\group}[1]{\def\groupname{#1}}
\newcommand*{\faculty}[1]{\def\facname{#1}}

\newcommand*{\subject}[1]{\def\subjectname{#1}}
\newcommand*{\keywords}[1]{\def\keywordnames{#1}}
\director{}
\degree{}
\authors{}

\university{\texorpdfstring{\href{https://www.usta.edu.co/}%
{\textbf{\Huge{U}\LARGE{NIVERSIDAD} \Huge{S}\LARGE{ANTO} \Huge{T}\LARGE{OMÁS}}}}{University Name}}

\department{División de Ingenierías}

\faculty{\texorpdfstring{\href{https://facultadingenieriaelectronica.usta.edu.co/index.php/nuestros-programas/pregrado-en-ingenieria-electronica}%
{Facultad de Ingeniería Electrónica}}{Faculty Name}}
                
\addresses{}
\subject{}
\keywords{}

%\newcommand\Declaration[1]{
%\btypeout{Declaration of Authorship}
%\addtotoc{Declaration of Authorship}
%\thispagestyle{plain}
%\null\vfil
%%\vskip 60\p@
%\begin{center}{\huge\bf Declaration of Authorship\par}\end{center}
%%\vskip 60\p@
%{\normalsize #1}
%\vfil\vfil\null
%%\cleardoublepage
%}

\newcommand\btypeout[1]{\bhrule\typeout{\space #1}\bhrule}

\def\cleardoublepage{\clearpage\if@twoside \ifodd\c@page\else
\hbox{}

\thispagestyle{empty}
\newpage
\if@twocolumn\hbox{}\newpage\fi\fi\fi}

\theoremstyle{plain}
\newtheorem{example}{Example}[chapter]
\newtheorem{theorem}{Theorem}[chapter]
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{axiom}[theorem]{Axiom}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

\newcommand{\fref}[1]{Figure~\ref{#1}}
\newcommand{\tref}[1]{Table~\ref{#1}}
\newcommand{\eref}[1]{Equation~\ref{#1}}
\newcommand{\cref}[1]{Chapter~\ref{#1}}
\newcommand{\sref}[1]{Section~\ref{#1}}
\newcommand{\aref}[1]{Appendix~\ref{#1}}
\renewcommand{\topfraction}{0.85}
\renewcommand{\bottomfraction}{.85}
\renewcommand{\textfraction}{0.1}
\renewcommand{\dbltopfraction}{.85}
\renewcommand{\floatpagefraction}{0.75}
\renewcommand{\dblfloatpagefraction}{.75}
\setcounter{topnumber}{9}
\setcounter{bottomnumber}{9}
\setcounter{totalnumber}{20}
\setcounter{dbltopnumber}{9}

\lstset{captionpos=b,
        frame=tb,
        basicstyle=\scriptsize\ttfamily,
        showstringspaces=false,
        keepspaces=true}
\lstdefinestyle{matlab} {
        language=Matlab,
        keywordstyle=\color{blue},
        commentstyle=\color[rgb]{0.13,0.55,0.13}\em,
        stringstyle=\color[rgb]{0.7,0,0} }

% ---------------------------------------------------------------------
% ---------------------- Make Title / Cover Page ----------------------
% ---------------------------------------------------------------------
\renewcommand\maketitle{
	\btypeout{Title Page}
	\hypersetup{pdftitle={\@title}}
	\hypersetup{pdfsubject=\subjectname}
	\hypersetup{pdfauthor=\authornames}
	\hypersetup{pdfkeywords=\keywordnames}
	\thispagestyle{empty}
	
	\begin{titlepage}
		\vspace*{-2cm}
	    \let\footnotesize\small
	    \let\footnoterule\relax
	    \let \footnote \thanks
	    \setcounter{footnote}{0}
	    \null\vfil
% ----- Cover Page -----
    	\begin{center}  		
			\setlength{\parskip}{0pt}
			{\large\textbf{\univname}\par}
			\vfill
			\rule{\textwidth}{.1pt}
			{\Large \bf \@title \par}
			\rule{\textwidth}{.1pt}
			\vfill
			\vspace{1cm}
			{\large Realizado por \par}
			\smallskip
			{\LARGE \authornames \par}
			\vspace{1cm}
			\vfill
			\ifthenelse{\equal{\ProjectName}{I}}%
			{\large{Anteproyecto enviado en cumplimiento del requisito parcial \par para optar por el grado de Ingeniería Electrónica}}%
			{\large{Proyecto de Grado presentado en cumplimiento del requisito \par para optar por el grado de Ingeniería Electrónica}}
			\vfill
			\includegraphics[width=0.7\textwidth]{./Cover Page/Escudos.pdf}
			\vfill
			\ifthenelse{\equal{\groupname}{MEM}}%
			{\texorpdfstring{\href{https://facultadingenieriaelectronica.usta.edu.co/index.php/investigacion-pregrado1}{Grupo de Investigación MEM (Modelado-Electrónica-Monitoreo)}}{Research Group Name}}%
			{\texorpdfstring{\href{https://facultadingenieriaelectronica.usta.edu.co/index.php/investigacion-pregrado1}{Grupo de Investigación GED (Grupo de Estudio y Desarrollo en Robótica)}}{Research Group Name}\par Grupo de Investigación MEM (Modelado-Electrónica-Monitoreo)\par}
%			{\large \groupname \par}
			{\large \facname \par}
			{\large \deptname \par}
			\bigskip
			\bigskip
			\bigskip
			{\Large \@date \par}
			\bigskip
    	\end{center}
		\par
		\@thanks
		\vfil\null
		
		% Back-Cover Page -------------------------------
		\newpage
		\thispagestyle{empty}
		\vspace*{-2cm}
		\let\footnotesize\small
		\let\footnoterule\relax
		\let \footnote \thanks
		\setcounter{footnote}{0}
		\null\vfil
		\begin{center}
			\setlength{\parskip}{0pt}
			\rule{\textwidth}{.1pt}
			{\LARGE \bf \@title \par}
			\rule{\textwidth}{.1pt}
			\vfill
			\vspace{0.5cm}
			{\large Realizado por \par}
			\smallskip
			{\LARGE \authornames \par}
			\vspace{1cm}
			\vfill
			\ifthenelse{\equal{\ProjectName}{I}}%
			{\large{Anteproyecto enviado en cumplimiento del requisito parcial \par para optar por el grado de Ingeniería Electrónica}}%
			{\large{Proyecto de Grado presentado en cumplimiento del requisito \par para optar por el grado de Ingeniería Electrónica}}
			\vfill
			\vspace{1cm}
			{\large Dirigido por\par}
			{\LARGE \dirname \par} 
			\vfill
			\vspace{0.5cm}
			\ifdefined\codirname
				{\large Codirigido por\par}%
				{\LARGE \codirname \par}
				\vfill
				\vspace{1cm}
			\fi
			\vfill
			\ifthenelse{\equal{\groupname}{MEM}}%
			{\texorpdfstring{\href{https://facultadingenieriaelectronica.usta.edu.co/index.php/investigacion-pregrado1}{Grupo de Investigación MEM (Modelado-Electrónica-Monitoreo)}}{Research Group MEM}\par}%
			{\texorpdfstring{\href{https://facultadingenieriaelectronica.usta.edu.co/index.php/investigacion-pregrado1}{Grupo de Investigación GED (Grupo de Estudio y Desarrollo en Robótica)}}{Research Group Name}\par Grupo de Investigación MEM (Modelado-Electrónica-Monitoreo)\par}
%			{\large \groupname \par}
			{\large \facname \par}
			{\large \deptname \par}
			\bigskip
			\bigskip
			\bigskip
			{\Large \@date \par}
			\bigskip
		\end{center}
		\par
		\@thanks
		\vfil\null
	\end{titlepage}
	\setcounter{footnote}{0}%
	\global\let\thanks\relax
	\global\let\maketitle\relax
	\global\let\@thanks\@empty
	\global\let\@author\@empty
	\global\let\@date\@empty
	\global\let\@title\@empty
	\global\let\title\relax
	\global\let\author\relax
	\global\let\date\relax
	\global\let\and\relax
	\cleardoublepage
}

% ---------------------------------------------------------------------
% ------------------------------ Abstract -----------------------------
% ---------------------------------------------------------------------

\newenvironment{abstract}
{
  \btypeout{Abstract Page}
  \thispagestyle{empty}
  \null\vfil
  \begin{center}
    \setlength{\parskip}{0pt}
    {\normalsize \UNIVNAME \par}
    \bigskip
    {\huge{\textit{Abstract}} \par}
    \bigskip
    {\normalsize \facname \par}
    {\normalsize \deptname \par}
    \bigskip
    {\normalsize Doctor of Philosophy\par}
    \bigskip
    {\normalsize\bf \@title \par}
    \medskip
    {\normalsize by \authornames \par}
    \bigskip
  \end{center}
}
{
  \vfil\vfil\vfil\null
  \cleardoublepage
}
\addtocounter{secnumdepth}{1}
\setcounter{tocdepth}{6}
\newcounter{dummy}
\newcommand\addtotoc[1]{
\refstepcounter{dummy}
\addcontentsline{toc}{chapter}{#1}}
\renewcommand\tableofcontents{
\btypeout{Table of Contents}
\begin{spacing}{1}{
    \setlength{\parskip}{1pt}
    \if@twocolumn
      \@restonecoltrue\onecolumn
    \else
      \@restonecolfalse
    \fi
    \chapter*{\contentsname
        \@mkboth{
           \MakeUppercase\contentsname}{\MakeUppercase\contentsname}}
    \@starttoc{toc}
    \if@restonecol\twocolumn\fi
   \cleardoublepage
}\end{spacing}
}
\renewcommand\listoffigures{
\btypeout{List of Figures}
\addtotoc{List of Figures}
\begin{spacing}{1}{
    \setlength{\parskip}{1pt}
    \if@twocolumn
      \@restonecoltrue\onecolumn
    \else
      \@restonecolfalse
    \fi
    \chapter*{\listfigurename
      \@mkboth{\MakeUppercase\listfigurename}
              {\MakeUppercase\listfigurename}}
    \@starttoc{lof}
    \if@restonecol\twocolumn\fi
    \cleardoublepage
}\end{spacing}
}
\renewcommand\listoftables{
\btypeout{List of Tables}
\addtotoc{List of Tables}
\begin{spacing}{1}{
    \setlength{\parskip}{1pt}
    \if@twocolumn
      \@restonecoltrue\onecolumn
    \else
      \@restonecolfalse
    \fi
    \chapter*{\listtablename
      \@mkboth{
          \MakeUppercase\listtablename}{\MakeUppercase\listtablename}}
    \@starttoc{lot}
    \if@restonecol\twocolumn\fi
    \cleardoublepage
}\end{spacing}
}
\newcommand\listsymbolname{Abbreviations}
\usepackage{longtable}
\newcommand\listofsymbols[2]{
\btypeout{\listsymbolname}
\addtotoc{\listsymbolname}
    \chapter*{\listsymbolname
      \@mkboth{
          \MakeUppercase\listsymbolname}{\MakeUppercase\listsymbolname}}
\begin{longtable}[c]{#1}#2\end{longtable}\par
    \cleardoublepage
}
\newcommand\listconstants{Physical Constants}
\usepackage{longtable}
\newcommand\listofconstants[2]{
\btypeout{\listconstants}
\addtotoc{\listconstants}
    \chapter*{\listconstants
      \@mkboth{
          \MakeUppercase\listconstants}{\MakeUppercase\listconstants}}
\begin{longtable}[c]{#1}#2\end{longtable}\par
    \cleardoublepage
}
\newcommand\listnomenclature{Symbols}
\usepackage{longtable}
\newcommand\listofnomenclature[2]{
\btypeout{\listnomenclature}
\addtotoc{\listnomenclature}
    \chapter*{\listnomenclature
      \@mkboth{
          \MakeUppercase\listnomenclature}{\MakeUppercase\listnomenclature}}
\begin{longtable}[c]{#1}#2\end{longtable}\par
    \cleardoublepage
}
\newcommand\acknowledgements[1]{
\btypeout{Acknowledgements}
\addtotoc{Acknowledgements}
\thispagestyle{plain}
\begin{center}{\huge{\textit{Acknowledgements}} \par}\end{center}
{\normalsize #1}
\vfil\vfil\null

}
\newcommand\dedicatory[1]{
\btypeout{Dedicatory}
\thispagestyle{plain}
\null\vfil
\vskip 60\p@
\begin{center}{\Large \sl #1}\end{center}
\vfil\null
\cleardoublepage
}

\renewcommand\backmatter{
  \if@openright
    \cleardoublepage
  \else
    \clearpage
  \fi
%  \addtotoc{\bibname}
%  \btypeout{\bibname}
  \@mainmatterfalse}
\endinput
%%
%% End of file `Thesis.cls'.
