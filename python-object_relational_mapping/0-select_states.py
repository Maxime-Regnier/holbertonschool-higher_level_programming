#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Connexion à la base
    conn = MySQLdb.connect(
        host="localhost", 
        port=3306,
        user=username, 
        passwd=password,
        db=database, 
        charset="utf8"
    )
    cur = conn.cursor()

    # Exécuter la requête
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Afficher les résultats
    for row in cur.fetchall():
        print(row)

    # Fermer la connexion
    cur.close()
    conn.close()