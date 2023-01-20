import random as rd
import csv
from termcolor import colored
import pyfiglet
from playsound import playsound

# Variables
game = 0
enemy_victory = 0
player_victory = 0

def no_one_is_dead (player_lives:int,enemy_lives:int) -> bool:
    """Function wich verify that no one is dead.

    Args:
        player_lives (int): lives of the player
        enemy_lives (int): lives of the enemy 

    Returns:
        bool : True if no one is dead, False if someone is dead 
    """
    # Scores comparaison
    if player_lives <= 0 or enemy_lives <= 0:
        return False 
    else :
        return True 


def drink_potion(who_plays:str, player_lives:int, player_potion:int, enemy_lives:int, enemy_potion:int) -> tuple:
    """The function increases the player's lives by a random amount between 15 and 50, but not exceeding 50. \n
    It also decrements the number of potions by 1.

    Args:
        player_lives (int): representing the number of lives the player has
        who_plays(str): representing who's turn is
        player_potion (int) : representing the number of players's potion 
        enemy_potion(int) : representing the number of enemy's potion 
        enemy_lives(int) : representing the number of lives the enemy has
        

    Returns:
        tuple: containing the updated number of lives, number of potions for both players.
    """
    if who_plays == 'you':
        print('You chose to drink a potion. Tchin !')
        player_lives += (rd.randint(15,50))
        if player_lives > 50:
            player_lives = 50
        player_potion -= 1
    else : 
        print('Enemy chose to drink a potion. Tchin !')
        enemy_lives +=(rd.randint(15,50))
        if enemy_lives > 50:
            enemy_lives = 50
        enemy_potion -= 1
    return player_lives, player_potion, enemy_lives, enemy_potion


def display_scores(player_lives:int, enemy_lives:int, player:str, enemy:str) -> None :
    """Displays the pokémon and the number of lives of both the enemy and the player.
    
    Args:
        enemy_lives (int): represents the number of lives the enemy has
        player_lives (int): represents the number of lives the player has
        player (str): name of the pokémon chosen by the player
        enemy (str) : name of the enemy's pokémon
    """
    player_score = f'YOU: {player_lives}HP'           
    enemy_score= f'ENEMY: {enemy_lives}HP'
    # Calling of de draw_ascii function to display the right pokémons
    if player == 'Bulbizarre':
        if enemy == 'Bulbizarre':
            draw_ascii("Pokemons_Ascii/bulbul")
        elif enemy == 'Salamèche':
            draw_ascii("Pokemons_Ascii/bulsal")
        elif enemy == 'Carapuce':
            draw_ascii("Pokemons_Ascii/bulcar")
    if player == 'Salamèche':
        if enemy == 'Bulbizarre':
            draw_ascii("Pokemons_Ascii/salbul")
        elif enemy == 'Salamèche':
            draw_ascii("Pokemons_Ascii/salsal")
        elif enemy == 'Carapuce':
            draw_ascii("Pokemons_Ascii/salcar")
    if player == 'Carapuce':
        if enemy == 'Bulbizarre':
            draw_ascii("Pokemons_Ascii/carbul")
        elif enemy == 'Salamèche':
            draw_ascii("Pokemons_Ascii/carsal")
        elif enemy == 'Carapuce':
            draw_ascii("Pokemons_Ascii/carcar")
    print(colored('\t\t'+player_score, 'black', 'on_blue', ['bold']), end='\t\t\t\t\t')
    print(colored(enemy_score, 'black', 'on_red', ['bold']))


def who_won(player_lives:int, enemy_lives:int,player_victory:int, enemy_victory:int) -> tuple:
    """The function checks which player has more lives and prints who is the winner. \n
    It also counts the number of victories for each player. It plays a sound of victory or defeat.

    Args:
        enemy_lives (int): represents the number of lives the enemy has
        player_lives (int): represents the number of lives the player has
        player_victory (int) : represents the number of victory the player has 
        enemy_victory (int) : represents the numer of victory the enemy has 
        
    Returns: 
        tuple: the number of victories of each player
    """
    if player_lives > enemy_lives:
        print(pyfiglet.figlet_format('You won !'))
        play_sound("Sounds/success.wav")
        player_victory += 1
    else : 
        print(pyfiglet.figlet_format('You loose ...'))
        enemy_victory += 1
        play_sound("Sounds/defeat.wav")
    return player_victory, enemy_victory


