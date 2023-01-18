from utils import no_one_is_dead, attack, drink_potion, display_scores, who_won, store_scores, menu
import random as rd 

op_lives = 50
m_lives = 50
potion = 3
player = 'opponent'

display_scores(op_lives, m_lives)
while no_one_is_dead(m_lives, op_lives):
        print("It's my turn.")
        choice = menu(potion)
        if choice=='1':
            op_lives, my_lives = attack('you', op_lives, m_lives)
            if op_lives < 0:
                op_lives = 0
            display_scores(op_lives, m_lives)
            if not no_one_is_dead(m_lives, op_lives):
                break 
            else :
                print("It's opponent's turn.")
                op_lives , m_lives = attack('opponent', op_lives, m_lives)
                display_scores(op_lives, m_lives)
        elif choice =='2':
            m_lives, potion = drink_potion(m_lives, potion)
            display_scores(op_lives, m_lives)
            print("It's opponent's turn.")
            op_lives, m_lives= attack('opponent',op_lives, m_lives)
            display_scores(op_lives, m_lives)
            print("You chose to drink a potion in the previous turn, you must skip your turn")
            opponent_lives, m_lives = attack('opponent',op_lives, m_lives)
            display_scores(op_lives, m_lives)
who_won(m_lives, op_lives)
store_scores() 
    
