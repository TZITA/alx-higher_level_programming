#!/usr/bin/python3
"""Lists all cities of that state, using the database hbtn_0e_4_usa."""
import sys
import MySQLdb


if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = conn.cursor()
    c.execute("SELECT c.id, c.name, s.name \
            FROM cities AS c \
            INNER JOIN states AS s \
            ON c.state_id = s.id \
            ORDER BY c.id")
    cc = []
    for city in c.fetchall():
        if city[2] == sys.argv[4]:
            cc.append(city[1])
    print(", ".join(cc))
