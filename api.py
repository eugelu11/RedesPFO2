import sqlite3
import os

PATH_APP = os.getcwd()
PATH_BBDD = PATH_APP + '/miBBDD.db'

con = sqlite3.connect(PATH_BBDD)
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER)")
con.commit()
con.close()
