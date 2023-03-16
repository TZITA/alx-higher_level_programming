#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)."""
import sys
import MySQLdb

if __name__ == '__main__':
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = con.cursor()
    c.execute("SELECT * FROM states WHERE name REGEXP '^N' ORDER BY states.id ASC")
    [print (state) for state in c.fetchall()]
