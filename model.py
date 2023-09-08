# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    wins = Column(Integer, default=0)  # New column to track wins

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())  # Timestamp for game
    player_id = Column(Integer, ForeignKey('players.id'))
    player = relationship('Player')
    result = Column(String)  # New column to record game result

class Move(Base):
    __tablename__ = 'moves'
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship('Game')
    choice = Column(String)

engine = create_engine('sqlite:///game.db')
Base.metadata.create_all(engine)


# Base is a base class provided by SQLAlchemy for declarative class definitions.

# The Player class represents the 'players' table and has columns for id (primary key) and name.

# The Game class represents the 'games' table and has a column for id (primary key).

# The Move class represents the 'moves' table and has columns for id, player_id (foreign key referencing a player), game_id (foreign key referencing a game), and choice to store the player's choice in the game.

# Finally, it creates an SQLite database engine named 'game.db' and uses the create_all method to create the corresponding database tables based on the class definitions in the Base.metadata.

# game_logic.py provides the core logic for playing a single round of the Rock, Paper, Scissors game and determining the result of the round.