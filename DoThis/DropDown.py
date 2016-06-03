from tkinter import *

def doNothing():
    print("These are some mental words")

root = Tk()

men = Menu(root)
root.config(menu=men)

subMen = Menu(men)
men.add_cascade(label="File", menu=subMen)
subMen.add_command(label="New", command=doNothing)
subMen.add_separator()
subMen.add_command(label="Anus", command=doNothing)


editMen = Menu(men)
men.add_cascade(label="Anusol", menu=editMen)
editMen.add_command(label="Anus", command=doNothing)

root.mainloop()