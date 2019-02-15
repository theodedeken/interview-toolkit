\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{template}[My custom CV class]

\LoadClass{letter}

% Packages
\RequirePackage{graphicx}
\RequirePackage{tikz}
\RequirePackage[left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm]{geometry}
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


% Commands
\newcommand{\cvphoto}[1]{%
  \roundpic{.25\textwidth}{.25\textwidth}{#1} 
}

\newcommand{\roundpic}[4][]{
  \tikz\node [circle, minimum width = #2,
    path picture = {
      \node [#1] at (path picture bounding box.center) {
        \includegraphics[width=#3]{#4}};
    }] {};}

\newcommand{\coviconline}[2]{
  {\Large #1} &
  #2
  \\
}

\newcommand{\covemail}[1]{
  \coviconline{\faEnvelope}{\href{mailto:#1}{#1}}
}

\newcommand{\covaddress}[1]{
  \coviconline{\faMapMarker}{#1}
}

\newcommand{\covphone}[1]{
  \coviconline{\faMobile}{#1}
}

\newcommand{\covname}[1]{
  {\Huge #1}
}

\newcommand{\covtitle}[1]{
  {\large \textcolor{secondary}{#1}}
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

\newenvironment{covdetails}
{
  \begin{flushright}
    \covname{\@author} \newline
    \covtitle{\@title} \newline
    {\color{secondary}\hrule}  
    \begin{tabular}{c l}
}{
    \end{tabular}
    \end{flushright}
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