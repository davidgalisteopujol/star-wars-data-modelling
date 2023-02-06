import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class Person(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = True) 
    surname = Column(String(250))
    password = Column(String(7), nullable = True)
    email = Column(String(250), nullable = True)
    suscription_date = Column(Integer, nullable = True)
    # favorites_id = Column(Integer, ForeignKey("favorites.id"))
    # favorites = relationship("Favorites")


class Favorites(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("Person")
    character_id = Column(Integer, ForeignKey("character.id"))
    character = relationship("Character")
    planet_id = Column(Integer, ForeignKey("planet.id"))
    planet = relationship("Planet")
    starship_id = Column(Integer, ForeignKey("starship.id"))
    starship = relationship("Starship")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = True)
    description = Column(String(250), nullable = True) 
    height = Column(Integer, nullable = True)
    mass = Column(Integer, nullable = True)
    hair_color = Column(String(250), nullable = True)
    skin_color = Column(String(250), nullable = True)
    eye_color = Column(String(250), nullable = True)	
    birthday_year = Column(Integer, nullable = True)
    Gender = Column(String(250), nullable = True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = True)
    description = Column(String(250), nullable = True) 
    diameter = Column(Integer, nullable = True)
    rotation_period = Column(Integer, nullable = True)
    orbital_period = Column(Integer, nullable = True)
    gravity = Column(String(250), nullable = True)
    population = Column(Integer, nullable = True)
    climate = Column(String(250), nullable = True)
    terrain = Column(String(250), nullable = True)
    surface_water = Column(Integer, nullable = True)

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = True)
    description = Column(String(250), nullable = True)
    starship_class = Column(String(250), nullable = True)
    manufacturer = Column(String(250), nullable = True)
    cost_in_credits = Column(Integer, nullable = True)
    length = Column(Integer, nullable = True)
    crew = Column(Integer, nullable = True)
    passengers = Column(Integer, nullable = True)
    max_atmosphering_speed = Column(Integer, nullable = True)
    hyperdrive_rating = Column(Integer, nullable = True)
    mglt = Column(Integer, nullable = True)
    cargo_capacity = Column(Integer, nullable = True)
    consumables = Column(Integer, nullable = True)

   
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
