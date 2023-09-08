# game_logic.py
import random
from model import Player, Game, Move, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

Session = sessionmaker(bind=engine)
session = Session()

def play_round(player_choice, player_name):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        result = "You win!"
        update_player_wins(player_name)  # Update player's wins
    else:
        result = "Computer wins!"

    # Record the game result in the database
    record_game(player_name, player_choice, computer_choice, result)

    return result

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def update_player_wins(player_name):
    player = session.query(Player).filter_by(name=player_name).first()
    if player:
        player.wins += 1
        session.commit()

def record_game(player_name, player_choice, computer_choice, result):
    player = session.query(Player).filter_by(name=player_name).first()
    if player:
        game = Game(player=player, result=result)
        session.add(game)
        session.commit()

def get_game_history(player_name):
    player = session.query(Player).filter_by(name=player_name).first()
    if player:
        games = session.query(Game).filter_by(player=player).all()
        return games
    return []

def get_player_wins(player_name):
    player = session.query(Player).filter_by(name=player_name).first()
    if player:
        return player.wins
    return 0

# import random: This line imports the Python random module, which is used to generate random choices for the computer.

# play_round(player_choice): This function simulates a single round of the game. It takes the player's choice as an argument.

# choices = ['rock', 'paper', 'scissors']: This is a list containing the possible choices in the game.

# computer_choice = random.choice(choices): This line randomly selects a choice from the choices list as the computer's choice.

# The if and elif statements compare the player's choice to the computer's choice to determine the round's result. If the choices are the same, it's a tie. Otherwise, it checks if the player's choice beats the computer's choice based on the rules of the game.

# get_computer_choice(): This function simply returns a random choice for the computer from the choices list.
