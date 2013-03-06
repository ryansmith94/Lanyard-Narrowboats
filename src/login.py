import tkinter


def login():
    win = tkinter.Toplevel()
    win.title("success")
    root.withdraw()
    makeLogin(win)


def register():
    pass


def makeLogin(window):
    tkinter.Label(window, text="Enter ID").grid(row=0, column=0, columnspan=2)
    tkinter.Entry(window).grid(row=1, column=0, columnspan=2)
    tkinter.Button(window, text="Login", command=login).grid(row=2, column=0)
    tkinter.Button(window, text="Register", command=register).grid(row=2, column=1)


root = tkinter.Tk()
root.title("Login")
makeLogin(root)
root.mainloop()
