\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{template}[My custom CV class]

\LoadClass{article}

% Packages
\RequirePackage{titlesec}
\RequirePackage{graphicx}
\RequirePackage{tikz}
\RequirePackage[left=1cm, right=1cm, top=1cm, bottom=1cm]{geometry}
\RequirePackage{hyperref}
\RequirePackage[default]{lato}
\RequirePackage[T1]{fontenc}
\RequirePackage{fontawesome}
\RequirePackage{xcolor}

\definecolor{secondary}{gray}{0.314}




% Section
\titleformat{\section}         % Customise the \section command 
  {\huge\scshape\raggedright} % Make the \section headers large (\Large),
                               % small capitals (\scshape) and left aligned (\raggedright)
  {}{0em}                      % Can be used to give a prefix to all sections, like 'Section ...'
  {}                           % Can be used to insert code before the heading
  [\titlerule]                 % Inserts a horizontal line after the heading

% Commands
\newcommand{\cvexperience}[4]{%
  \subsection[#1]{#1 \hfill #2}
  #3 #4
}

\newcommand{\cvphoto}[1]{%
  \roundpic{.3\textwidth}{.3\textwidth}{#1} 
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