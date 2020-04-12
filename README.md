<!--
SPDX-FileCopyrightText: 2020 Theo Dedeken

SPDX-License-Identifier: CC0-1.0
-->

# interview-toolkit

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
![REUSE compliant](https://github.com/theodedeken/interview-toolkit/workflows/REUSE%20compliant/badge.svg)

Script to generate resumes and cover letters

I use the templates `resume.cls` and `cover.cls` for the styling and structure of my resumes and cover letters. You are free to do so as well! The styling is inspired by the [Semantic UI](https://semantic-ui.com/) style which I used on my [site](www.theodedeken.xyz).

I also created a script to automatically generate them from `.yml` files.

## Table of Contents

- [interview-toolkit](#interview-toolkit)
  - [Table of Contents](#table-of-contents)
  - [Install](#install)
  - [Usage](#usage)
    - [Generate a cover letter](#generate-a-cover-letter)
    - [Generate a resume](#generate-a-resume)
    - [Arguments](#arguments)
  - [Overview of Latex style files](#overview-of-latex-style-files)
    - [Resume](#resume)
      - [Environments](#environments)
        - [`cvheader`](#cvheader)
        - [`cvdetails`](#cvdetails)
        - [`cvskills`](#cvskills)
      - [Commands](#commands)
        - [`\cvsite`](#cvsite)
        - [`\cvemail`](#cvemail)
        - [`\cvbirthdate`](#cvbirthdate)
        - [`\cvaddress`](#cvaddress)
        - [`\cvphone`](#cvphone)
        - [`\cvgithub`](#cvgithub)
        - [`\cvitem`](#cvitem)
        - [`\cvskill`](#cvskill)
        - [`\cvproject`](#cvproject)
        - [`\cvcallaction`](#cvcallaction)
    - [Cover letter](#cover-letter)
      - [Environment](#environment)
        - [`covdetails`](#covdetails)
      - [Commands](#commands-1)
        - [`\covemail`](#covemail)
        - [`\covaddress`](#covaddress)
        - [`\covphone`](#covphone)
  - [Configuration files for the generators](#configuration-files-for-the-generators)
    - [Resume yml structure](#resume-yml-structure)
    - [Cover letter yml structure](#cover-letter-yml-structure)
  - [Maintainers](#maintainers)
  - [Contributing](#contributing)
  - [License](#license)

## Install

```bash
git clone https://github.com/theodedeken/interview-toolkit
pip install .
```

## Usage

It's required that the `latexmk`  command is available.

### Generate a cover letter
```bash
interview-toolkit cover <path_to_cover_yml_file>
```

### Generate a resume
```bash
interview-toolkit resume <path_to_resume_yml_file>
```

### Arguments
* `--lang <lang>`: specify language (currently only `dutch` and `english` are supported)
* `--tex`: only generate `.tex` file
* `--clean`: clean the build files

## Overview of Latex style files
### Resume
#### Environments
##### `cvheader`
The header of the resume, takes the path to your photo as argument.
##### `cvdetails`
The details section of the header.
##### `cvskills`
Environment to group and format the `cvskill` commands.

#### Commands

##### `\cvsite`
Used in the `cvdetails` environment to add a site to your details.

##### `\cvemail`
Used in the `cvdetails` environment to add an email to your details.

##### `\cvbirthdate`
Used in the `cvdetails` environment to add a birthdate to your details.

##### `\cvaddress`
Used in the `cvdetails` environment to add an address to your details.

##### `\cvphone`
Used in the `cvdetails` environment to add a phone number to your details.

##### `\cvgithub`
Used in the `cvdetails` environment to add a link to your Github profile to your details.

##### `\cvitem`
Experience to add to your resume.
```latex
\cvitem{title}{location}{date}{description}{leveraged_knowledge}
```

##### `\cvskill`
Skill to add to your resume.
```latex
\cvskill{name}{grade}{content}
```

##### `\cvproject`
Personal project to add to your resume
```latex
\cvproject{title}{link}{description}{leveraged_knowledge}
```

##### `\cvcallaction`
Add a call to action to your resume.

### Cover letter
#### Environment
##### `covdetails`
Section in the cover letter to include your own details.
#### Commands
##### `\covemail`
Used in the `covdetails` environment to add an email address to your details.
##### `\covaddress`
Used in the `covdetails` environment to add an address to your details.
##### `\covphone`
Used in the `covdetails` environment to add a phone number to your details.

## Configuration files for the generators
To optimize the process of making cover letters and resumes for potential jobs I wrote a script to generate then for me from a yml file. This way content is separated from styling and structure.

### Resume yml structure
```yml
author: your name
title: your title
photo: path to your photo
details:
  birthdate: your birthdate
  address: your address
  phone: your phone
  site: your site
  email: your email
  github: your github username
education:
  - title: degree title
    place: institution
    date:  period of enrollment
    text: extra info
  ...
experience:
  - title: title of experience
    place: location of experience
    date: period of experience
    text: description of experience
    leveraged: leveraged knowledge
  ...
projects:
  - title: title of project
    link: link to project
    text: description of project
    leveraged: leveraged knowledge
skills:
  - title: skill name
    grade: skill grade
    body: skill body
  ...
action: call to action
```

### Cover letter yml structure
```yml
author: your name
title: your title
details:
  address: your address
  phone: your phone
  email: your email
addressee: The recipient of your cover letter
signature: your signature
opening: your opening
closing: your closing
body: the cover letter itself
```

## Maintainers

[@theodedeken](https://github.com/theodedeken)

## Contributing

Small note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © 2020 Theo Dedeken

This work is licensed under multiple licences:

* All original source code is licensed under MIT.
* All configuration files are licensed under CC0.
* My picture in the examples is licensed under CC-BY-NC-4.0.

All the files in this repo are licensed according to the [REUSE](https://reuse.software) specification.