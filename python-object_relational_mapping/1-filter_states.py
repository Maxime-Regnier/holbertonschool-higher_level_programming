#!/usr/bin/python3
"""Script that lists all states with a name starting with N"""

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
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
