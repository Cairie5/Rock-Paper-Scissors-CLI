

# Base is a base class provided by SQLAlchemy for declarative class definitions.

# The Player class represents the 'players' table and has columns for id (primary key) and name.

# The Game class represents the 'games' table and has a column for id (primary key).

# The Move class represents the 'moves' table and has columns for id, player_id (foreign key referencing a player), game_id (foreign key referencing a game), and choice to store the player's choice in the game.

# Finally, it creates an SQLite database engine named 'game.db' and uses the create_all method to create the corresponding database tables based on the class definitions in the Base.metadata.

# game_logic.py provides the core logic for playing a single round of the Rock, Paper, Scissors game and determining the result of the round.