/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa."""
import sys
import MySQLdb


if __name__ == '__main__':
    co = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = co.cursor()
    c.execute("SELECT c.id, c.name, s.name \
            FROM states AS s \
            INNER JOIN cities \
            AS c ON s.id = c.state_id \
            ORDER BY c.id")
    [print(city) for city in c.fetchall()]
