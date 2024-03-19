#!/usr/bin/python3
"""
Script that list all cities from database hbtn_0e_4_usa part of
the state argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Main execution block
    connect to mysql database and list cities from the state argument
    """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    query = "SELECT cities.name FROM cities JOIN states ON states.id = cities.state_id \
        WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))
