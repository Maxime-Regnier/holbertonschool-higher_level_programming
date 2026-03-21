#!/usr/bin/python3
"""
Script that takes in the name of a state and lists all cities of that state
Usage: ./5-filter_cities.py <username> <password> <database> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Using parameterized query to prevent SQL injection
    cursor.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state_name,)
    )

    rows = cursor.fetchall()

    # Format output as comma-separated city names
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cursor.close()
    db.close()
