#!/usr/bin/python3
"""script that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_parameters = {
            "host": "localhost",
            "port": 3306,
            "user": sys.argv[1],
            "pass": sys.argv[2],
            "db": sys.argv[3]
            }
    engine = create_engine('mysql+mysqldb://{user}:{pass}@{host}:{port}/{db}'
                           .format(**db_parameters), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(State(name='Louisiana'))
    session.commit()
    result = session.query(State).filter(State.name.like('Louisiana')).all()
    for states in result:
        print("{}".format(states.id))
