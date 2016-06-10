class Item: #define a class object
    def setName (self,value): #define class methods
        self.name = value #self ID particular instance
    def display(self):
        print self.name; #prints data dor a particular instance

x = Item() #Defines x,y,and z to be "Items"
y = Item()
z = Item()

x.setName("Helo, this is python book.") #Sets the "name" of the values that
y.setName("I am a quick learner.")#are to be printed
z.setName("Books.")

x.display() #displays the set name
y.display()
z.display()
