# cli.py
import argparse
from game_logic import play_round, get_computer_choice, get_game_history, get_player_wins
from model import Player, Game, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def main():
    parser = argparse.ArgumentParser(description="Rock, Paper, Scissors CLI Game")
    parser.add_argument('player_name', type=str, help="Your name")
    args = parser.parse_args()

    player = session.query(Player).filter_by(name=args.player_name).first()
    if not player:
        player = Player(name=args.player_name)
        session.add(player)
        session.commit()

    while True:
        player_choice = input("Enter your choice (rock/paper/scissors/q to quit): ").lower()

        if player_choice == 'q':
            break
        elif player_choice == 'history':
            display_game_history(args.player_name)
        elif player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, scissors, or q to quit.")
        else:
            result = play_round(player_choice, args.player_name)
            print(f"Computer chose {get_computer_choice()}")
            print(result)

def display_game_history(player_name):
    games = get_game_history(player_name)
    if not games:
        print("No game history found.")
    else:
        print("\nGame History:")
        for game in games:
            print(f"Timestamp: {game.timestamp}, Result: {game.result}")
        print(f"Total Wins: {get_player_wins(player_name)}")

if __name__ == "__main__":
    main()

# this codes set up a command-line interface (CLI) for the Rock, Paper, Scissors game using argparse for command-line argument parsing and SQLAlchemy for database operations. It allows players to enter their name, play the game, and stores player information in a database. The game loop continues until the player chooses to quit by entering 'q'.