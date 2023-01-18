import unittest 
from unittest.mock import patch
import random
from utils import attack, who_won, total_score, principal_menu

class TestAddWithUnittest(unittest.TestCase):

    def test_attack(self):
        random.seed(15)
        self.assertEqual(attack("you",50,50),(44,50))
        random.seed(15)
        self.assertEqual(attack("Marie",50,50),(50,42))
    
    def test_who_won(self):
        self.assertEqual(who_won(34,0,3,4),(4,4))
        self.assertEqual(who_won(0,17,3,1),(3,2))
    
    def test_total_score(self):
        total_score(3,2)
        path_to_file="scores.csv"
        with open(path_to_file,"r") as fichier:
            self.assertIn("3" and "2",fichier.read())
    
    @patch('builtins.input', side_effect = ['1', '2'])
    def test_principal_menu(self, mock_input):
        calling_1= mock_input()
        calling_2= mock_input()
        self.assertTrue(calling_1 == '1' and calling_2 == '2')