import sqlite3
connection = sqlite3.connect("Hand_Tools.database")
cursor = connection.cursor();


def data_input():
    try:
        cursor.execute("""CREATE TABLE Tools (id INTEGER PRIMARY KEY, name TEXT, size TEXT, price INTEGER)""")
        for item in((None,"Book","Small",15),(None,"Pois","Medium",35),(None,"Bayg","Large",69),):cursor.execute ("INSERT INTO Tools VALUES(?,?,?,?)",item)
        connection.commit()
        cursor.close()
    except sqlite3.OperationalError:pass


data_input()

cursor.execute("SELECT name, size, price FROM Tools")
toolsTuple = cursor.fetchall()

for row in toolsTuple: name, size, price = row
x = ("%s, %s, %d"%(name, size, price))
print (x)
