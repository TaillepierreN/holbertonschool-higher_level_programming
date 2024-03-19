#!/usr/bin/python3
import MySQLdb
import sys
"""
Script that list all states from database hbtn_0e_0_usa
"""


def select_states(username, password, dbname):
    """
    connect to mysql database and list states by ID ascending
    username: user name for the db
    password: password for the db
    dbname database name to connect to
    """
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, password=password, database=dbname)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        select_states(username, password, dbname)
    else:
        print("expected arguments: username password dbname")
