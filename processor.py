import document_handler
import settings
import sys
import os
import re


is_centered = False
to_right = False


def process_file(path, class_name):
    """
    converts PoemScript Markdown to html

    :param path: file containing PoemScript Markdown
    :param class_name: div class name
    """
    # get every line in given file as list
    with open(path) as file:
        lines = [line.rstrip() for line in file]

    document_handler.append_centered_div(class_name)

    # check for lines to ignore
    is_comment = False
    symbol = settings.get_comment_symbol()
    for line in lines:
        if line:
            if symbol in line:
                if not (line.count(symbol) % 2 == 0):
                    is_comment = not is_comment
                    if not is_comment:
                        continue
                else:
                    continue
            if not is_comment:
                process_line(line)
        else:
            document_handler.append_opening_tag("br")

    document_handler.append_closing_tags()


def process_line(line):
    """
    helper function for process_file
    """

    # get color
    color = ""
    for col in settings.get_colors():
        if col in line:
            line = line.replace(col, '')
            color = col[1:]
            break

    # get font
    font = "Arial"
    for ft in settings.get_fonts():
        if ft in line:
            line = line.replace(ft, '')
            font = ft[1:]
            break

    # get size
    size = ""
    compiled_regex = re.compile(':' + r'\d+')
    match = compiled_regex.search(line)
    if match:
        match = match.group()
        line = line.replace(match, '')
        size = match[1:]

    # check if header
    if line.startswith(settings.get_header_start_symbol()) and line.endswith(settings.get_header_end_symbol()):
        document_handler.append_opening_tag("br")
        size, color = process_arguments(size, "32", color, "black")

        global is_centered
        global to_right

        # close alignment
        if is_centered:
            document_handler.append_closing_tag("center")
            is_centered = False
        elif to_right:
            document_handler.append_closing_tag("div")
            to_right = False

        # check how to align
        if settings.get_middle_marker() in line:
            is_centered = True
            document_handler.append_opening_tag("center")
            document_handler.append_header(line[1:-3], color, font, size)
        elif settings.get_right_marker() in line:
            to_right = True
            document_handler.append("<div style=\"float: right;\">")
            document_handler.append_header(line[1:-3], color, font, size)
        else:
            document_handler.append_header(line[1:-1], color, font, size)
    elif line.startswith(settings.get_author_start_symbol()) and line.endswith(settings.get_author_end_symbol()):
        size, color = process_arguments(size, "12", color, "gray")
        document_handler.append_author(line[1:-1], color, font, size)
    else:
        size, color = process_arguments(size, "16", color, "black")
        document_handler.append_paragraph(line, color, font, size)


def process_arguments(size, default_size, color, default_color):
    if not size:
        size = default_size
    if not color:
        color = default_color
    return size, color


def get_color():
    pass


def get_font():
    pass


def get_size():
    pass


def main():
    name = sys.argv[1]
    document_handler.generate_document(os.getcwd() + '/' + name, name[:-4], process_file)


if __name__ == "__main__":
    main()
