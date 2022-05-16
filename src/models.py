import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    member_since = Column(String, nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    climate = Column(String, nullable=False)
    population = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    rotation_perios = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_year = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    height = Column(Integer, nullable=False)
    eye_color = Column(String, nullable=False)
    hair_color = Column(String, nullable=False)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    model = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    vehicle_class = Column(String, nullable=False)

class FavCharacters(Base):
    __tablename__ = 'fav_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    characters_id = Column(Integer, ForeignKey("characters.id"))
    user = relationship(User)
    characters = relationship(Characters)

class FavVehicles(Base):
    __tablename__ = 'fav_vehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    vehicles_id = Column(Integer, ForeignKey("vehicles.id"))
    user = relationship(User)
    vehicles = relationship(Vehicles)

class FavPlanets(Base):
    __tablename__ = 'fav_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    planet_id = Column(Integer, ForeignKey("planets.id"))
    user = relationship(User)
    planets = relationship(Planets)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')