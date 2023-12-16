import sqlite3 as sql
from lib import *

con = sql.connect('database.db')
cur = con.cursor()
add_customer(cur, "zhang3")
res = cur.execute("SELECT * FROM CUSTOMERS")
print(res.fetchall())
