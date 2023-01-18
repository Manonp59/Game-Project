import unittest
from utils import store_scores

class TestFunctionWithUnittest(unittest.TestCase):
    
    def test_store_scores(self):
        game = "1"
        player_lives = "0"
        enemy_lives = "12"
        store_scores(game, player_lives, enemy_lives)
        with open('scores.csv', "r") as scores:
            self.assertIn("1" and "0" and "12", scores.read())
