import webbrowser
import os
import sys


header_start_symbol = '['
header_end_symbol = ']'

author_start_symbol = '('
author_end_symbol = ')'

content = []


def process_file(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    for line in lines:
        process_line(line)


def process_line(line):
    if line.startswith(header_start_symbol) and line.endswith(header_end_symbol):
        append_header(line[1:-1])
    elif line.startswith(author_start_symbol) and line.endswith(author_end_symbol):
        append_author(line[1:-1])
    else:
        append_paragraph(line)


def append_header(line):
    processed_line = "<h1 style=\"font-weight: bold\">" + line + "</h1>"
    content.append(processed_line)


def append_author(line):
    processed_line = "<p style=\"color:gray\">by " + line + "</p>"
    content.append(processed_line)


def append_paragraph(line):
    processed_line = "<p>" + line + "</p>"
    content.append(processed_line)


def write(name):
    file = open(os.getcwd() + '/' + name + '.html', 'w')
    for line in content:
        file.write('%s\n' % line)
    file.close()


def open_document(name):
    webbrowser.open_new_tab(os.getcwd() + '/' + name + '.html')


def generate_document(path):
    meta1 = "<!DOCTYPE HTML><html><head><meta charset=\"utf-8\"/>"
    content.append(meta1)
    customizable1 = "<title>Poem</title>"
    content.append(customizable1)
    meta2 = "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/></head><body>"
    content.append(meta2)
    customizable2 = "<div class=\"poem\">"
    content.append(customizable2)

    process_file(path)

    meta3 = "</div></body></html>"
    content.append(meta3)

    write("poem")
    open_document("poem")


def main():
    generate_document(os.getcwd() + '/' + sys.argv[1])


if __name__ == "__main__":
    main()