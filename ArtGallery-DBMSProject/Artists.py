import sqlite3
def createTable():
    connection = sqlite3.connect('Artists.db')
    connection.execute("CREATE TABLE Artists(MemId INTEGER NOT NULL PRIMARY KEY, FullName TEXT NOT NULL, Pincode NUMBER NOT NULL,PhNo NUMBER NOT NULL)")
    connection.execute("INSERT INTO Artists VALUES(101, 'Robert Gills', '600061', 9792342545)")
    connection.execute("INSERT INTO Artists VALUES(102, 'Jack Jhonson', '600036', 9863552545)")
    connection.execute("INSERT INTO Artists VALUES(103, 'Roshini Gourav', '625706', 9734266937)")
    connection.execute("INSERT INTO Artists VALUES(104, 'Sally Sanders', '600019', 9240778485)")
    connection.execute("INSERT INTO Artists VALUES(105, 'Darrell Rivers', '132113', 552247092)")
    connection.execute("INSERT INTO Artists VALUES(106, 'Meena Patel', '825408', 8242147092)")
    connection.execute("INSERT INTO Artists VALUES(107, 'Neeti Rakesh', '110002', 9249247092)")
    connection.commit()
    connection.close()

createTable()
