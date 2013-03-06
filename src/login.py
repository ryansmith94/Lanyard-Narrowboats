from tkinter import *

def login():
    win = Toplevel()
    win.title("success")
    root.withdraw()
    makeLogin(win)

def register():
    pass

def makeLogin(window):
    Label(window, text="Enter ID").grid(row=0, column=0, columnspan=2)
    Entry(window).grid(row=1, column=0, columnspan=2)
    Button(window, text="Login", command=login).grid(row=2, column=0)
    Button(window, text="Register", command=register).grid(row=2, column=1)

root=Tk()
root.title("Login")
makeLogin(root)
root.mainloop()
