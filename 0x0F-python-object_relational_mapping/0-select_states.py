#!/usr/bin/python3
import MySQLdb


conn = MySQLdb.connect(host='localhost', user='root',
                       passwd='tomzita123$', db='hbtn_0e_0_usa')

c = conn.cursor()

c.execute("SELECT * FROM states")
rows = c.fetchall()
for r in rows:
    print(r)
