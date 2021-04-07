import document_handler
import sys
import os


header_start_symbol = '['
header_end_symbol = ']'

author_start_symbol = '('
author_end_symbol = ')'

comment_symbol = '#'

middle_marker = ':M'
right_marker = ':R'

is_centered = False
to_right = False


def process_file(path, class_name):
    with open(path) as file:
        lines = [line.rstrip() for line in file]

    document_handler.append_centered_div(class_name)

    is_comment = False
    for line in lines:
        if line:
            if comment_symbol in line:
                if not (line.count(comment_symbol) % 2 == 0):
                    is_comment = not is_comment
                    if not is_comment:
                        continue
                else:
                    continue
            if not is_comment:
                process_line(line)

    document_handler.append_closing_tags()


def process_line(line):
    if line.startswith(header_start_symbol) and line.endswith(header_end_symbol):
        center = "<br>"
        document_handler.append(center)

        global is_centered
        global to_right

        if is_centered:
            center = "</center>"
            document_handler.append(center)
            is_centered = False
        elif to_right:
            div = "</div>"
            document_handler.append(div)
            to_right = False

        if middle_marker in line:
            is_centered = True
            center = "<center>"
            document_handler.append(center)
            document_handler.append_header(line[1:-3])
        elif right_marker in line:
            to_right = True
            div = "<div style=\"float: right;\">"
            document_handler.append(div)
            document_handler.append_header(line[1:-3])
        else:
            document_handler.append_header(line[1:-1])
    elif line.startswith(author_start_symbol) and line.endswith(author_end_symbol):
        document_handler.append_author(line[1:-1])
    else:
        document_handler.append_paragraph(line)


def main():
    name = sys.argv[1]
    document_handler.generate_document(os.getcwd() + '/' + name, name[:-4], process_file)


if __name__ == "__main__":
    main()
