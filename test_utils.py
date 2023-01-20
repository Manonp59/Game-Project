import unittest
from unittest.mock import patch
import unittest.mock as mock
import random
import os
from utils import no_one_is_dead, drink_potion, create_file, menu, store_scores, attack, who_won, total_score, principal_menu, choose_pokemon

class TestWithUnittest(unittest.TestCase):
    
    def test_no_one_is_dead(self):
        self.assertEqual(no_one_is_dead(5,0), False)
        self.assertEqual(no_one_is_dead(0,5), False)
        self.assertEqual(no_one_is_dead(14,25), True)
    
     
    def test_drink_potion(self):
                random.seed(10)
                self.assertEqual(drink_potion('you',12, 2, 22, 3),(29, 1, 22, 3))
                random.seed(19)
                self.assertEqual(drink_potion('Manon',46, 0, 5, 1),(46, 0, 22, 0))
                self.assertEqual(drink_potion('Myriam',30, 2, 19, 1),(30, 2, 50, 0))
        
    
    def test_create_file(self):
        create_file()
        # Check if the file 'scores.csv' exists
        self.assertTrue(os.path.exists('scores.csv'))
        # Check if the file is not empty
        self.assertGreater(os.path.getsize('scores.csv'), 0)
        with open('scores.csv','r') as fichier:
            self.assertIn('Victory' and 'Game n°' and 'You' and 'Enemy', fichier.read())
     
     
    # Define possible values of inputs and verify the return
    @patch('builtins.input', side_effect = ['1','2'])
    def test_menu(self, mock_input):
        calling_1 = mock_input()
        calling_2 = mock_input()
        self.assertTrue(calling_1 == '1' and calling_2 == '2')
        self.assertEqual(menu('you',0,0,12,),'1')
        
        
    def test_store_scores(self):
        store_scores(1,2,3)
        with open('scores.csv','r') as fichier:
            self.assertIn('1' and '2' and '3', fichier.read())


    def test_normal_hit(self):
    # Test a normal hit with player's Bulbizarre and enemy's Bulbizarre or Salamèche
        player_lives, enemy_lives, player_special_hits, enemy_special_hits = attack('you', 'Bulbizarre', 'Bulbizarre', 2, 2, 50, 50)
        self.assertGreaterEqual(enemy_lives, 35)
        self.assertLessEqual(enemy_lives, 45)
        self.assertEqual(player_lives, 50)
        self.assertEqual(player_special_hits, 2)
        self.assertEqual(enemy_special_hits, 2)

    
    @patch('builtins.input', return_value = "1")
    def test_special_hit(self, return_value):
        # Test a special hit with player's Bulbizarre and enemy's Carapuce
        player_lives, enemy_lives, player_special_hits, enemy_special_hits = attack('you', 'Bulbizarre', 'Carapuce', 2, 2, 50, 50)
        self.assertGreaterEqual(enemy_lives, 25)
        self.assertLessEqual(enemy_lives, 35)
        self.assertEqual(player_lives, 50)
        self.assertEqual(player_special_hits, 1)
        self.assertEqual(enemy_special_hits, 2)


    @patch('builtins.input', return_value = "2")
    def test_not_use_special_hit(self, return_value):
        # Test not using a special hit with player's Bulbizarre and enemy's Carapuce
        player_lives, enemy_lives, player_special_hits, enemy_special_hits = attack('you', 'Bulbizarre', 'Carapuce', 2, 2, 50, 50)
        self.assertGreaterEqual(enemy_lives, 35)
        self.assertLessEqual(enemy_lives, 45)
        self.assertEqual(player_lives, 50)
        self.assertEqual(player_special_hits, 2)
        self.assertEqual(enemy_special_hits, 2)
    
    
    def test_who_won(self):
        self.assertEqual(who_won(34,0,3,4),(4,4))
        self.assertEqual(who_won(0,17,3,1),(3,2))
    
    
    def test_total_score(self):
        total_score(3,2)
        path_to_file="scores.csv"
        with open(path_to_file,"r") as fichier:
            self.assertIn("3" and "2",fichier.read())
    
    
    @patch('builtins.input', return_value = '1')
    def test_principal_menu(self, return_value):
        self.assertEqual(principal_menu(),"1")
        
    @patch('builtins.input', return_value = '2')
    def test_principal_menu(self, return_value):
        self.assertEqual(principal_menu(),"2")
        
    @patch('builtins.input', return_value = '3')
    def test_principal_menu(self, return_value):
        self.assertEqual(principal_menu(),"3")
        
    def test_invalid_input(self):
        # Test invalid input
        input_str = ["4", "1"]
        with mock.patch('builtins.input', side_effect=input_str), mock.patch('builtins.print') as mock_print:
            choice = principal_menu()
            self.assertEqual(choice, "1")
            mock_print.assert_called_with("Please, press 1, 2 or 3.")

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