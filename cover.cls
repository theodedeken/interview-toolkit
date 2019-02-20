\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{template}[A cover letter based on the Semantic UI style]

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