# Testing __init__


class Application:

    def __init__(self, num):  # Master means root or main window
        self.num = num


z = input("Enter a number: ")
x = Application(z)
print(x.num)