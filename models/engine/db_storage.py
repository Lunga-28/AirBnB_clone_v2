#!/usr/bin/python3
"""DBStorage class that sets up SQLAlchemy and connects with database"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {
    "User": User,
    "State": State,
    "Place": Place,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}

class DBStorage:
    """Database storage
    Attributes:
        __engine (SQLAlchemy.Engine): the engine for the database
        __session (SQLAlchemy.Session): the current session
    """
    __engine = None
    __session = None

    def __init__(self):
        """Database initailisations"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                               getenv("HBNB_MYSQL_USER"),
                               getenv("HBNB_MYSQL_PWD"),
                               getenv("HBNB_MYSQL_HOST"),
                               getenv("HBNB_MYSQL_DB"), pool_pre_ping=True))
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return a dictionary of objects of type 'cls'
           or return all objects if cls is None
        """

        dct = {}
        if type(cls) == str:
            cls = eval(cls)

        if cls is None:
            for c in classes.values():
                objs = self.__session.query(c).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dct[key] = obj

        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                dct[key] = obj

        return dct

    def new(self, obj):
        """Add object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes on the current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from current session if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all database tables and initialise session"""
        Base.metadata.create_all(self.__engine)
        my_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(my_session)
        self.__session = Session()

    def close(self):
        """call remove method"""
        self.__session.close()
