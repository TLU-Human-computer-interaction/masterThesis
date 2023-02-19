\NeedsTeXFormat{LaTeX2e}

% the name of the new class I created
\ProvidesClass{master_thesis}[2023/01/01 TLU Master Thesis]

% Load an existing class as the base
\LoadClass[12pt, a4paper]{article}

\setlength{\parindent}{0cm}

\RequirePackage[left=20mm, right=20mm, top=25mm, bottom=25mm]{geometry}
\RequirePackage{ifthen}

\RequirePackage[]{times}
\RequirePackage{graphicx}

\RequirePackage[english]{babel}

\RequirePackage{subfiles} % Best loaded last in the preamble


% BIBLIOGRAPHY

%  Use biblatex for references - change style= as appropriate

% needed to switch to backend=bibtex and then back to biber
% \RequirePackage[natbib=true,backend=bibtex,sorting=nyt,style=apa]{biblatex}

% use this to see all they keys
% \RequirePackage[natbib=true,backend=biber,style=draft]{biblatex}
\RequirePackage[natbib=true,backend=biber,style=apa, labeldate=year, urldate=short]{biblatex}
\renewcommand*{\bibfont}{\fontsize{10}{12}\selectfont}
% add your references to this file
\addbibresource{refs.bib}


% CUSTOM COMMANDS

% custom command for listing research questions
\newcounter{questionCounter}
\newenvironment{RQlist}
{\begin{list}
	{\textbf{RQ\arabic{questionCounter}:}}
	{\usecounter{questionCounter}}
}
{\end{list}}

% custom command for todo items
\newenvironment{todo}
{\\ \\ \textbf{TODO:}\begin{list}}
{\end{list}}