def create_file() -> None :
    """This function creates a CSV file named 'scores.csv' if it does not exist, and writes a header row with the following titles: "Game n°", "You", "Enemy", "Victory". \n 
    This function is used to initialize the file to store the scores of the played games.
    """
    # If the file alreay exist from a previous game, it delete its content
    with open('scores.csv', 'w') as file:
            file.truncate()
    with open('scores.csv', 'a', newline='') as scores:
        write=csv.writer(scores)
        # Creation of the column headers of the scores table
        write.writerow(["","Game n°", "You", "Enemy", "Victory"])
        

def store_scores(game:int, player_lives:int, enemy_lives:int) -> None :
    """This function stores the scores of a game in a CSV file named 'scores.csv. \n
    It uses the CSV library to write the game number, player lives, enemy lives, and the winner of the game (either 'You' or 'enemy') to a new row in the CSV file.

    Args:
        game (int): the name of the game
        player_lives (int): the number of lives the player has
        enemy_lives (int): the number of lives the enemy has. 
    """
    with open('scores.csv', 'a', newline='') as scores:
        write=csv.writer(scores) 
        victory = ""
        # Check to define the round's winner
        if player_lives > enemy_lives:
            victory ="You"
        else : 
            victory ="enemy"
        write.writerow(["",game, player_lives, enemy_lives,victory])  
  
        
def total_score(player_victory:int, enemy_victory:int) -> None :
    """
    Store the total scores of the games played in the CSV file. 

    Args:
    player_victory (int): the number of the player's victory
    enemy_victory (int): the number of the enemy's victory

    """
    with open('scores.csv', 'a', newline='') as scores:
        write=csv.writer(scores) 
        winner = ""
        #Check to define the game's winner
        if player_victory > enemy_victory:
            winner ="You"
        elif player_victory < enemy_victory: 
            winner ="Enemy"
        else:
            winner = "Equality"
            # Skip a row
            write.writerow([])
        # Creation of the column headers of the total scores table
        write.writerow(["","Player's victories", "Enemy's victories", "Winner"])
        write.writerow(["Total",player_victory, enemy_victory, winner])


def menu(who_plays:int, player_potion:int, enemy_potion:int, enemy_lives:int) -> str:
    """"This function is a menu for a game where the player can choose to attack or drink a potion. \n 
    It prompts the player to input their choice (either '1' to attack or '2' to drink a potion). \n
    If the player inputs an invalid choice, they will be prompted again. \n
    If the player has no potions, they will automatically be forced to attack and the function will return '1'."
    
    Args:
        player_potion (int): the number of potions the player has.
        who_plays(str) : determine who's turn is
        enemy_potion (int) : the number of potions the enemy has
        enemy_lives (int) : the number of lives the enemy has
        
        
    Returns:
        str: the player's choice
    """
    if who_plays == 'you':
        if player_potion > 0 :
            choice = input(f'You have {player_potion} potion(s). To attack, type 1. To drink potion, type 2.')
            print(choice)
            while choice != "1" and choice != "2" :
                print("Please press 1 or 2.")
                choice = input(f'You have {player_potion} potion(s). To attack, type 1. To drink potion, type 2.')
            if choice == "1" or choice == "2":
                return choice
        else :
            print("You don't have potion anymore. You must attack.")
            return "1"
    else :
        if enemy_potion > 0 and enemy_lives < 35 :
            choice = rd.randint(1,2)
            return str(choice)
        elif enemy_potion > 0 and enemy_lives < 15 :
            return '2'
        elif enemy_potion < 1 :
            print("Enemy doesn't have potion anymore. He must attack.")
            return "1"
        else :
            return '1'
               
    
