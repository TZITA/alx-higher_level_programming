#!/usr/bin/python3
"""Displays values in states where name=arg(Safe from MySQL injections)"""
import sys
import MySQLdb

if __name__ == '__main__':
    co = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = co.cursor()
    c.execute("SELECT * FROM states")
    [print(st) for st in c.fetchall() if st[1] == sys.argv[4]]
