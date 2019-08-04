import sqlite3
def createTable():
    connection = sqlite3.connect('Artworks.db')
    connection.execute("CREATE TABLE Artworks(ArtId INTEGER NOT NULL PRIMARY KEY, Title TEXT NOT NULL, Genre TEXT NOT NULL, MemId NUMBER NOT NULL, Price FLOAT NOT NULL)")
    connection.execute("INSERT INTO Artworks VALUES(1001, 'Taj Mahal', 'Oil Painting', 101, 7000)")
    connection.execute("INSERT INTO Artworks VALUES(1002, 'Dance', 'Oil Painting', 102, 9000)")
    connection.execute("INSERT INTO Artworks VALUES(1003, 'The Mind', 'Abstract Art', 103, 10000)")
    connection.execute("INSERT INTO Artworks VALUES(1004, 'Rainy season', 'Dot Art', 102, 8500)")
    connection.execute("INSERT INTO Artworks VALUES(1005, 'Rainbow', 'Dot Art', 104, 9000)")
    connection.execute("INSERT INTO Artworks VALUES(1006, 'Mysteries', 'Abstract Art', 105, 10000)")
    connection.execute("INSERT INTO Artworks VALUES(1007, 'Waterfalls', '3D Art', 106, 6700)")
    connection.commit()
    connection.close()

createTable()
