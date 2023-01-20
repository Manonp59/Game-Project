import unittest
import unittest.mock as mock
from unittest.mock import patch
import random
from utils import drink_potion, choose_pokemon

class TestWithUnittest(unittest.TestCase):
        def test_drink_potion(self):
                random.seed(10)
                self.assertEqual(drink_potion('you',12, 2, 22, 3),(29, 1, 22, 3))
                random.seed(19)
                self.assertEqual(drink_potion('Manon',46, 0, 5, 1),(46, 0, 22, 0))
                self.assertEqual(drink_potion('Myriam',30, 2, 19, 1),(30, 2, 50, 0))
                
class TestChoosePokemon(unittest.TestCase):
    def test_valid_input(self):
        with patch('builtins.input', side_effect=["1", "y"]):
            player, enemy = choose_pokemon()
            self.assertIn(player, ["Bulbizarre", "Salamèche", "Carapuce"])
            self.assertIn(enemy, ["Bulbizarre", "Salamèche", "Carapuce"])

    def test_invalid_input(self):
        with patch('builtins.input', side_effect=["a", "1", "y"]):
            player, enemy = choose_pokemon()
            self.assertIn(player, ["Bulbizarre", "Salamèche", "Carapuce"])
            self.assertIn(enemy, ["Bulbizarre", "Salamèche", "Carapuce"])

    def test_invalid_confirm(self):
        with patch('builtins.input', side_effect=["1", "n", "1", "y"]):
            player, enemy = choose_pokemon()
            self.assertIn(player, ["Bulbizarre", "Salamèche", "Carapuce"])
            self.assertIn(enemy, ["Bulbizarre", "Salamèche", "Carapuce"])