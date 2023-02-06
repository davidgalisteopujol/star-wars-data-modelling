import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
import enum

Base = declarative_base()

class Media_enum(enum.Enum):
    imagen = "imagen",
    video = "video"

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = True) 
    surname = Column(String(250))
    password = Column(String(7), nullable = True)
    email = Column(String(250), nullable = True)
    suscription_date = Column(Integer, nullable = True)
    

class Favorites(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post")

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")
    text = Column(String(250))
    date = Column(String(8), nullable = True)
    media = Column(String, ForeignKey("media.id"))
    media = relationship("Media")

class Saved(Base):
    __tablename__ = "saved"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post")

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key = True)
    type = Column(Enum(Media_enum))
    url = Column(String, nullable = True)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post")

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key = True)
    comment_text = Column(String(250), nullable = True)
    date = Column(String(8), nullable = True)
    author_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post")

class Follower(Base):
    __tablename__ = "follower"
    id = Column(Integer, primary_key = True)
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")
    user_to_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
