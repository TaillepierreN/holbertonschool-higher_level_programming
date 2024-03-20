#!/usr/bin/python3
"""
Script to update the state with id 2 to new mexico in hbtn_0e_6_usa
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
    QuEry the state with id 2
    UpDate the name of the state

    """
    if len(argv) == 4:
        username, password, db_name = argv[1:4]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name), pool_pre_ping=True)

        DBsession = sessionmaker(bind=engine)
        session = DBsession()

        state = session.query(State).filter(State.id == 2).first()
        if state:
            state.name = 'New Mexico'
            session.commit()

    else:
        print("Usage: {} <username> <password>  \
              <db_name>".format(argv[0]))
