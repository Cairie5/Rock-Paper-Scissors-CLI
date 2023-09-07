# game_logic.py
import random

def play_round(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Base is a base class provided by SQLAlchemy for declarative class definitions.
# The Player class represents the 'players' table and has columns for id (primary key) and name.
# The Game class represents the 'games' table and has a column for id (primary key).
# The Move class represents the 'moves' table and has columns for id, player_id (foreign key referencing a player), game_id (foreign key referencing a game), and choice to store the player's choice in the game.
# Finally, it creates an SQLite database engine named 'game.db' and uses the create_all method to create the corresponding database tables based on the class definitions in the Base.metadata.