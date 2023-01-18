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
        choice = menu(potion)
        if choice=='1':
            op_lives = attack('you')
            display_scores(op_lives, m_lives)
            print("It's opponent's turn.")
            m_lives -= attack('opponent')
            display_scores(op_lives, m_lives)
        elif choice =='2':
            m_lives, potion, drinked_potion = drink_potion(m_lives, potion)
            display_scores(op_lives, m_lives)
            print("It's opponent's turn.")
            m_lives -= attack('opponent',)
            display_scores(op_lives, m_lives)
            print("You chose to drink a potion in the previous turn, you must skip your turn")
            m_lives -= attack('opponent',)
            display_scores(op_lives, m_lives)
    else : 
        drinked_potion = False
who_won(m_lives, op_lives)
store_scores() 
    
