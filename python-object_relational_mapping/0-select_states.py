#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <username> <password> <database>
Results are sorted by states.id in ascending order
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor and execute query
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    # Fetch all results and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()