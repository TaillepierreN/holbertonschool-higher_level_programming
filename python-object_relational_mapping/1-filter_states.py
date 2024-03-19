#!/usr/bin/python3
"""
Script that list all states from database hbtn_0e_0_usa starting with N
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Main execution block
    connect to mysql database and list states starting with N by ID ascending.
    """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
