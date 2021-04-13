import os


def get_fonts():
    with open(os.getcwd() + '/meta/fonts.txt') as file:
        return [line.rstrip() for line in file]


def get_colors():
    with open(os.getcwd() + '/meta/colors.txt') as file:
        return [line.rstrip() for line in file]


def get_scope_symbols():
    return '{}'


def get_scope_start_symbol():
    return get_scope_symbols()[0]


def get_scope_end_symbol():
    return get_scope_symbols()[1]


def get_header_symbols():
    return '[]'


def get_header_start_symbol():
    return get_header_symbols()[0]


def get_header_end_symbol():
    return get_header_symbols()[1]


def get_author_symbols():
    return '()'


def get_author_start_symbol():
    return get_author_symbols()[0]


def get_author_end_symbol():
    return get_author_symbols()[1]


def get_comment_symbol():
    return '#'


def get_middle_marker():
    return ':M'


def get_right_marker():
    return ':R'
