#!/usr/bin/python3
"""
Script that list all states from database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    connect to mysql database and list states by ID ascending
    username: user name for the db
    password: password for the db
    dbname database name to connect to
    """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
