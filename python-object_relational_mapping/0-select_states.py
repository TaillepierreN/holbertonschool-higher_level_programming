#!/usr/bin/python3
import MySQLdb
import sys
"""
Script that list all states from database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    """
    connect to mysql database and list states by ID ascending
    username: user name for the db
    password: password for the db
    dbname database name to connect to
    """
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], database=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
