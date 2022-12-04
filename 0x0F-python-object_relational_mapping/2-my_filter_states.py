#!/usr/bin/python3
"""Displays all values in states table where name matches argument."""
import sys
import MySQLdb

conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

c = conn.cursor()
c.execute("SELECT * FROM states WHERE name = '{}'".format(sys.argv[4]))
for st in c.fetchall():
    print(st)
