#!/usr/bin/python3
"""
    Python file that contains the class definition of a State and an instance
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State class inherits from Base
    """
    __tablename__ = 'states'
    cities = relationship("City", cascade="all, delete")
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
