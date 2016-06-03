import sys
import sqlite3
con = sqlite3.connect("Hand_Tools.database")

c = con.cursor()

c.execute("SELECT name, size, price FROM Tools")
toolsTuple = c.fetchall()

for row in toolsTuple: name, size, price = row
x = ("%s, %s, %d"%(name, size, price))
print (x)


