
import sqlite3

def createTable():
    
    connection = sqlite3.connect('AccountInfo.db')

    connection.execute("CREATE TABLE Users(AdminId INTEGER NOT NULL UNIQUE PRIMARY KEY, Fullname TEXT NOT NULL CHECK(Fullname!=''), Username TEXT NOT NULL CHECK(Fullname!=''), Password TEXT NOT NULL CHECK(Fullname!=''), email TEXT NOT NULL CHECK(Fullname!=''))")
    connection.commit()
    connection.close()

createTable()
