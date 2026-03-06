#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>
Results are sorted by states.id in ascending order
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and state name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server on localhost, port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Use format to create the SQL query with user input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(state_name)

    # Execute the query
    cursor.execute(query)

    # Fetch all results and print each row
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()
