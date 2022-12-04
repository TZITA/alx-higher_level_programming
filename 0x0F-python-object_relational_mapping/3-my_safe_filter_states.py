#!/usr/bin/python3
"""Displays values in states where name matches argument. Safe from MySQL injections!"""
import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = conn.cursor()
    c.execute("SELECT * FROM states")
    [print(st) for st in c.fetchall() if st[1] == sys.argv[4]]
