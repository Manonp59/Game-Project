import unittest
from unittest.mock import patch
import random
from utils import no_one_is_dead, drink_potion, display_scores, create_file, menu, store_scores

class TestWithUnittest(unittest.TestCase):
    
    def test_no_one_is_dead(self):
        self.assertEqual(no_one_is_dead(5,0), False)
        self.assertEqual(no_one_is_dead(0,5), False)
        self.assertEqual(no_one_is_dead(14,25), True)
    
     
    def test_drink_potion(self):
        random.seed(10)
        self.assertEqual(drink_potion(10,3),(27,2))
        self.assertEqual(drink_potion(45,2),(50,1))
    
      
    def test_display_score(self):
        self.assertEqual(display_scores(15,20), f'Opponent has 15 lives. I have 20 lives.') 
        
    
    def test_create_file(self):
        create_file()
        with open('scores.csv','r') as fichier:
            self.assertIn('Victory' and 'Game n°' and 'You' and 'Opponent', fichier.read())
     
     
    # Define possible values of inputs and verify the return
    @patch('builtins.input', side_effect = ['1','2'])
    def test_menu(self, mock_input):
        calling_1 = mock_input()
        calling_2 = mock_input()
        self.assertTrue(calling_1 == '1' and calling_2 == '2')
        self.assertEqual(menu(0),'1')
        
    def test_store_scores(self):
        store_scores(1,2,3)
        with open('scores.csv','r') as fichier:
            self.assertIn('1' and '2' and '3', fichier.read())
