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

\usepackage[T1]{fontenc} %Absolutely critical for *hyphenation* of words with non-ASCII letters.

% For images
\RequirePackage{graphicx}
\RequirePackage{float}
\RequirePackage{wrapfig}
\RequirePackage{subcaption}

%===Choose the main language in thesis
\usepackage[estonian, english]{babel} %the thesis is in English
% \usepackage[english, estonian]{babel} %the thesis is in Estonian

\RequirePackage[final]{microtype}
\RequirePackage{csquotes}

\RequirePackage{tabularx}

% embed jpeg png
\RequirePackage{graphicx}

\RequirePackage[format=plain,font=it]{caption}

% TABLE OF CONTENTS
\RequirePackage[notlof, nottoc, notlot, numbib]{tocbibind}

% this will make table of contents hypelinks and will allow to use hyperlinks in refs
\RequirePackage[]{hyperref}
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

% FONTS
% \RequirePackage{fontspec}

% % \setmainfont[
% %     Path=../helpers/AtkinsonHyperlegible/
% %     Scale=0.9,
% %     Extension = .ttf,
% %     UprightFont=*-Regular,
% %     BoldFont=*-Bold,
% %     ItalicFont=*-Italic,
% %     BoldItalicFont=*-BoldItalic
% %     ]{AtkinsonHyperlegible}

% \setmainfont{Atkinson_Hyperlegible}

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

% LISTS
\RequirePackage[titles]{tocloft}

% List of Figures
\newlength{\figNumLen}
\renewcommand\cftfigindent{0pt}  % no indentation
\renewcommand\cftfigpresnum{Figure~}   % prefix "(" before figure number
\renewcommand\cftfigaftersnum{.} % affix ")" after figure number
\settowidth{\figNumLen}{\cftfigpresnum\cftfigaftersnum0}
\renewcommand{\cftfignumwidth}{\figNumLen}

% List of Tables
\newlength{\tabNumLen}
\renewcommand\cfttabindent{0pt}  % no indentation
\renewcommand\cfttabpresnum{Table~}   % prefix before figure number
\renewcommand\cfttabaftersnum{.} % affix after tabure number
\settowidth{\tabNumLen}{\cfttabpresnum\cfttabaftersnum0}
\renewcommand{\cfttabnumwidth}{\tabNumLen}


% Paragraph style. If you do not use indentation there should be a space between the paragraphs. No mixing of the two styles is permitted within the same paper.

% Justifying. The text must be justified from both left and right margin.

% The page numbers of a thesis are placed at the bottom of a page, in the centre. The title page does not have a page number although it is counted (i.e. the page numbers start from the page after the title page and with two).

% Headings. It should be remembered that the space between the last paragraph of a chapter and the new heading should be larger than between the heading and the following paragraph. Even though the text should be justified from both sides the titles should commonly be set to left margin. If the title is on a separate row there is no full stop after it.

% List of Abbreviation

\RequirePackage{acro}

\DeclareAcronym{svg}{
  short=SVG,
  long=Scalable Vector Graphics,
}
\DeclareAcronym{who}{
  short=WHO,
  long=World Health Organization,
}
\DeclareAcronym{ci}{
  short=CI,
  long=Continuous Integration,
}
\DeclareAcronym{ui}{
  short=UI,
  long=User Interface,
}
\DeclareAcronym{act}{
  short=ACT,
  long=Accessibility Conformance Testing,
}
\DeclareAcronym{ux}{
  short=UX,
  long=user experience,
}
\DeclareAcronym{dom}{
  short=DOM,
  long=Document Object Model,
}
\DeclareAcronym{cli}{
  short=CLI,
  long=command-line interface,
}
\DeclareAcronym{api}{
  short=API,
  long=application programming interfaces,
}
\DeclareAcronym{html}{
  short=HTML,
  long=HyperText Markup Language,
}
\DeclareAcronym{wai}{
  short=WAI,
  long=Web Accessibility Initiative,
}
\DeclareAcronym{w3c}{
  short=W3C,
  long=World Wide Web Consortium,
}
\DeclareAcronym{cdd}{
  short=CDD,
  long=Component Driven Development,
}
\DeclareAcronym{wcag}{
  short=WCAG,
  long=Web Content Accessibility Guidelines,
}
\DeclareAcronym{crm}{
  short=CRM,
  long=Customer Relationship Management
}
\DeclareAcronym{iaap}{
  short=IAAP,
  long=International Association of Accessibility Professionals
}
\DeclareAcronym{iaapwas}{
  short=IAAP WAS,
  long=International Association of Accessibility Professionals Web Accessibility Specialist
}
\DeclareAcronym{wai-aria}{
  short=WAI-ARIA,
  long=Accessible Rich Internet Applications
}

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
\definecolor{darkRed}{HTML}{BD3E09}
\definecolor{yellow}{HTML}{F6E199}
\definecolor{darkBlue}{HTML}{233658}
\definecolor{lightBlue}{HTML}{BFD5EB}
\definecolor{orange}{HTML}{F5A26F}
\definecolor{lilac}{HTML}{C5AECF}

% Nice todo notes (backgroundcolor=lightBlue!25)
\setlength {\marginparwidth }{2cm}
\RequirePackage[backgroundcolor=yellow, bordercolor=yellow, textcolor=darkBlue, colorinlistoftodos]{todonotes}
\setuptodonotes{inline}
\RequirePackage{xargs} % Use more than one optional parameter in a new commands

\newcommandx{\info}[2][1=]{\todo[backgroundcolor=lightBlue,bordercolor=lightBlue,#1]{#2}}
\newcommandx{\problem}[2][1=]{\todo[backgroundcolor=orange,bordercolor=orange,#1]{#2}}
\newcommandx{\review}[2][1=]{\todo[backgroundcolor=lilac,bordercolor=lilac,#1]{#2}}

\RequirePackage{subfiles} % Best loaded last in the preamble