def principal_menu() -> str:
    """   This function displays a main menu for the game and prompts the user to choose between playing (choice 1), quitting the game (choice 2) or displaying the rules (choice 3). 

    Args:
    game (str): the name of the game

    Returns:
    str: the player's choice (either "1", "2" or "3")
    """
    choice = input('What do you want to do ? To play press 1, to end the game press 2, to display the rules press 3.')
    while choice != "1" and choice != "2"  and choice != "3" :
        print('Please, press 1, 2 or 3.')
        choice = input('What do you want to do ? To play press 1, to end the game press 2, to display the rules press 3.')
    if choice == "1":
        return choice 
    elif choice == "2":
        return choice 
    elif choice == '3':
        display_rules()
        choice = input('What do you want to do ? To play press 1, to end the game press 2.')
        while choice != "1" and choice != "2":
            print('Please, press 1, 2 or 3.')
            choice = input()
        return choice
    else : 
        print('Please, press 1, 2 or 3.')
        choice = input()


def display_rules() -> None:
    """Dsiplay the rules of the game
    """
    print("")
    print("You must choose your Pokémon from Bulbizarre (Grass type), Salamèche (Fire type), and Carapuce (Water type).")
    print("The opponent's Pokémon will be assigned at random. \n Carapuce has an advantage over Salamèche. \n Salamèche has an advantage over Blubizarre.\n Bulbizarre has an advantage over Carapuce.")
    print("")
    print("You will start the game with 50 HP each. Each turn, you will have the choice to attack the opponent or drink a potion. \n Then it will be the opponent's turn to make the same choice. The game ends when one of you has 0 HP.")
    print("")
    print("Attacks:")
    print("\t - classic attacks unlimited, they inflict between 5 and 15 damage points to the opponent")
    print("\t - 2 special attacks that inflict maximum damage if your Pokémon has an advantage over the opponent's Pokémon, \n causing them to lose between 15 and 25 HP, and behave like a classic attack otherwise.")
    print("")
    print("Potions:")
    print("\t - you have 3 potions that can recover between 15 and 50 HP")
    print("")
    print("Good luck! Get ready!") 
    print("")
 
           
def display_welcome() -> None:
    """Displays an ASCII banner with the message "WELCOME TO POKEMON FIGHT" using the pyfiglet library. It also plays the welcome song using the playsound library.
    """
    ascii_banner = pyfiglet.figlet_format("     WELCOME TO \n POKEMON FIGHT")
    print(ascii_banner)  
    play_sound('Sounds/welcome.mp3')    
 

def play_sound(music:str) -> None:
    """Play the sound from a wav file.
    
    Arg:
    music (str): The name of the file to play.
    """
    playsound(music)
    

