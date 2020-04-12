% SPDX-FileCopyrightText: 2020 Theo Dedeken
%
% SPDX-License-Identifier: MIT

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{template}[A resume based on the Semantic UI style]

\LoadClass{article}

% Packages
\RequirePackage{titlesec}
\RequirePackage{graphicx}
\RequirePackage{tikz}
\RequirePackage[left=1.5cm, right=1cm, top=1cm, bottom=1cm]{geometry}
\RequirePackage{hyperref}
\RequirePackage[default]{lato}
\RequirePackage[T1]{fontenc}
\RequirePackage{fontawesome}
\RequirePackage{xcolor}
\RequirePackage{intcalc}
\RequirePackage{ifthen}
\RequirePackage{tcolorbox}

\definecolor{primary}{HTML}{2185D0}
\definecolor{secondary}{gray}{0.6}
\pagestyle{empty}



% Section
\titleformat{\section}         % Customise the \section command 
  {\large\raggedright} % Make the \section headers large (\Large),
                               % small capitals (\scshape) and left aligned (\raggedright)
  {}{0em}                      % Can be used to give a prefix to all sections, like 'Section ...'
  {}                           % Can be used to insert code before the heading
  [{\color{secondary}\titlerule[.5pt]}]                 % Inserts a horizontal line after the heading
\titlespacing*{\section}{2pt}{*0}{4pt}


\titleformat{\subsection}
  {
    \large\raggedright
  }{}{0em}{}
\titlespacing*{\subsection}{0pt}{*0}{0pt}

% Commands
\newcommand{\cvitem}[5]{%
  \subsection[#1]{\textbf{#1} \hfill {\normalsize\faMapMarker \hspace{3px} #2}}
  {\footnotesize \textcolor{secondary}{\faCalendar \hspace{5px}#3}}\newline 
  {
    \small #4 
    \ifthenelse{\equal{#5}{0}}{

    }{
      \newline
      \textbf{\iflanguage{english}{Leveraged knowledge}{Gebruikte kennis}: } #5
    }
  }
  \vspace{5pt}
}

\newcommand{\cvphoto}[1]{%
  \roundpic{.25\textwidth}{.25\textwidth}{#1} 
}

\newcommand{\roundpic}[4][]{
  \tikz\node [circle, minimum width = #2,
    path picture = {
      \node [#1] at (path picture bounding box.center) {
        \includegraphics[width=#3]{#4}};
    }] {};}

\newcommand{\cviconline}[2]{
  {\Large #1} &
  #2
  \\
}

\newcommand{\cvsite}[1]{
  \cviconline{\faLink}{\href{https://#1}{#1}}
}

\newcommand{\cvemail}[1]{
  \cviconline{\faEnvelope}{\href{mailto:#1}{#1}}
}

\newcommand{\cvbirthdate}[1]{
  \cviconline{\faInfoCircle}{#1}
}

\newcommand{\cvaddress}[1]{
  \cviconline{\faMapMarker}{#1}
}

\newcommand{\cvphone}[1]{
  \cviconline{\faMobile}{#1}
}

\newcommand{\cvname}[1]{
  {\Huge #1}
}

\newcommand{\cvtitle}[1]{
  {\large \textcolor{secondary}{#1}}
}

\newcommand{\cvgithub}[1]{
  \cviconline{\faGithub}{\href{https://github.com/#1}{#1}}
}

\newcommand{\cvskill}[3]{%
  \stepcounter{skillcount}
  \begin{tcolorbox}[colback=white,colframe=secondary,boxrule=0.5pt,boxsep=0mm,nobeforeafter]  
    \textbf{#1} \hfill  
    \cvgrade{#2}
    \vspace{3pt}
    {\color{secondary}\hrule}
    \vspace{3pt}
    {\small #3}
  \end{tcolorbox}
  \ifthenelse{\equal{\intcalcMod{\theskillcount}{4}}{0}}
    {\\}
    {&}
}

%\newcommand{\cvgrade}[1]{
%  \foreach \n in {0,...,5}{
%    \ifthenelse{\n < #1}{\faStar}{}
%  }
%}

\newcommand{\cvgrade}[1]{
  #1 \faStar
}

\newcommand{\cvproject}[4]{
  \subsection[#1]{\textbf{#1} \hfill {\normalsize\href{https://#2}{#2}}}
  {
    \small #3 \newline
    \textbf{\iflanguage{english}{Leveraged knowledge}{Gebruikte kennis}: } #4
  }
  \vspace{5pt}
}

\newcommand{\cvcallaction}[1]{
  \begin{tcolorbox}[colback=primary,colframe=primary, halign=center]
    {\bf\textcolor{white}{#1}}
  \end{tcolorbox}
}

%Environmnents
\newenvironment{cvheader}[1]
{
  \begin{center}
    \begin{tabular}{l l}
      \cvphoto{#1} &
}{
    \end{tabular}
  \end{center}
}

\newenvironment{cvdetails}
{
  \begin{tabular}[b]{l}
    \cvname{\@author} \\
    \cvtitle{\@title} \\  \\
    \begin{tabular}[b]{c l}
}{
    \end{tabular}
  \end{tabular}
}


\newcounter{skillcount}
\newenvironment{cvskills}
{
  \setcounter{skillcount}{0}
  \begin{center}
    \begin{tabular}{p{.225\textwidth} p{.225\textwidth} p{.225\textwidth} p{.225\textwidth}}
}{
  
    \end{tabular}
  \end{center}
}