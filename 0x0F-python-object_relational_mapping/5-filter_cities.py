#!/usr/bin/python3
import MySQLdb
from sys import argv, exit


try:
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("""SELECT cities.name
                    FROM cities INNER JOIN states
                    ON cities.state_id = states.id
                    WHERE states.name = '{}'""".format(argv[4]))
    rows = cur.fetchall()

    cities = ", ".join(row[0] for row in rows)

    print(cities)
    cur.close()
except MySQLdb.Error as e:
    print("MySQL Error:", e)
    exit(1)

db.close()
