#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
Usage: ./4-cities_by_state.py <username> <password> <database>
Results are sorted by cities.id in ascending order
"""

import MySQLdb  # type: ignore
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Execute the query to select all cities with their state names
    # Using JOIN to get the state name instead of state_id
    cursor.execute("""SELECT cities.id, cities.name, states.name 
                      FROM cities 
                      JOIN states ON cities.state_id = states.id 
                      ORDER BY cities.id ASC""")

    # Fetch all results and print each row
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()