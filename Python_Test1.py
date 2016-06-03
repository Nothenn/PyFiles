class Item: #define a class object
    def setName (self,value): #define class methods
        self.name = value #self ID particular instance
    def display(self):
        print self.name; #prints data dor a particular instance

x = Item()
y = Item()
z = Item()

x.setName("Helo, this is python book.")
y.setName("I am a quick learner.")
z.setName("Books.")

x.display()
y.display()
z.display()
