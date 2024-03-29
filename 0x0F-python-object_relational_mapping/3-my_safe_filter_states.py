#!/usr/bin/python3
"""
displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
from sys import argv, exit

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states where name LIKE '{}'".format(argv[4]))
    rows = cur.fetchall()

    state_name = argv[4]
    for data in rows:
        if (state_name == data[1]):
            print(data)
    cur.close()
    db.close()
