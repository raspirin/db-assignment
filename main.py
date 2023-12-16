import sqlite3 as sql

con = sql.connect('database.db')
cur = con.cursor()
res = cur.execute("SELECT * FROM BUS")