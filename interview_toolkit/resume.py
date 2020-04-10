import yaml
import sys
import subprocess


def generate_resume(template_file, content_file, lang):
    with open(content_file, 'r') as content:
        content = yaml.load(content)
        name = 'cv_{}.tex'.format(content['author'].lower().replace(' ', '_'))
        with open(name, 'w') as output_file:
            _wl(output_file,
                "\\documentclass[{}]{{{}}}".format(lang, template_file))
            _wl(output_file,  "\\usepackage{babel}")
            _wl(output_file, "\\author{{{}}}".format(content['author']))
            _wl(output_file, "\\title{{{}}}".format(content['title']))
            _wl(output_file, '\\begin{document}')
            # Header
            _wl(output_file, '\\begin{{cvheader}}{{{}}}'.format(
                content['photo']))
            _wl(output_file, '\\begin{cvdetails}')
            for key, value in content['details'].items():
                _wl(output_file, '\\cv{}{{{}}}'.format(key, value))
            _wl(output_file, '\\end{cvdetails}')
            _wl(output_file, '\\end{cvheader}')

            # Education
            _wl(output_file, '\\section{EDUCATION}')
            for item in content['education']:
                _w_item(output_file, item)
            # Experience
            _wl(output_file, '\\section{EXPERIENCE}')
            for item in content['experience']:
                _w_item(output_file, item)
            # Projects
            if 'projects' in content:
                _wl(output_file, '\\section{PROJECTS}')
                for item in content['projects']:
                    _w_project(output_file, item)

            # Skills
            if 'skills' in content:
                _wl(output_file, '\\section{SKILLS}')
                _wl(output_file, '\\begin{cvskills}')
                for skill in content['skills']:
                    _w_skill(output_file, skill)
                _wl(output_file, '\\end{cvskills}')

            # Call to action
            _wl(output_file, '\\cvcallaction{{{}}}'.format(content['action']))

            _wl(output_file, '\\end{document}')
    return name


def _wl(file, line):
    file.write(line + ' \n')


def _w_skill(file, skill):
    text = ''
    if 'frameworks' in skill:
        text = ' \\textbf{FRAMEWORKS}'
        text += '\\begin{itemize}'
        for framework in skill['frameworks']:
            text += '\\item {}'.format(framework)
        text += '\\end{itemize}'
    elif 'body' in skill:
        text = skill['body']
    _wl(file, '\\cvskill{{{}}}{{{}}}{{{}}}'.format(
        skill['title'], skill['grade'], text))


def _w_item(file, item):
    if 'leveraged' in item:
        leveraged = item['leveraged']
    else:
        leveraged = 0
    _wl(file, '\\cvitem{{{}}}{{{}}}{{{}}}{{{}}}{{{}}}'.format(
        item['title'], item['place'], item['date'], item['text'], leveraged))


def _w_project(file, project):
    _wl(file, '\\cvproject{{{}}}{{{}}}{{{}}}{{{}}}'.format(
        project['title'], project['link'], project['text'], project['leveraged']))