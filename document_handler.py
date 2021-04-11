import os
import pdfkit
import webbrowser


content = []
css_content = []
classes = []


def append(line):
    """
    appends given line to document
    """
    content.append(line)


def append_opening_tag(tag_type):
    """
    appends opening tag of given type to document
    """
    processed_line = "<" + tag_type + ">"
    content.append(processed_line)


def append_closing_tag(tag_type):
    """
    appends closing tag of given type to document
    """
    processed_line = "</" + tag_type + ">"
    content.append(processed_line)


def append_title(title):
    """
    appends opening and closing title-tag containing given content to document
    """
    processed_line = "<title>" + title + "</title>"
    content.append(processed_line)


def append_header(line, color, font):
    """
    appends opening and closing header-tag containing given content (in bold & given color) to document
    """
    class_name = "header_" + color + "_" + font
    class_name = class_name.replace(' ', '')

    processed_line = "<h1 class=" + class_name + ">" + line + "</h1>"
    content.append(processed_line)

    if class_name not in classes:
        css = "font-weight: bold; margin-bottom: 0px; color: " + color + "; font-family:" + font + ";"
        append_css_scope(class_name, css)


def append_author(line, color, font):
    """
    appends opening and closing p-tag containing given content (in given color) to document
    """
    class_name = "author_" + color + "_" + font
    class_name = class_name.replace(' ', '')

    processed_line = "<p class=" + class_name + ">by " + line + "</p>"
    content.append(processed_line)

    if class_name not in classes:
        css = "color: " + color + "; font-family:" + font + "; margin-top: 0px;"
        append_css_scope(class_name, css)


def append_paragraph(line, color, font):
    """
    appends opening and closing p-tag containing given content (in given color) to document
    """
    class_name = "paragraph_" + color + "_" + font
    class_name = class_name.replace(' ', '')

    processed_line = "<p class=" + class_name + ">" + line + "</p>"
    content.append(processed_line)

    if class_name not in classes:
        css = "margin-bottom: 6px; margin-top: 6px; color: " + color + "; font-family:" + font + ";"
        append_css_scope(class_name, css)


def append_centered_div(class_name):
    """
    appends a centered div with given class name to document
    """
    processed_line = "<div class=\"" + class_name + "\" style=\"margin: auto; width: 50%;\">"
    content.append(processed_line)


def append_closing_tags():
    """
    appends some common closing tags to document
    """
    append_closing_tag("div")
    append_closing_tag("body")
    append_closing_tag("html")


def append_opening_css_scope(class_name):
    css = "." + class_name + " {"
    css_content.append(css)


def append_closing_css_scope():
    css = "}"
    css_content.append(css)


def append_css_scope(class_name, css):
    global classes
    classes.append(class_name)

    append_opening_css_scope(class_name)
    css_content.append(css)
    append_closing_css_scope()


def write(name):
    """
    generates a html file with given name based on content in document and converts it to pdf
    """
    # write to html
    file = open(os.getcwd() + '/' + name + '.html', 'w')
    for line in content:
        file.write('%s\n' % line)
        if "<style>" in line:
            for css_line in css_content:
                file.write('%s\n' % css_line)
    file.close()

    pdfkit.from_file(name + ".html", name + ".pdf")


def open_document(name):
    """
    opens pdf with given name
    """
    webbrowser.open_new_tab(os.getcwd() + '/' + name + '.pdf')


def generate_document(path, title, process_func):
    """
    generates html file, converts it to pdf and opens it
    """
    append("<!DOCTYPE HTML><html><head><meta charset=\"utf-8\"/>")

    append_title(title)

    append("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>")
    append_opening_tag("style")
    append_closing_tag("style")

    append_closing_tag("head")
    append_opening_tag("body")

    process_func(path, title)

    write(title)
    open_document(title)
