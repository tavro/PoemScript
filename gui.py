from tkinter import *
import os

root = Tk()
root.title('PoemScript Engine')
root.iconbitmap(os.getcwd() + '/resources/poem_script_icon.ico')

editor = LabelFrame(root, text="PoemScript Editor")
editor.grid(row=0, column=0, padx=8, pady=8)

result = LabelFrame(root, text="Output")
result.grid(row=0, column=1, padx=8, pady=8)


def compile():
    title = Label(result, text="Result", width=64)
    title.grid(row=0, column=0)

    content = Label(result, text=entry.get())
    content.grid(row=1, column=0)


button = Button(editor, text="Compile", command=compile)
button.grid(row=0, column=0)

entry = Entry(editor, width=64)
entry.grid(row=1, column=0)

current_line = 1
line_amount = 1
line_label = Label(editor, text="Line " + str(current_line) + " of " + str(line_amount), relief=SUNKEN, anchor=W)
line_label.grid(row=2, column=0, sticky=W+E)

root.mainloop()
