import yaml
import sys


def generate_resume(template_file, content_file):
    with open(content_file, 'r') as content:
        content = yaml.load(content)
        name = 'cv_{}.tex'.format(content['author'].lower().replace(' ', '_'))
        with open(name, 'w') as output_file:
            _wl(output_file, '\\documentclass[11pt]{{{template_file}}}')

            _wl(output_file, "\\author{{{}}}".format(content['author']))
            _wl(output_file, "\\title{{{}}}".format(content['title']))
            _wl(output_file, '\\begin{document}')

            _wl(output_file, '\\begin{{letter}}{{{}}}'.format(
                content['adressee']))

            _wl(output_file, '\\begin{covdetails}')
            for key, value in content['details'].items():
                _wl(output_file, '\\cov{}{{{}}}'.format(key, value))
            _wl(output_file, '\\end{covdetails}')

            _wl(output_file, '\\signature{{{}}}'.format(content['signature']))

            _wl(output_file, '\\opening{{{}}}'.format(content['opening']))

            _wl(output_file, content['body'])

            _wl(output_file, '\\closing{{{}}}'.format(content['closing']))

            _wl(output_file, '\\end{letter}')
            _wl(output_file, '\\end{document}')


def _wl(file, line):
    file.write(line + ' \n')
