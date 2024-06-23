#!/usr/bin/python3
"""

Script that lists all states that matches name

"""

import sys
import MySQLdb

if __name__ == "__main__":
    connection = MySQLdb.connect(
        host='localhost', port=3306, user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities \
         INNER JOIN states ON cities.state_id = states.id \
         WHERE state.name=%s ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], end="")
        if row != rows[-1]:
            print(", ", end="")
    cursor.close()
    connection.close()
