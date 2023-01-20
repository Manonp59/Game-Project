import unittest
from unittest.mock import patch
import unittest.mock as mock
import random as rd
from utils import attack, menu, create_file, principal_menu



class TestWithUnittest(unittest.TestCase):
    
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
    
    
    # Define possible values of inputs and verify the return
    @patch('builtins.input', side_effect = ['1','2'])
    def test_menu(self, mock_input):
        calling_1 = mock_input()
        calling_2 = mock_input()
        self.assertTrue(calling_1 == '1' and calling_2 == '2')
        self.assertEqual(menu('you',0,0,12,),'1')
     
     
    # Verify the file's creation   
    def test_create_file(self):
        create_file()
        with open('scores.csv','r') as fichier:
            self.assertIn('Victory' and 'Game n°' and 'You' and 'Enemy', fichier.read())
    
    
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