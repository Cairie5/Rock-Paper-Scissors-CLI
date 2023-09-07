# cli.py
import argparse
from game_logic import play_round, get_computer_choice
from model import Player, Game, Move, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def main():
    parser = argparse.ArgumentParser(description="Rock, Paper, Scissors CLI Game")
    parser.add_argument('player_name', type=str, help="Your name")
    args = parser.parse_args()

    # Create or get the player
    player = session.query(Player).filter_by(name=args.player_name).first()
    if not player:
        player = Player(name=args.player_name)
        session.add(player)
        session.commit()

    while True:
        player_choice = input("Enter your choice (rock/paper/scissors/q to quit): ").lower()

        if player_choice == 'q':
            break
        elif player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
        else:
            result = play_round(player_choice)
            print(f"Computer chose {get_computer_choice()}")
            print(result)

if __name__ == "__main__":
    main()
