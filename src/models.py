import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class people(Base):
    __tablename__ = 'people'
    name = Column(String(250), primary_key=True, unique=True, nullable=False)
    height = Column(Integer)
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    gender = Column(String(250))
    birth_year = Column(String(250))

class planets(Base):
    __tablename__ = 'planets'
    name = Column(String(250), primary_key=True, unique=True, nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250))
    gravity = Column(String(250))
    water = Column(String(250))
    population = Column(Integer)
    
class vehicles(Base):
    __tablename__ = 'vehicles'
    name = Column(String(250), primary_key=True, unique=True, nullable=False)
    passengers = Column(Integer)
    model = Column(String(250))
    manufacturer = Column(String(250))
    consumables = Column(String(250))
    crew = Column(Integer)

class user(Base):
    __tablename__ = 'user'
    userID = Column(Integer, unique=True, primary_key=True)
    favID = Column(Integer, ForeignKey('favorites.favID'))
    

class favorites(Base):
    __tablename__ = 'favorites'
    userID = Column(Integer, ForeignKey('user.userID'))
    favID = Column(Integer, unique=True, primary_key=True)
    peopleFav = Column(String(250), ForeignKey('people.name'))
    planetFav = Column(String(250), ForeignKey('planets.name'))
    vehicleFav = Column(String(250), ForeignKey('vehicles.name'))
    user = relationship(user)
    planets = relationship(planets)
    people = relationship(people)
    vehicles = relationship(vehicles)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')