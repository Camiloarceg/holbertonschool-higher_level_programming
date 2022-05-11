#!/usr/bin/python3
"""script that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
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
    myState = State(name='California')
    myCity = City(name='San Francisco')
    myState.cities.append(myCity)
    session.add_all([myState])
    session.commit()
