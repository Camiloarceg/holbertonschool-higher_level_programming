#!/usr/bin/python3
"""
    Python file that contains the class definition of a City and an instance
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import State, Base


class City(Base):
    """ City class inherits from Base
    """
    __tablename__ = 'cities'
    states = relationship("State", overlaps="cities")
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
