# Interview Toolkit
## Resume and cover letter templates
I use the templates `resume.cls` and `cover.cls` for the styling and structure of my resumes and cover letters. You are free to do so as well! The styling is inspired by the [Semantic UI](https://semantic-ui.com/) style which I used on my [site](www.theodedeken.xyz).

### Resume template commands and environments
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

### Cover letter template
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

## Resume and cover letter generators
To optimize the process of making cover letters and resumes for potential jobs I wrote some quick and dirty python script to generate then for me from a yml file. This way content is separated from styling and structure.

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

### Usage
It's required that the `latexmk`  command is available.

```bash
python cover_script.py <path_to_cover_template> <path_to_cover_yml_file>
```