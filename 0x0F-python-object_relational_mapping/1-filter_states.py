#!/usr/bin/python3
# Lists all states with a name starting with N (upper N)
import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = conn.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    for state in c.fetchall():
        print(r)
