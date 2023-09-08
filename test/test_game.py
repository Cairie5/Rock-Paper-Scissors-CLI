# tests/test_game_logic.py
import unittest
from unittest.mock import patch
from game_logic import play_round, get_computer_choice, update_player_wins, record_game, get_game_history, get_player_wins
from model import Player, Game, Move, engine
from sqlalchemy.orm import sessionmaker

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def tearDown(self):
        self.session.close()

    def test_play_round(self):
        # Test a round where the player wins
        with patch('game_logic.get_computer_choice', return_value='scissors'):
            result = play_round('rock', 'test_player')
        self.assertEqual(result, 'You win!')

        # Test a round where the player loses
        with patch('game_logic.get_computer_choice', return_value='paper'):
            result = play_round('rock', 'test_player')
        self.assertEqual(result, 'Computer wins!')

        # Test a round that ends in a tie
        with patch('game_logic.get_computer_choice', return_value='rock'):
            result = play_round('rock', 'test_player')
        self.assertEqual(result, "It's a tie!")

    def test_update_player_wins(self):
        # Test updating player wins
        player = Player(name='test_player')
        self.session.add(player)
        self.session.commit()

        update_player_wins('test_player')
        self.assertEqual(player.wins, 1)

    def test_record_game(self):
        # Test recording a game
        player = Player(name='test_player')
        self.session.add(player)
        self.session.commit()

        record_game('test_player', 'rock', 'scissors', 'You win!')
        game = self.session.query(Game).filter_by(player=player).first()
        self.assertIsNotNone(game)

    def test_get_game_history(self):
        # Test getting game history for a player
        player = Player(name='test_player')
        self.session.add(player)
        self.session.commit()

        record_game('test_player', 'rock', 'scissors', 'You win!')
        record_game('test_player', 'paper', 'rock', 'You win!')

        games = get_game_history('test_player')
        self.assertEqual(len(games), 2)

    def test_get_player_wins(self):
        # Test getting player wins
        player = Player(name='test_player', wins=3)
        self.session.add(player)
        self.session.commit()

        wins = get_player_wins('test_player')
        self.assertEqual(wins, 3)

if __name__ == '__main__':
    unittest.main()
