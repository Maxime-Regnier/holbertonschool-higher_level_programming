#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from database hbtn_0e_0_usa.

This module connects to a MySQL database and displays all states whose names
begin with the uppercase letter N, sorted by their id in ascending order.

Takes 3 command-line arguments:
    - MySQL username
    - MySQL password
    - Database name
""" 

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE SUBSTR(name, 1, 1) = 'N' ORDER BY id ASC")

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
