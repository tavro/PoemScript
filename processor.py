import document_handler
import settings
import sys
import os


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

    document_handler.append_closing_tags()


def process_line(line):
    """
    helper function for process_file
    """

    # get color
    color = ""
    for col in settings.colors:
        if col in line:
            line = line.replace(col, '')
            color = col[1:]
            break

    # check if header
    if line.startswith(settings.get_header_start_symbol()) and line.endswith(settings.get_header_end_symbol()):
        document_handler.append_opening_tag("br")

        if not color:
            color = "black"

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
            document_handler.append_header(line[1:-3], color)
        elif settings.get_right_marker() in line:
            to_right = True
            document_handler.append("<div style=\"float: right;\">")
            document_handler.append_header(line[1:-3], color)
        else:
            document_handler.append_header(line[1:-1], color)
    elif line.startswith(settings.get_author_start_symbol()) and line.endswith(settings.get_author_end_symbol()):
        if not color:
            color = "gray"
        document_handler.append_author(line[1:-1], color)
    else:
        if not color:
            color = "black"
        document_handler.append_paragraph(line, color)


def main():
    name = sys.argv[1]
    document_handler.generate_document(os.getcwd() + '/' + name, name[:-4], process_file)


if __name__ == "__main__":
    main()
