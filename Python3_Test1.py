class Item: #define a class object
    def setName (self,value): self.name = value #define class methods
def display(self):
            print (self.name); #prints data or a particular instance

x = Item()
y = Item()
z = Item()

x.setName("Hello, this is python book.")
y.setName("I am a quick learner.")
z.setName("Books.")

x.display()
