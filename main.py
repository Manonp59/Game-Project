from utils import no_one_is_dead, attack, drink_potion, display_scores, who_won, store_scores, menu
import random as rd 

op_lives = 50
m_lives = 50
potion = 3
player = 'opponent'
drinked_potion = False


while no_one_is_dead(m_lives, op_lives):
    if not drinked_potion:
        print("It's my turn.")
        if menu(potion)=='1':
            attack('me',op_lives, m_lives)
        elif menu(potion)=='2':
            drink_potion(m_lives)
        print(op_lives)
        display_scores(op_lives, m_lives)
        print("It's opponent's turn.")
        attack('opponent', op_lives, m_lives)
        display_scores(op_lives, m_lives)
    else : 
        attack('opponent', op_lives, m_lives)
        drinked_potion = False
who_won()
store_scores() 
    
