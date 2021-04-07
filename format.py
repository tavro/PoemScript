import webbrowser
import os
import sys
import pdfkit

header_start_symbol = '['
header_end_symbol = ']'

author_start_symbol = '('
author_end_symbol = ')'

comment_symbol = '#'

middle_marker = ':M'
right_marker = ':R'

content = []
title = ""

is_centered = False
to_right = False


def process_file(path, class_name):
    with open(path) as file:
        lines = [line.rstrip() for line in file]

    customizable2 = "<div class=\"" + class_name + "\" style=\"margin: auto; width: 50%;\">"
    content.append(customizable2)

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

    meta3 = "</div></body></html>"
    content.append(meta3)


def process_line(line):
    if line.startswith(header_start_symbol) and line.endswith(header_end_symbol):
        center = "<br>"
        content.append(center)

        global is_centered
        global to_right

        if is_centered:
            center = "</center>"
            content.append(center)
            is_centered = False
        elif to_right:
            div = "</div>"
            content.append(div)
            to_right = False

        if middle_marker in line:
            is_centered = True
            center = "<center>"
            content.append(center)
            append_header(line[1:-3])
        elif right_marker in line:
            to_right = True
            div = "<div style=\"float: right;\">"
            content.append(div)
            append_header(line[1:-3])
        else:
            append_header(line[1:-1])
    elif line.startswith(author_start_symbol) and line.endswith(author_end_symbol):
        append_author(line[1:-1])
    else:
        append_paragraph(line)


def append_header(line):
    processed_line = "<h1 style=\"font-weight: bold; margin-bottom: 0px;\">" + line + "</h1>"
    content.append(processed_line)


def append_author(line):
    processed_line = "<p style=\"color:gray;  margin-top: 0px;\">by " + line + "</p>"
    content.append(processed_line)


def append_paragraph(line):
    processed_line = "<p style=\"margin-bottom: 6px; margin-top: 6px;\">" + line + "</p>"
    content.append(processed_line)


def write(name):
    file = open(os.getcwd() + '/' + name + '.html', 'w')
    for line in content:
        file.write('%s\n' % line)
    file.close()
    pdfkit.from_file(name + ".html", name + ".pdf")


def open_document(name):
    webbrowser.open_new_tab(os.getcwd() + '/' + name + '.pdf')


def generate_document(path):
    global title
    title = sys.argv[1][:-4]

    meta1 = "<!DOCTYPE HTML><html><head><meta charset=\"utf-8\"/>"
    content.append(meta1)

    customizable1 = "<title>" + title + "</title>"
    content.append(customizable1)

    meta2 = "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/></head><body>"
    content.append(meta2)

    process_file(path, title)

    write(title)
    open_document(title)


def main():
    generate_document(os.getcwd() + '/' + sys.argv[1])


if __name__ == "__main__":
    main()
