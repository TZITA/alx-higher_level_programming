#!/usr/bin/python3
import sys
import MySQLdb


conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

c = conn.cursor()

c.execute("SELECT * FROM states")
rows = c.fetchall()
for r in rows:
    print(r)
