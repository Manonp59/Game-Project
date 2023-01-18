from utils import no_one_is_dead, attack, drink_potion, display_scores, who_won, store_scores, menu, principal_menu, create_file, total_score, display_welcome
import random as rd 


display_welcome()
    
# Variables 
game = 0
enemy_victory = 0
player_victory = 0

# Scores file creation
create_file()
choice = principal_menu()
while choice == "3":
    print("THE RULES OF THE GAME")
    choice = principal_menu()
# If the player choose to play a game
while choice == "1":
    # Reset of the scores and the number of potion
    enemy_lives = 50
    player_lives = 50
    potion = 3
    # Update of the game number
    game += 1
    # Display of the scores
    display_scores(enemy_lives, player_lives)

    # Check if no one died
    while no_one_is_dead(player_lives, enemy_lives):
            # Display who plays
            print("It's your turn.")
            # Asks for choices : attack or drink potion
            choice = menu(potion)
            # If player choose attack
            if choice =='1':
                # Update of the scores with attack
                enemy_lives, my_lives = attack('you', enemy_lives, player_lives)
                display_scores(enemy_lives, player_lives)
                if not no_one_is_dead(player_lives, enemy_lives):
                    break 
                else :
                    # Displays who plays
                    print("It's enemy's turn.")
                    # Update of the scores with attack
                    enemy_lives , player_lives = attack('enemy', enemy_lives, player_lives)
                    display_scores(enemy_lives, player_lives)
            # If player choose potion
            elif choice == '2':
                # Update of the scores with potion
                player_lives, potion = drink_potion(player_lives, potion)
                display_scores(enemy_lives, player_lives)
                # Displays who plays
                print("It's enemy's turn.")
                # Update of the score with attack
                enemy_lives, player_lives= attack('enemy',enemy_lives, player_lives)
                display_scores(enemy_lives, player_lives)
                # The player skips his turn
                print("You chose to drink a potion in the previous turn, you must skip your turn")
                # Update of scores with attack
                enemy_lives, player_lives = attack('enemy',enemy_lives, player_lives)
                display_scores(enemy_lives, player_lives)
    # Someone is dead, so it displays who won 
    player_victory,enemy_victory = who_won(player_lives, enemy_lives, player_victory,enemy_victory)
    # Storage of the scores in a file
    store_scores(game, player_lives, enemy_lives) 
    # Asks if the player wants to play an other game or end it
    choice = principal_menu()

# Adds the total wins of each player in the scores file and displays the final winner
total_score(player_victory, enemy_victory)
    
