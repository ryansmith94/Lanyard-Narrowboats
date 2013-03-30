import tkinter as tk


def window(title, fn):
    win = tk.Tk()
    win.title(title)
    fn(win)
    win.mainloop()
    return win


def list2String(list, separator=", "):
    string = ""
    for value in list:
            string += str(value) + separator
    return string[:-len(separator)]


def displayList(items, listBox):
    listBox.delete(0, tk.END)
    for item in items:
        listBox.insert(tk.END, list2String(item))


def listBox(win, keys, height=20):
    listBox = tk.Listbox(win, selectmode=tk.SINGLE, width=70, height=height)
    listBox.grid(sticky=tk.W + tk.E)
    tk.Label(win, text=list2String(keys)).grid(column=0, sticky=tk.W + tk.E)
    return listBox


def button(win, text, command, row=None, column=None):
    btn = tk.Button(win, text=text, command=command)
    if row is None:
        btn.grid(sticky=tk.W + tk.E, columnspan=2)
    else:
        btn.grid(row=row, column=column, sticky=tk.W + tk.E, columnspan=1)


def label(win, text, row):
    tk.Label(win, text=text).grid(row=row, column=0, sticky=tk.W + tk.E)


def textBox(win, row, column):
    textBox = tk.Entry(win)
    textBox.grid(row=row, column=column, sticky=tk.W + tk.E)
    return textBox


def field(win, fieldName, row):
    label(win, fieldName, row)
    return textBox(win, row, 1)


def form(win, properties, command):
    textBoxes = []
    row = 0
    for prop in properties:
        textBoxes.append(field(win, prop, row))
        row += 1
    button(win, "Submit", command)
    return textBoxes


def dropDown(win, options, command):
    selected = tk.StringVar()
    selected.set(options[0])
    tk.OptionMenu(win, selected, *options, command=command).grid(sticky=tk.W + tk.E)
    return selected


def errorMsg(message):
    tk.messagebox.showerror("Error", message)

END = tk.END
