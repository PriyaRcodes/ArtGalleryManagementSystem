import sqlite3

def createTable():
    connection = sqlite3.connect('ExhibitonsReport.db')
    connection.execute("DROP TABLE Exhibitions")
    connection.execute("CREATE TABLE Exhibitions(ExCount INTEGER NOT NULL PRIMARY KEY, Theme TEXT NOT NULL, Pincode NUMBER NOT NULL,PhNo NUMBER NOT NULL, FromDate TEXT NOT NULL, ToDate TEXT NOT NULL)")
    connection.execute("INSERT INTO Exhibitions VALUES(820, 'Tiny Art', '600061', 9799132545, '2018-02-23', '2018-02-27')")
    connection.execute("INSERT INTO Exhibitions VALUES(821, '3D Art', '600081', 9863142545,'2018-04-26','2018-04-28')")
    connection.execute("INSERT INTO Exhibitions VALUES(822, 'Famous Landmarks', '600038', 9799112937,'2018-05-26','2018-05-28')")
    connection.execute("INSERT INTO Exhibitions VALUES(823, 'Local Inspiration', '600019', 9240238485,'2018-06-26','2018-06-29')")
    connection.execute("INSERT INTO Exhibitions VALUES(824, 'Infinity', '600045', 649247092,'2018-08-23','2018-08-27')")
    connection.execute("INSERT INTO Exhibitions VALUES(825, 'Universe', '603210', 8249247092,'2018-10-20','2018-10-23')")
    connection.execute("INSERT INTO Exhibitions VALUES(826, 'Bio Diversity', '603210', 1249247092,'2018-11-24','2018-11-28')")
    connection.commit()
    connection.close()

createTable()
