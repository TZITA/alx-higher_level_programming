#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           port=3306, db=sys.argv[3])
    c = conn.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    rows = c.fetchall()
    for r in rows:
        print(r)