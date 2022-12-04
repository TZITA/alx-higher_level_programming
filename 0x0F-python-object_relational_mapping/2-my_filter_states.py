#!/usr/bin/python3
"""Displays all values in states table where name matches argument."""
import sys
import MySQLdb

if __name__ == '__main__':
    co = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = co.cursor()

    c.execute("SELECT * FROM states WHERE name = '{}' ORDER BY states.id".
              format(sys.argv[4]))
    for st in c.fetchall():
        print(st)
