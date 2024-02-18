# SPDX-FileCopyrightText: 2020 Theo Dedeken
#
# SPDX-License-Identifier: MIT

import yaml
from .lib import write_tex

dictionary = {
    'english': {
        'edu': 'EDUCATION',
        'exp': 'EXPERIENCE',
        'prj': 'PROJECTS',
        'skl': 'SKILLS'
    },
    'dutch':  {
        'edu': 'OPLEIDING',
        'exp': 'ERVARING',
        'prj': 'PROJECTEN',
        'skl': 'VAARDIGHEDEN'
    },
}


def generate_resume(template_file, content_file, lang):
    with open(content_file, 'r') as content:
        content = yaml.load(content, yaml.SafeLoader)
        name = 'cv_{}.tex'.format(content['author'].lower().replace(' ', '_'))
        with open(name, 'w') as output_file:
            write_tex(output_file, 'documentclass[{}]'.format(
                lang), template_file)

            write_tex(output_file, 'usepackage', 'babel')
            write_tex(output_file, 'author', content['author'])
            write_tex(output_file, 'title', content['title'])
            write_tex(output_file, 'begin', 'document')

            # Header
            write_tex(output_file, 'begin', 'cvheader', content['photo'])
            write_tex(output_file, 'begin', 'cvdetails')
            for key, value in content['details'].items():
                write_tex(output_file, 'cv{}'.format(key), value)
            write_tex(output_file, 'end', 'cvdetails')
            write_tex(output_file, 'end', 'cvheader')

            # Education
            write_tex(output_file, 'section',  dictionary[lang]['edu'])
            for item in content['education']:
                _w_item(output_file, item)
            # Experience
            write_tex(output_file, 'section',  dictionary[lang]['exp'])
            for item in content['experience']:
                _w_item(output_file, item)
            # Projects
            if 'projects' in content:
                write_tex(output_file, 'section', dictionary[lang]['prj'])
                for item in content['projects']:
                    _w_project(output_file, item)

            # Skills
            if 'skills' in content:
                write_tex(output_file, 'section',  dictionary[lang]['skl'])
                write_tex(output_file, 'begin', 'cvskills')
                for skill in content['skills']:
                    _w_skill(output_file, skill)
                write_tex(output_file, 'end', 'cvskills')

            # Call to action
            write_tex(output_file, 'cvcallaction', content['action'])

            write_tex(output_file, 'end', 'document')
    return name


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
    write_tex(file, 'cvskill', skill['title'], skill['grade'], text)


def _w_item(file, item):
    if 'leveraged' in item:
        leveraged = item['leveraged']
    else:
        leveraged = 0
    write_tex(file, 'cvitem', item['title'], item['place'],
              item['date'], item['text'], leveraged)


def _w_project(file, project):
    write_tex(file, 'cvproject',
              project['title'], project['link'], project['text'], project['leveraged'])
