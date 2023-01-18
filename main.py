from utils import no_one_is_dead, attack, drink_potion, display_scores, who_won, store_scores, menu, principal_menu, create_file, total_score
import random as rd 

# Variables 
game = 0
opponent_victory = 0
your_victory = 0

create_file()
choice = principal_menu(game)
while choice == "1":
    op_lives = 50
    m_lives = 50
    potion = 3
    game += 1
    # Displaying scores
    display_scores(op_lives, m_lives)

    # Verify that no one is dead 
    while no_one_is_dead(m_lives, op_lives):
            # Displays who plays
            print("It's your turn.")
            # Ask for choices : attack or drink potion
            choice = menu(potion)
            # If player choose attack
            if choice=='1':
                # Update scores with attack
                op_lives, my_lives = attack('you', op_lives, m_lives)
                display_scores(op_lives, m_lives)
                if not no_one_is_dead(m_lives, op_lives):
                    break 
                else :
                    # Displays who plays
                    print("It's opponent's turn.")
                    # Update score with attack
                    op_lives , m_lives = attack('opponent', op_lives, m_lives)
                    display_scores(op_lives, m_lives)
            # If player choose potion
            elif choice =='2':
                # Update scores with potion
                m_lives, potion = drink_potion(m_lives, potion)
                display_scores(op_lives, m_lives)
                # Displays who plays
                print("It's opponent's turn.")
                # Update score with attack
                op_lives, m_lives= attack('opponent',op_lives, m_lives)
                display_scores(op_lives, m_lives)
                # Player skips his turn
                print("You chose to drink a potion in the previous turn, you must skip your turn")
                # Update scores with attack
                opponent_lives, m_lives = attack('opponent',op_lives, m_lives)
                display_scores(op_lives, m_lives)
    # Someone is dead, so displays who won 
    your_victory,opponent_victory = who_won(m_lives, op_lives, your_victory,opponent_victory)
    # Store scores in a file
    store_scores(game, m_lives, op_lives) 
    choice = principal_menu(game)

total_score(your_victory, opponent_victory)
    