def attack(who_plays:str, player:str, enemy:str, player_special_hits:int, enemy_special_hits:int, player_lives:int, enemy_lives:int) -> None:
    """This function simulates an attack on the player or enemy depending on who's turn it is.
       The attack is based on the type of the player and enemy pokemon and the number of special hits available.
       The player can choose if he uses a special hit. 

    Args:
        who_plays (str) : 'you' if it's the player's turn, 'enemy' if it's the enemy's turn
        player (str) : the type of player's pokemon ('Bulbizarre', 'Carapuce', 'Salamèche')
        enemy (str) : the type of enemy's pokemon ('Bulbizarre', 'Carapuce', 'Salamèche')
        player_special_hits (int) : the number of remaining special hits for the player
        enemy_special_hits (int) : the number of remaining special hits for the enemy
        player_lives (int) : the number of lives remaining for the player's pokemon
        enemy_lives (int) : the number of lives remaining for the enemy's pokemon

    Returns:
        tuple of 4 integers : 
        - player_lives: the remaining number of lives for the player's pokemon
        - enemy_lives: the remaining number of lives for the enemy's pokemon
        - player_special_hits: the remaining number of special hits for the player
        - enemy_special_hits: the remaining number of special hits for the enemy
    """
    # Who's turn is
    if who_plays == 'you':
        # Verify if special hits are available
        if player_special_hits > 0 :
            # Normal hit
            if player == 'Bulbizarre' and (enemy == 'Bulbizarre' or enemy == 'Salamèche'):
                damage = rd.randint(5,15)
                enemy_lives -= damage
                print('You hit enemy with a normal hit.')
            # Special hit
            if player == 'Bulbizarre' and enemy == 'Carapuce' :
                choice = input(f'You can use special hit against Carapuce ! You have {player_special_hits} special hits. Press 1 to use it, press 2 for a normal hit.')
                while choice != "1" and choice != "2" :
                    print("Please press 1 or 2.")
                    choice = input(f'You can use special hit against Carapuce ! You have {player_special_hits} special hits. Press 1 to use it, press 2 for a normal hit.')
                if choice == "1":
                    damage = rd.randint(15,25)
                    enemy_lives -= damage
                    player_special_hits -= 1
                    print('Special hit ! You strangle the enemy with a vine !')
                elif choice == "2":
                    damage = rd.randint(5,15)
                    enemy_lives -= damage
                    print('You hit enemy with a normal hit.')
            # Normal hit
            if player == 'Carapuce' and (enemy == 'Carapuce' or enemy == 'Bulbizarre'):
                damage = rd.randint(5,15)
                enemy_lives -= damage
                print('You hit enemy with a normal hit.')
            # Special hit or not
            if player == 'Carapuce' and enemy == 'Salamèche':
                choice = input(f'You can use special hit against Salamèche ! You have {player_special_hits} special hits. Press 1 to use it, press 2 for a normal hit.')
                while choice != "1"  and choice != "2" :
                    print("Please press 1 or 2.")
                    choice = input(f'You can use special hit against Carapuce ! You have {player_special_hits} special hits. Press 1 to use it, press 2 for a normal hit.')
                if choice == "1":
                    damage = rd.randint(15,25)
                    enemy_lives -= damage
                    player_special_hits -= 1
                    print('Special hit ! You launch a powerful jet of water on your enemy !')
                elif choice == "2":
                    damage = rd.randint(5,15)
                    enemy_lives -= damage
                    print('You hit enemy with a normal hit.')
            # Normal hit
            if player == 'Salamèche' and (enemy == 'Salamèche' or enemy == 'Carapuce'):
                damage = rd.randint(5,15)
                enemy_lives -= damage
                print('You hit enemy with a normal hit.')
            # Special hit
            if player == 'Salamèche' and enemy == 'Bulbizarre' :
                choice = input(f'You can use special hit against Bulbizarrere ! You have {player_special_hits} special hits. Press 1 to use it, press 2 for a normal hit.')
                while choice != "1" and choice != "2" :
                    print("Please press 1 or 2.")
                    choice = input(f'You can use special hit against Carapuce ! You have {player_special_hits} special hits. Press 1 to use it, press 2 for a normal hit.')
                if choice == "1":
                    damage = rd.randint(15,25)
                    enemy_lives -= damage
                    player_special_hits -= 1
                    print('Special hit ! You throw a ball of fire on your enemy !')
                elif choice == "2":
                    damage = rd.randint(5,15)
                    enemy_lives -= damage
                    print('You hit enemy with a normal hit.')
        # Special hits aren't available, so normal hit
        else : 
            print("You don't have special hit anymore. You hit enemy with normal hit.")
            damage = rd.randint(5,15)
            enemy_lives -= damage
        # Avoid negative scores
        if enemy_lives < 0:
            enemy_lives = 0
    # Who's turn is 
    if who_plays == 'enemy':
        # Verify if special hits are available
        if enemy_special_hits > 0 :
            # Normal hit
            if enemy == 'Bulbizarre' and (player == 'Bulbizarre' or player == 'Salamèche'):
                damage = rd.randint(5,15)
                player_lives -= damage
                print('Enemy hits you with a normal hit.')
            # Special hit
            if enemy == 'Bulbizarre' and player == 'Carapuce' :
                choice = rd.randint(1,2)
                if choice == 1 :
                    damage = rd.randint(15,25)
                    player_lives -= damage
                    enemy_special_hits -= 1
                    print('Special hit ! Enenmy strangle you with a vine !')
                elif choice == 2 :
                    damage = rd.randint(5,15)
                    player_lives -= damage
                    print('Enemy hits you with a normal hit.')
                else : 
                    print('Please, press 1 or 2.')
                    choice = input(f'You can use special hit against Carapuce ! You have {player_special_hits} special hits. Press 1 to use it, press 2 for a normal hit.')
            # Normal hit
            if enemy == 'Carapuce' and (player == 'Carapuce' or player == 'Bulbizarre'):
                damage = rd.randint(5,15)
                player_lives -= damage
                print('Enemy hits you with a normal hit.')
            # Special hit
            if enemy == 'Carapuce' and player == 'Salamèche' :
                choice = rd.randint(1,2)
                if choice == 1:
                    damage = rd.randint(15,25)
                    player_lives -= damage
                    enemy_special_hits -= 1
                    print('Special hit ! Enemy launch a powerful jet of water on you !')
                elif choice == 2:
                    damage = rd.randint(5,15)
                    player_lives -= damage
                    print('Enemy hits you with a normal hit.')
                else : 
                    print('Please, press 1 or 2.')
                    choice = input(f'You can use special hit against Carapuce ! You have {player_special_hits} special hits. Press 1 to use it, press 2 for a normal hit.')
            # Normal hit
            if enemy == 'Salamèche' and (player == 'Salamèche' or player == 'Carapuce'):
                damage = rd.randint(5,15)
                player_lives -= damage
                print('Enemy hits you with a normal hit.')
            # Special hit
            if enemy == 'Salamèche' and player == 'Bulbizarre' :
                choice = rd.randint(1,2)
                if choice == 1:
                    damage = rd.randint(15,25)
                    player_lives -= damage
                    enemy_special_hits -= 1
                    print('Special hit ! Enemy throw a ball of fire on you !')
                elif choice == 2:
                    damage = rd.randint(5,15)
                    player_lives -= damage
                    print('Enemy hits you with a normal hit.')
                else : 
                    print('Please, press 1 or 2.')
                    choice = input(f'You can use special hit against Carapuce ! You have {player_special_hits} special hits. Press 1 to use it, press 2 for a normal hit.')
        # Special hits aren't available anymore
        else : 
            damage = rd.randint(5,15)
            player_lives -= damage
            print('Enemy hits you with a normal hit.')
        # Avoid negative scores
        if player_lives < 0:
            player_lives = 0
    return player_lives, enemy_lives, player_special_hits, enemy_special_hits


