import yaml

from .lib import write_tex


def generate_cover(template_file, content_file, lang):
    with open(content_file, 'r') as content:
        content = yaml.load(content)
        name = 'cover_{}.tex'.format(
            content['author'].lower().replace(' ', '_'))
        with open(name, 'w') as output_file:
            write_tex(output_file, 'documentclass[11pt,{}]'.format(
                lang), template_file)
            write_tex(output_file, 'usepackage', 'babel')

            write_tex(output_file, 'author', content['author'])
            write_tex(output_file, 'title', content['title'])
            write_tex(output_file, 'begin', 'document')

            write_tex(output_file, 'begin', 'letter', content['addressee'])

            write_tex(output_file, 'begin', 'covdetails')
            for key, value in content['details'].items():
                write_tex(output_file, 'cov{}'.format(key), value)
            write_tex(output_file, 'end', 'covdetails')

            write_tex(output_file, 'signature', content['signature'])
            write_tex(output_file, 'opening', content['opening'])
            output_file.write(content['body'] + '\n')
            write_tex(output_file, 'closing', content['closing'])

            write_tex(output_file, 'end', 'letter')
            write_tex(output_file, 'end', 'document')
    return name
