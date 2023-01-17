import random as rd


def no_one_is_dead (my_lives,opponent_lives):
    if my_lives <= 0 or opponent_lives <= 0:
        return False 
    else :
        return True 


def attack(player, opponent_lives, my_lives):
    if player == 'me' :
        print('ok')
        opponent_lives -= (rd.randint(5,10))
        print(opponent_lives)
    else :
        my_lives -= (rd.randint(5,15))

def drink_potion(my_lives):
    my_lives += (rd.randint(15,50))
    if my_lives >50 :
        my_lives = 50
    potion -= 1
    drinked_potion = True

def display_scores(opponent_lives, my_lives):
    print(f'Opponent has {opponent_lives} lives. I have {my_lives} lives.')

def who_won(my_lives, opponent_lives):
    if my_lives > opponent_lives:
        print('I won !!!!!')
    else : 
        print('Opponent won...')
    
            
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
        choice == 1
        return choice 
        
        
    