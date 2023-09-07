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

# import random: This line imports the Python random module, which is used to generate random choices for the computer.

# play_round(player_choice): This function simulates a single round of the game. It takes the player's choice as an argument.

# choices = ['rock', 'paper', 'scissors']: This is a list containing the possible choices in the game.

# computer_choice = random.choice(choices): This line randomly selects a choice from the choices list as the computer's choice.

# The if and elif statements compare the player's choice to the computer's choice to determine the round's result. If the choices are the same, it's a tie. Otherwise, it checks if the player's choice beats the computer's choice based on the rules of the game.

# get_computer_choice(): This function simply returns a random choice for the computer from the choices list.
