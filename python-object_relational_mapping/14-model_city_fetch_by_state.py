#!/usr/bin/python3
"""
Script to print all cities in hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    """
    Main execution code
    Check Argv
    Create an engine to connect to a MySQL server
    Create with Factory function sessionmaker a work area
    with engine binded foR execution of SQL statements
    QuEry the state with the letter 'a'
    Select and Delete the states

    """
    if len(argv) == 4:
        username, password, db_name = argv[1:4]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name), pool_pre_ping=True)

        DBsession = sessionmaker(bind=engine)
        session = DBsession()

        cities_with_states = session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id).all()

        for state, city in cities_with_states:
            print("{}: ({}) {}".format(state.name, city.id, city.name))

    else:
        print("Usage: {} <username> <password>  \
              <db_name>".format(argv[0]))
