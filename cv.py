import yaml
import sys


def generate_cv(template_file, content_file):
    with open(content_file, 'r') as content:
        content = yaml.load(content)
        name = 'cv_{}.tex'.format(content['author'].lower().replace(' ', '_'))
        with open(name, 'w') as output_file:
            _wl(output_file,
                "\\documentclass{{{}}}".format(template_file))
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
            _wl(output_file, '\\section{Education}')
            for item in content['education']:
                _w_item(output_file, item)
            # Experience
            _wl(output_file, '\\section{Experience}')
            for item in content['experience']:
                _w_item(output_file, item)
            # Projects
            _wl(output_file, '\\section{Projects}')
            for item in content['projects']:
                _w_project(output_file, item)
            # Skills
            _wl(output_file, '\\section{Skills}')
            _wl(output_file, '\\begin{cvskills}')
            for skill in content['skills']:
                _w_skill(output_file, skill)
            _wl(output_file, '\\end{cvskills}')
            # Call to action
            _wl(output_file, '\\cvcallaction{{{}}}'.format(content['action']))

            _wl(output_file, '\\end{document}')


def _wl(file, line):
    file.write(line + ' \n')


def _w_skill(file, skill):
    _wl(file, '\\cvskill{{{}}}{{{}}}{{{}}}'.format(
        skill['title'], skill['grade'], skill['text']))


def _w_item(file, item):
    _wl(file, '\\cvitem{{{}}}{{{}}}{{{}}}{{{}}}'.format(
        item['title'], item['place'], item['date'], item['text']))


def _w_project(file, project):
    _wl(file, '\\cvproject{{{}}}{{{}}}{{{}}}'.format(
        project['title'], project['link'], project['text']))


if __name__ == "__main__":
    generate_cv(sys.argv[1], sys.argv[2])