def choose_pokemon()-> tuple:
    """Allows the user to select a pokemon from a predefined list of three options, Bulbizarre, Salamèche, and Carapuce.
    \n The function repeatedly prompts the user to make a selection until a valid choice is made and confirmed by the user.
   
    Returns:
        tuple: the user's selected pokemon and a randomly selected Pokemon
    """    
    pokemon_list = ["Bulbizarre", "Salamèche", "Carapuce"]
    while True:
        print("It's time to choose your pokemon !")
        for i, pokemon in enumerate(pokemon_list):
            print(f"{i+1}. {pokemon}")    
        choice = input()
        # Verify that choice is a number between 1 et 3
        if choice.isnumeric() and int(choice) in range(1, 4):
            print("Do you confirm your choice? [y/n])")
            confirm = input()
            if confirm == "y":
                player = pokemon_list[int(choice)-1]
                break
            elif confirm == "n":
                continue
            elif confirm not in ["y","n"]:
                print("Invalid input, please choose again")
                continue
        if choice not in ["1","2","3"]:
                print("Invalid input, please choose again")
    # The enemy's pokemon is randomly chosen
    enemy = rd.choice(pokemon_list) 
    print("You chose:", player)
    print(f"The enemy chose {enemy}")
    return player, enemy


def draw_ascii(file_name:str) -> None :
    """Opens the file with the given name and reads the contents of the file.
    The contents of the file are then printed to the console. The file is then closed. 
    The function expects the file to be a plain text file with ascii art representation.

    Args:
        file_name (str): String representing the name of the file with ascii art representation
    """
    file = open(file_name + ".txt","r")
    image = file.read()
    print(image)
    file.close()


    