import random as rd
import csv
from termcolor import colored
import pyfiglet
import pygame

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


def attack(player:str, enemy_lives: int, player_lives :int) -> int:
    """The function calculate damage depending on whether the player or the enemy is attacking. \n
    If the player is attacking, the function will randomly choose a value between 5 and 10 to subtract from the enemy's lives. \n
    If the enemy is attacking, the function will randomly choose a value between 5 and 15 to subtract from the player's lives. \n

    Args:
    player (str): representing the attacking player ('you' or 'enemy')
    enemy_lives (int):representing the number of lives the enemy has
    player_lives (int): representing the number of lives the player has

    Returns:
        tuple containing the updated number of lives of the enemy and the player. 
    """
    damage = 0
    if player == 'you':
        damage = rd.randint(5,10)
        enemy_lives -= damage
        # It checks if the lives are less than 0 and sets it to 0 if it is
        if enemy_lives < 0:
            enemy_lives = 0
    else :
        damage = rd.randint(5,15)
        player_lives -= damage
        # It checks if the lives are less than 0 and sets it to 0 if it is
        if player_lives < 0:
            player_lives = 0
    return enemy_lives, player_lives


def drink_potion(player_lives:int, potion:int) -> tuple:
    """The function increases the player's lives by a random amount between 15 and 50, but not exceeding 50. \n
    It also decrements the number of potions by 1.

    Args:
        player_lives (int): representing the number of lives the player has
        potion (int): representing the number of potions the player has

    Returns:
        tuple: containing the updated number of lives, number of potions.
    """
    player_lives += (rd.randint(15,50))
    if player_lives > 50:
        player_lives = 50
    potion -= 1
    return player_lives, potion


def display_scores(enemy_lives:int, player_lives:int):
    """Displays the number of lives of both the enemy and the player.
    
    Args:
        enemy_lives (int): represents the number of lives the enemy has
        player_lives (int): represents the number of lives the player has
    """
    player_score = f'YOU: {player_lives}HP'           
    enemy_score= f'ENEMY: {enemy_lives}HP'
    print(colored(player_score, 'black', 'on_blue', ['bold']), end='\t')
    print(colored(enemy_score, 'black', 'on_red', ['bold']))
    #return f'Enemy has {enemy_lives} lives. I have {player_lives} lives.'


def who_won(player_lives:int, enemy_lives:int,player_victory:int, enemy_victory:int) -> tuple:
    """The function checks which player has more lives and prints who is the winner. \n
    It also counts the number of victories for each player.

    Args:
        enemy_lives (int): represents the number of lives the enemy has
        player_lives (int): represents the number of lives the player has
        
    Returns: 
        tuple: the number of victories of each player
    """
    if player_lives > enemy_lives:
        print('You won !!!!!')
        play_victory_sound()
        player_victory += 1
    else : 
        print('Enemy wons...')
        enemy_victory += 1
        play_defeat_sound()
    return player_victory, enemy_victory


def create_file():
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
        

def store_scores(game:int, player_lives:int, enemy_lives:int):
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
  
        
def total_score(player_victory:int, enemy_victory:int):
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


def menu(potion:int) -> str:
    """"This function is a menu for a game where the player can choose to attack or drink a potion. \n 
    It prompts the player to input their choice (either '1' to attack or '2' to drink a potion). \n
    If the player inputs an invalid choice, they will be prompted again. \n
    If the player has no potions, they will automatically be forced to attack and the function will return '1'."
    
    Args:
        potion (int): the number of potions the player has.
        
    Returns:
        str: the player's choice
    """
    if potion > 0 :
        choice = input('To attack, type 1. To drink potion, type 2.')
        if choice == "1" or choice == "2":
            return choice
        else : 
            print('Please type a correct value.')
            choice = input('To attack, type 1. To drink potion, type 2.')
    else :
        print("You don't have potion anymore. You will attack.")
        return "1"
    
    
def principal_menu() -> str:
    """   This function displays a main menu for the game and prompts the user to choose between playing (choice 1) or quitting the game (choice 2). 
    If the user enters a valid input (1 or 2), the function returns that input. Otherwise, the user will be prompted to enter a valid input.

    Args:
    game (str): the name of the game

    Returns:
    str: the player's choice (either "1" or "2")
    """
    choice = input('What do you want to do ? To play press 1, to end the game press 2, to display the rules press 3.')
    if choice == "1":
        return choice 
    elif choice == "2":
        return choice 
    elif choice == '3':
        print("RULES OF THE GAME")
        choice = input('What do you want to do ? To play press 1, to end the game press 2.')
        return choice
    else : 
        print('Please, press 1 or 2.')
        choice = input('What do you want to do ? To play press 1, to end the game press 2.')
        
def display_welcome():
    ascii_banner = pyfiglet.figlet_format("     WELCOME TO \n POKEMON FIGHT")
    print(ascii_banner)      
    
def play_victory_sound():
    pygame.init()
    pygame.mixer.music.load("sucess.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)    
        pygame.quit

def play_defeat_sound():
    pygame.init()
    pygame.mixer.music.load("defeat.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)    
        pygame.quit
