def write_tex(file, identifier, *args):
    line = '\\{}'.format(identifier)
    for arg in args:
        line += '{{{}}}'.format(arg)

    _wl(file, line)


def _wl(file, line):
    file.write(line + ' \n')
