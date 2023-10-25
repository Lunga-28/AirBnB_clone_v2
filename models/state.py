#!/usr/bin/python3
'''
    Implementation of the State class
'''
from models import storage
from models.city import City
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """ State table
    Attributes:
        __tablename__: the database table
        name: state name
        cities: Defines a relationship to the cities table
     """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get the cities whose states ids correspond to the current state
            """
            city_list = []

            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
