# Rock-Paper-Scissors-CLI
Welcome to the Rock, Paper, Scissors CLI Game! This project is a command-line interface (CLI) implementation of the classic Rock, Paper, Scissors game using Python. Challenge the computer to a game and see who wins!

## Table of Contents
Description
Features
Requirements
Installation
Usage
Project Structure
Contributing
License

## Features
Play Rock, Paper, Scissors against the computer in the command line.

## Requirements
Before you start, ensure you have met the following requirements:

. Python 3.x installed on your system.
. Pipenv for managing virtual environments (you can install it using pip).

## Installation
Clone this repository to your local machine:

```bash
git clone git@github.com:Cairie5/Rock-Paper-Scissors-CLI.git
```

Navigate to the project directory:

```bash
cd Rock-Paper-Scissors-CLI
```

Create and activate a virtual environment using Pipenv:

```bash
pipenv install
pipenv shell
```
## Usage
To play the Rock, Paper, Scissors CLI game, follow these steps:

1. Run the game by executing the cli.py script with your name as an argument:

```bash
python cli.py <your_name>
```

2. Follow the on-screen instructions to choose between rock, paper, or scissors. Enter your choice when prompted.

3. The game will display the result of each round and keep track of your game.

4. To quit the game, enter 'q' when prompted for your choice.

## Project Structure
The project directory is organized as follows:

cli.py: The main CLI script for playing the game.
game_logic.py: Contains the game logic for playing rounds and determining the winner.
models.py: Defines the database schema using SQLAlchemy.
game.db: The SQLite database file for storing player information and game history.

## Author
The author of this script is Patience Wangari Muraguri.

[LICENSE](https://github.com/Cairie5/Rock-Paper-Scissors-CLI/blob/main/LICENSE)
