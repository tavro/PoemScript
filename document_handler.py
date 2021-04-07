import os
import pdfkit
import webbrowser


content = []


def append(line):
    content.append(line)


def append_opening_tag(tag_type):
    processed_line = "<" + tag_type + ">"
    content.append(processed_line)


def append_title(title):
    processed_line = "<title>" + title + "</title>"
    content.append(processed_line)


def append_header(line):
    processed_line = "<h1 style=\"font-weight: bold; margin-bottom: 0px;\">" + line + "</h1>"
    content.append(processed_line)


def append_closing_tag(tag_type):
    processed_line = "</" + tag_type + ">"
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
    append_closing_tag("div")
    append_closing_tag("body")
    append_closing_tag("html")


def write(name):
    file = open(os.getcwd() + '/' + name + '.html', 'w')
    for line in content:
        file.write('%s\n' % line)
    file.close()
    pdfkit.from_file(name + ".html", name + ".pdf")


def open_document(name):
    webbrowser.open_new_tab(os.getcwd() + '/' + name + '.pdf')


def generate_document(path, title, process_func):
    append("<!DOCTYPE HTML><html><head><meta charset=\"utf-8\"/>")

    append_title(title)

    append("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>")
    append_closing_tag("head")
    append_opening_tag("body")

    process_func(path, title)

    write(title)
    open_document(title)
