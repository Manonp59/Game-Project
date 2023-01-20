from utils import choose_pokemon, no_one_is_dead, attack, drink_potion, display_scores, who_won, store_scores, menu, principal_menu, create_file, total_score, display_welcome
import random as rd 

# Welcome message and song
display_welcome()
    
# Variables 
game = 0
enemy_victory = 0
player_victory = 0

# Scores file creation
create_file()
choice = principal_menu()
# If the player choose to play a game
while choice == "1":
    # Reset of the scores, the number of potion and the number of special hits
    enemy_lives = 50
    player_lives = 50
    player_potion = 3
    enemy_potion = 3
    player_special_hits = 2
    enemy_special_hits = 2
    player, enemy = choose_pokemon()
    # Update of the game number
    game += 1
    # Display of the scores
    display_scores(enemy_lives, player_lives, player, enemy)
    # Check if no one died
    while no_one_is_dead(player_lives, enemy_lives):
            # Display who plays
            print("It's your turn.")
            # Asks for choices : attack or drink potion
            choice = menu('you', player_potion, enemy_potion, enemy_lives)
            # If player choose attack
            if choice =='1':
                # Update of the scores with attack
                player_lives, enemy_lives, player_special_hits, enemy_special_hits = attack('you', player, enemy, player_special_hits, enemy_special_hits, player_lives, enemy_lives)
                display_scores(player_lives, enemy_lives, player, enemy)
                if not no_one_is_dead(player_lives, enemy_lives):
                    break    
            # If player choose potion
            elif choice == '2':
                # Update of the scores with potion
                player_lives, player_potion, enemy_lives, enemy_potion = drink_potion('you', player_lives, player_potion, enemy_lives, enemy_potion)
                display_scores(player_lives, enemy_lives, player, enemy)
                # Displays who plays
            print("It's enemy's turn.")
            choice = menu('enemy', player_potion, enemy_potion, enemy_lives)
            if choice == '1':
            # Update of the score with attack
                player_lives, enemy_lives, player_special_hits, enemy_special_hits = attack('enemy', player, enemy, player_special_hits, enemy_special_hits, player_lives, enemy_lives)
                display_scores(player_lives, enemy_lives, player, enemy)
                if not no_one_is_dead(player_lives, enemy_lives):
                    break  
            elif choice == '2' :
                # Update of scores with attack
                player_lives, player_potion, enemy_lives, enemy_potion = drink_potion('enemy', player_lives, player_potion, enemy_lives, enemy_potion)
                display_scores(player_lives, enemy_lives, player, enemy)
    # Someone is dead, so it displays who won 
    player_victory,enemy_victory = who_won(player_lives, enemy_lives, player_victory, enemy_victory)
    # Storage of the scores in a file
    store_scores(game, player_lives, enemy_lives) 
    # Asks if the player wants to play an other game or end it
    choice = principal_menu()

# Adds the total wins of each player in the scores file and displays the final winner
total_score(player_victory, enemy_victory)
    
