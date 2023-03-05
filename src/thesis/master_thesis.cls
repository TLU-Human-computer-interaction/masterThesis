\NeedsTeXFormat{LaTeX2e}

% the name of the new class I created
\ProvidesClass{master_thesis}[2023/01/01 TLU Master Thesis]

% Load an existing class as the base
\LoadClass[12pt, a4paper]{article}

\setlength{\parindent}{0cm}
% Margins. Upper and lower margins should be 2,5 cm, the right margin 2 cm and the left
% margin 3,5 cm to allow appropriate binding.
\RequirePackage[left=35mm, right=20mm, top=25mm, bottom=25mm]{geometry}
% \RequirePackage{ifthen}
\RequirePackage{parskip}

% Form images
\RequirePackage{graphicx}
\RequirePackage{float}

\RequirePackage[english]{babel}
\RequirePackage{csquotes}

% embed jpeg png
\RequirePackage{graphicx}

% this will make table of contents hypelinks and will allow to use hyperlinks in refs
\usepackage[]{hyperref}
    \hypersetup{hidelinks}

% BIBLIOGRAPHY

%  Use biblatex for references - change style= as appropriate

% needed to switch to backend=bibtex and then back to biber
% \RequirePackage[natbib=true,backend=bibtex,sorting=nyt,style=apa]{biblatex}

% use this to see all they keys
% \RequirePackage[natbib=true,backend=biber,style=draft]{biblatex}
\RequirePackage[natbib=true,backend=biber,style=apa, labeldate=year, urldate=short]{biblatex}
\renewcommand*{\bibfont}{\fontsize{10}{12}\selectfont}
% References file in in main file to enable intellisense in VS code
% \addbibresource{refs.bib}

% Formatting
% Font. The preferred font is Times New Roman, 12 points, with 1,5 spacing.
\RequirePackage[]{times}
% line spacing to 1.5
\RequirePackage{setspace}
\onehalfspacing
% rename Contents title
\addto{\captionsenglish}{\renewcommand*{\contentsname}{Table of Contents}}
% The major level subsections (heading 1 level) start from a new page.
\AddToHook{cmd/section/before}{\clearpage}

% Paragraph style. If you do not use indentation there should be a space between the paragraphs. No mixing of the two styles is permitted within the same paper.

% Justifying. The text must be justified from both left and right margin.

% The page numbers of a thesis are placed at the bottom of a page, in the centre. The title page does not have a page number although it is counted (i.e. the page numbers start from the page after the title page and with two).

% Headings. It should be remembered that the space between the last paragraph of a chapter and the new heading should be larger than between the heading and the following paragraph. Even though the text should be justified from both sides the titles should commonly be set to left margin. If the title is on a separate row there is no full stop after it.


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
% \newenvironment{name}[numarg][optarg_default]{begin_def}{end_def}
\RequirePackage[dvipsnames]{xcolor}
\definecolor{brightRed}{HTML}{F15E22}
\newenvironment{todo}
	{\textcolor{brightRed}{\textbf{**TODO: }}}
	{\textcolor{orange}{\textbf{**-----}}}

\RequirePackage{subfiles} % Best loaded last in the preamble