# cli.py
# Import necessary modules and functions
import argparse  # For parsing command-line arguments
from game_logic import play_round, get_computer_choice  # Import game logic functions
from model import Player, Game, Move, engine  # Import SQLAlchemy models and engine
from sqlalchemy.orm import sessionmaker  # For creating a database session

# Create a session object that will allow us to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Define the main function that will run when the script is executed
def main():
    # Create a command-line argument parser with a description
    parser = argparse.ArgumentParser(description="Rock, Paper, Scissors CLI Game")

    # Define a command-line argument for the player's name
    parser.add_argument('player_name', type=str, help="Your name")
    args = parser.parse_args()  # Parse the command-line arguments

    # Create or get the player from the database based on the provided name
    player = session.query(Player).filter_by(name=args.player_name).first()

    if not player:
        # If the player does not exist in the database, create a new player
        player = Player(name=args.player_name)
        session.add(player)  # Add the player to the session
        session.commit()  # Commit the transaction to save the player in the database

    # Start the game loop
    while True:
        # Prompt the player to enter their choice
        player_choice = input("Enter your choice (rock/paper/scissors/q to quit): ").lower()

        if player_choice == 'q':
            break  # Exit the game loop if 'q' is entered
        elif player_choice not in ['rock', 'paper', 'scissors']:
            # Handle invalid input
            print("Invalid choice. Please choose rock, paper, or scissors.")
        else:
            # Call the play_round function to determine the game result
            result = play_round(player_choice)
            # Get the computer's choice
            computer_choice = get_computer_choice()
            # Print the computer's choice and the game result
            print(f"Computer chose {computer_choice}")
            print(result)

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()  # Call the main function to start the game
c