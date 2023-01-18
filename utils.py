import random as rd


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
    print(f'Opponent has {opponent_lives} lives. I have {my_lives} lives.')

def who_won(my_lives:int, opponent_lives:int,my_victory:int, opponent_victory:int):
    """The function checks which player has more lives and prints the result of the game.
    If the player has more lives, it will print "I won !!!!!".
    Otherwise, it will print "Opponent won..."

    Args:
        opponent_lives (int): representing the number of lives the opponent has
        my_lives (int): representing the number of lives the player has
    """
    if my_lives > opponent_lives:
        print('I won !!!!!')
        my_victory += 1
    else : 
        print('Opponent won...')
        opponent_victory += 1

    
            
def store_scores():
    pass

def menu(potion):
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
    
def principal_menu(game):
    choice = input('Welcome. What do you want to do ? To play press 1, to end the game press 2.')
    if choice == "1":
        return choice 
    elif choice == "2" :
        return choice 
    else : 
        print('Please, press 1 or 2.')
        choice = input('Welcome. What do you want to do ? To play press 1, to end the game press 2.')
        
         