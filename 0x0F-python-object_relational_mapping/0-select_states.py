#!/usr/bin/python3
import MySQLdb
from sys import argv, exit


try:
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for data in rows:
        print(data)
    cur.close()
except MySQLdb.Error as e:
    print("MySQL Error:", e)
    exit(1)

db.close()
