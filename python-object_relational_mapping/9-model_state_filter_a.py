#!/usr/bin/python3
"""
Script to list all states containing an 'a' in hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    """
    Main execution code
    Check Argv
    Create an engine to connect to a MySQL server
    Create with Factory function sessionmaker a work area
    with engine binded foR execution of SQL statements
    QuEry the State class representing a table
    anD print all entry containing 'a' in the table

    """
    if len(argv) == 4:
        username, password, db_name = argv[1:4]

        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name), pool_pre_ping=True)

        DBsession = sessionmaker(bind=engine)
        session = DBsession()

        states = session.query(State).filter(State.name.like('%a%')).order_by(
            State.id)

        for state in states:
            print("{}: {}".format(state.id, state.name))

    else:
        print("Usage: {} <username> <password> <db_name>".format(argv[0]))
