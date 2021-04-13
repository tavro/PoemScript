import os

header_start_symbol = '['
header_end_symbol = ']'

author_start_symbol = '('
author_end_symbol = ')'

comment_symbol = '#'

middle_marker = ':M'
right_marker = ':R'


def get_fonts():
    with open(os.getcwd() + '/meta/fonts.txt') as file:
        return [line.rstrip() for line in file]


def get_colors():
    with open(os.getcwd() + '/meta/colors.txt') as file:
        return [line.rstrip() for line in file]


def get_header_symbols():
    pass


def get_header_start_symbol():
    return header_start_symbol


def get_header_end_symbol():
    return header_end_symbol


def get_author_symbols():
    pass


def get_author_start_symbol():
    return author_start_symbol


def get_author_end_symbol():
    return author_end_symbol


def get_comment_symbol():
    return comment_symbol


def get_middle_marker():
    return middle_marker


def get_right_marker():
    return right_marker
