import webbrowser
import os
import sys

header_start_symbol = '['
header_end_symbol = ']'

author_start_symbol = '('
author_end_symbol = ')'

comment_symbol = '#'

content = []
title = ""


def process_file(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]

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


def process_line(line):
    if line.startswith(header_start_symbol) and line.endswith(header_end_symbol):
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


def open_document(name):
    webbrowser.open_new_tab(os.getcwd() + '/' + name + '.html')


def generate_document(path):
    global title
    title = sys.argv[1][:-4]

    meta1 = "<!DOCTYPE HTML><html><head><meta charset=\"utf-8\"/>"
    content.append(meta1)

    customizable1 = "<title>" + title + "</title>"

    content.append(customizable1)
    meta2 = "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/></head><body>"
    content.append(meta2)

    customizable2 = "<div class=\"" + title + "\" style=\"margin: auto; width: 50%;\">"

    content.append(customizable2)

    process_file(path)

    meta3 = "</div></body></html>"
    content.append(meta3)

    write(title)
    open_document(title)


def main():
    generate_document(os.getcwd() + '/' + sys.argv[1])


if __name__ == "__main__":
    main()
