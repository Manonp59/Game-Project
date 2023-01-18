import random as rd
import csv

def no_one_is_dead (my_lives:int,opponent_lives:int) -> bool:
    """Function wich verify that no one is dead.

    Args:
        my_lives (int): lives of the player
        opponent_lives (int): lives of the opponent 

    Returns:
        bool : True if no one is dead, False if someone is dead 
    """
    # Scores comparaison
    if my_lives <= 0 or opponent_lives <= 0:
        return False 
    else :
        return True 


def attack(player:str, opponent_lives: int, my_lives :int) -> int :
    """The function calculate damage depending on whether the player or the opponent is attacking
    If the player is attacking, the function will randomly choose a value between 5 and 10 to subtract from the opponent's lives.
    If the opponent is attacking, the function will randomly choose a value between 5 and 15 to subtract from the player's lives.

    It checks if the lives are less than 0 and sets it to 0 if it is.
    The function returns a tuple containing the updated number of lives of the opponent and the player. 

    Args:
    player (str): representing the attacking player ('you' or 'opponent')
    opponent_lives (int):representing the number of lives the opponent has
    my_lives (int): representing the number of lives the player has

    Returns:
        tuple containing the updated number of lives of the opponent and the player. 
    """
    damage = 0
    if player == 'you' :
        damage = rd.randint(5,10)
        opponent_lives -= damage
        if opponent_lives < 0 :
            opponent_lives = 0
    else :
        damage = rd.randint(5,15)
        my_lives -= damage
        if my_lives < 0 :
            my_lives = 0
    return opponent_lives, my_lives


def drink_potion(my_lives:int, potion:int)-> tuple:
    """The function increases the player's lives by a random amount between 15 and 50, but not exceeding 50.
    It also decrements the number of potions by 1.

    Args:
        my_lives (int): representing the number of lives the player has
        potion (int): representing the number of potions the player has

    Returns:
        tuple: containing the updated number of lives, number of potions.
    """
    my_lives += (rd.randint(15,50))
    if my_lives >50 :
        my_lives = 50
    potion -= 1
    return my_lives, potion


def display_scores(opponent_lives:int, my_lives:int):
    """Displays the number of lives of both the opponent and the player.
    
    Args:
        opponent_lives (int): representing the number of lives the opponent has
        my_lives (int): representing the number of lives the player has
    """
    return f'Opponent has {opponent_lives} lives. I have {my_lives} lives.'


def who_won(my_lives:int, opponent_lives:int,your_victory:int, opponent_victory:int):
    """The function checks which player has more lives and prints the result of the game.
    If the player has more lives, it will print "I won !!!!!".
    Otherwise, it will print "Opponent won...". It also counts the number of victories for each player.

    Args:
        opponent_lives (int): representing the number of lives the opponent has
        my_lives (int): representing the number of lives the player has
        
    Returns: 
        tuple:the number of victories of each player
    """
    if my_lives > opponent_lives:
        print('I won !!!!!')
        your_victory += 1
    else : 
        print('Opponent won...')
        opponent_victory += 1
    return your_victory, opponent_victory


def create_file():
    """This function creates a CSV file named 'scores.csv' if it does not exist, and writes a header row with the following titles: "Game n°", "You", "Opponent", "Victory". This function is used to initialize the file to store the scores of the played games.
    """
    with open('scores.csv', 'a', newline='') as scores:
        write=csv.writer(scores)
        #creation of the columns's head
        write.writerow(["","Game n°", "You", "Opponent", "Victory"])
        

def store_scores(game:int, m_lives:int, opponent_lives:int):
    """This function stores the scores of a game in a CSV file named 'scores.csv. It uses the CSV library to write the game name, player lives, opponent lives, and the winner of the game (either 'You' or 'Opponent') to a new row in the CSV file.

    Args:
        game (int): the name of the game
        m_lives (int): the number of lives the player has
        opponent_lives (int): the number of lives the opponent has. 
    """
    with open('scores.csv', 'a', newline='') as scores:
        write=csv.writer(scores) 
        victory = ""
        # Check to define the round's winner
        if m_lives>opponent_lives :
            victory ="You"
        else : 
            victory ="Opponent"
        write.writerow(["",game, m_lives, opponent_lives,victory])  
  
        
def total_score(your_victory:int, opponent_victory:int):
    """
    Store the total scores of the games played in a CSV file. 
    The file is created if it does not exist.

    Args:
    your_victory (int): the number of your victory
    opponent_victory (int): the number of opponent victory

    """
    with open('scores.csv', 'a', newline='') as scores:
        write=csv.writer(scores) 
        winner = ""
        #Check to define the game's winner
        if your_victory>opponent_victory :
            winner ="You"
        elif your_victory<opponent_victory : 
            winner ="Opponent"
        else:
            winner = "Equality"
            write.writerow([])
        write.writerow(["","Your victory", "Opponent victory", "Winner"])
        write.writerow(["Total",your_victory, opponent_victory, winner])


def menu(potion:int)->str:
    """"This function is a menu for a game where the player can choose to attack or drink a potion. It prompts the player to input their choice (either '1' to attack or '2' to drink a potion). If the player inputs an invalid choice, they will be prompted again. If the player has no potions, they will automatically be forced to attack and the function will return '1'."
    
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
    
    
def principal_menu():
    """   This function displays a main menu for the game and prompts the user to choose between playing (choice 1) or quitting the game (choice 2). If the user enters a valid input (1 or 2), the function returns that input. Otherwise, the user will be prompted to enter a valid input.

    Args:
    game (str): the name of the game

    Returns:
    str: the player's choice (either "1" or "2")
    """
    choice = input('Welcome. What do you want to do ? To play press 1, to end the game press 2.')
    if choice == "1":
        return choice 
    elif choice == "2" :
        return choice 
    else : 
        print('Please, press 1 or 2.')
        choice = input('Welcome. What do you want to do ? To play press 1, to end the game press 2.')
        
         