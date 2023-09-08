# models.py
# Import necessary modules and functions from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the Player class representing the 'players' table in the database
class Player(Base):
    __tablename__ = 'players'  # Table name in the database
    id = Column(Integer, primary_key=True)  # Primary key column for player's unique ID
    name = Column(String, unique=True)  # Column to store the player's name

# Define the Game class representing the 'games' table in the database
class Game(Base):
    __tablename__ = 'games'  # Table name in the database
    id = Column(Integer, primary_key=True)  # Primary key column for game's unique ID

# Define the Move class representing the 'moves' table in the database
class Move(Base):
    __tablename__ = 'moves'  # Table name in the database
    id = Column(Integer, primary_key=True)  # Primary key column for move's unique ID
    player_id = Column(Integer, ForeignKey('players.id'))  # Foreign key referencing the player
    game_id = Column(Integer, ForeignKey('games.id'))  # Foreign key referencing the game
    choice = Column(String)  # Column to store the player's choice (rock, paper, scissors)

# Create an SQLite database engine with the name 'game.db'
engine = create_engine('sqlite:///game.db')

# Create the database tables based on the class definitions (metadata)
Base.metadata.create_all(engine)

# Base is a base class provided by SQLAlchemy for declarative class definitions.

# The Player class represents the 'players' table and has columns for id (primary key) and name.

# The Game class represents the 'games' table and has a column for id (primary key).

# The Move class represents the 'moves' table and has columns for id, player_id (foreign key referencing a player), game_id (foreign key referencing a game), and choice to store the player's choice in the game.

# Finally, it creates an SQLite database engine named 'game.db' and uses the create_all method to create the corresponding database tables based on the class definitions in the Base.metadata.

# game_logic.py provides the core logic for playing a single round of the Rock, Paper, Scissors game and determining the result of the round.