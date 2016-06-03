from tkinter import *
from tkinter import font
# Testing class based GUI thing, super simple


class Application:

    def __init__(self):  # Master means root or main window
        root = Tk()
        frame = Frame(root, borderwidth=10, bg="#40E0D0")
        frame.pack()

        self.colour = "#40E0D0"
        self.customFont = ("Helvetica", 18)

        self.userLabel = Label(frame, text="User: ", font=self.customFont, bg=self.colour).grid(row=0)
        self.passLabel = Label(frame, text="Pass: ", font=self.customFont, bg=self.colour).grid(row=1)

        self.userNameInput = Entry(frame, font=self.customFont)
        self.passInput = Entry(frame, font=self.customFont)
        self.submitButton = Button(frame, text="Submit", command=lambda: self.printmessage(self.userNameInput.get(), self.passInput.get()))

        self.userNameInput.grid(row=0,column=1)
        self.passInput.grid(row=1,column=1)
        self.submitButton.grid(row=2,columnspan=2, pady=10)

        root.mainloop()

    def printmessage(self, nameIn, passIn):
        print("Name: " + nameIn)
        print("Pass: " + passIn)

app = Application()
