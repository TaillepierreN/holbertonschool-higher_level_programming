#!/usr/bin/python3
"""
Script that list all states from database hbtn_0e_0_usa..
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Main execution block
    connect to mysql database and list states by ID ascending.
    """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
