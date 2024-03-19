#!/usr/bin/python3
#!/usr/bin/python3
"""
Script that list all states from database hbtn_0e_0_usa
where name matches the argument safely
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Main execution block
    connect to mysql database and list states by ID ascending.
    use a placeholded for the user input, and input value
    is passed as an argument to execute in a tuple to make 
    sure it is handled as a value,not part of the sql command
    """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE \
        name LIKE BINARY %s ORDER BY id ASC"
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
