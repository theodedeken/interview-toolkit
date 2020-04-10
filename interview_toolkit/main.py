import argparse
from .cover import generate_cover
from .resume import generate_resume
import os
import subprocess


def run():
    # Setup argument parser
    parser = argparse.ArgumentParser(
        description='Generate a cover letter or resume.')
    parser.add_argument('type', help='Type of file to create',
                        choices=['cover', 'resume'])
    parser.add_argument(
        'input_file', help='input configuration file')

    parser.add_argument('--clean', action="store_true",
                        help="Cleanup build files",  default=False)
    parser.add_argument('--tex', action="store_true",
                        help="Only generate TeX file",  default=False)
    parser.add_argument(
        '--lang', help="Specify document language (default english)",  default='english')
    args = parser.parse_args()

    if args.type == 'resume':
        filename = generate_resume(os.path.join(
            os.path.dirname(__file__), 'templates', 'resume'), args.input_file, args.lang)
    else:
        filename = generate_cover(os.path.join(
            os.path.dirname(__file__), 'templates', 'cover'), args.input_file, args.lang)

    if not args.tex:
        subprocess.call(["latexmk", "-synctex=1",
                         "-interaction=nonstopmode",
                         "-file-line-error",
                         "-pdf", filename])
    if args.clean:
        subprocess.call(["latexmk", "-c"])
