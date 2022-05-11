#!/usr/bin/python3
"""script 14-model_city_fetch_by_state.py that prints all City
    objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
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
    result = session.query(State, City).filter(
        City.state_id == State.id).order_by(City.id).all()
    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
