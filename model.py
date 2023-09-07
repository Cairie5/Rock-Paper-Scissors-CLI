# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)

class Move(Base):
    __tablename__ = 'moves'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    game_id = Column(Integer, ForeignKey('games.id'))
    choice = Column(String)

engine = create_engine('sqlite:///game.db')
Base.metadata.create_all(engine)
