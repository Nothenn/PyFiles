from tkinter import *

# Testing class based GUI thing, super simple
class Application:

    def __init__(self, master):  # Master means root or main window
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow. This actually worked!")

root = Tk()
x = Application(root)
root.mainloop()
