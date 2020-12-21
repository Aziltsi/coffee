import sqlite3

con = sqlite3.connect('coffee.sqlite')
cur = con.cursor()
cur.execute("""SELECT * from information WHERE name = ?""", (sort, )).fetchall()
con.commit()
con.close()