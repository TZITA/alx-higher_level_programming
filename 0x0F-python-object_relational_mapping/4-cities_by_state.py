#!/usr/bin/python3
import sys
import MySQLdb


if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = conn.cursor()
    c.execute("SELECT c.id, c.name, s.name \
            FROM states AS s \
            INNER JOIN cities \
            AS c ON s.id = c.state_id \
            ORDER BY c.id")
    [print(city) for city in c.fetchall()]
