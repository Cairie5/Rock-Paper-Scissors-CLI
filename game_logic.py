# game_logic.py
import random  # Import the 'random' module to generate random choices

# Define a function to play a single round of the Rock, Paper, Scissors game
def play_round(player_choice):
    choices = ['rock', 'paper', 'scissors']  # List of possible choices
    computer_choice = random.choice(choices)  # Randomly select the computer's choice

    # Determine the result of the round based on player and computer choices
    if player_choice == computer_choice:
        return "It's a tie!"  # If both choices are the same, it's a tie
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"  # Player wins if they beat the computer's choice
    else:
        return "Computer wins!"  # Computer wins if none of the above conditions are met

# Define a function to get the computer's random choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']  # List of possible choices
    return random.choice(choices)  # Return a randomly chosen choice for the computer
