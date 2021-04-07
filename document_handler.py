import os
import pdfkit
import webbrowser


content = []


def append(line):
    content.append(line)


def append_header(line):
    processed_line = "<h1 style=\"font-weight: bold; margin-bottom: 0px;\">" + line + "</h1>"
    content.append(processed_line)


def append_author(line):
    processed_line = "<p style=\"color:gray;  margin-top: 0px;\">by " + line + "</p>"
    content.append(processed_line)


def append_paragraph(line):
    processed_line = "<p style=\"margin-bottom: 6px; margin-top: 6px;\">" + line + "</p>"
    content.append(processed_line)


def append_centered_div(class_name):
    processed_line = "<div class=\"" + class_name + "\" style=\"margin: auto; width: 50%;\">"
    content.append(processed_line)


def append_closing_tags():
    processed_line = "</div></body></html>"
    content.append(processed_line)


def write(name):
    file = open(os.getcwd() + '/' + name + '.html', 'w')
    for line in content:
        file.write('%s\n' % line)
    file.close()
    pdfkit.from_file(name + ".html", name + ".pdf")


def open_document(name):
    webbrowser.open_new_tab(os.getcwd() + '/' + name + '.pdf')


def generate_document(path, title, process_func):
    meta1 = "<!DOCTYPE HTML><html><head><meta charset=\"utf-8\"/>"
    content.append(meta1)

    customizable1 = "<title>" + title + "</title>"
    content.append(customizable1)

    meta2 = "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/></head><body>"
    content.append(meta2)

    process_func(path, title)

    write(title)
    open_document(title)
