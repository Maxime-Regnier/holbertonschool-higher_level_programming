#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Récupération des arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_to_search = sys.argv[4]

    # Connexion à la base de données
    # Utilisation de localhost et du port 3306 comme demandé
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, db_name),
                           pool_pre_ping=True)

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête avec filtre sur le nom
    # SQLAlchemy gère automatiquement la protection contre l'injection SQL
    # dans les filtres d'objets.
    state = session.query(State).filter(State.name == state_to_search).first()

    # Affichage du résultat
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Fermeture de la session
    session.close()