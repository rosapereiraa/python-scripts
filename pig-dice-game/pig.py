'''
Author: <Rosa Pereira>

Description:
This program runs a game of dice called Pig where two players
take turns at rolling the dice. The score begins at 0 for
both players, if a players rolls the dice and gets a 1 that
player gets 0 points for that round. So on until someone hits
50 points whoever gets to 50 first wins the game.
'''
import math
import random

def print_scores(p1_name,p1_score,p2_name,p2_score):
    '''
    This function prints the scores each player hold at the
    given round.
    Parameters:
    p1_name: str, name for player one
    p1_score: int, score for player one
    p2_name: str, name for player two
    p2_score: int, score for player two
    '''
    print("\n--- SCORES\t"+p1_name+":",str(p1_score)+"\t"+p2_name+":",str(p2_score)+" ---")

def check_for_winner(winner_is,winner_score):
    '''
    This function prints the name of the player that wins the game.
    It will happen after one of the two players hits 50 points.
    Parameters:
    winner_is: str, player that wins the game
    winner_score: int, score of player that wins the game
    returns True if the score is 50 or more, otherwise it 
    returns False (game keeps going)
    '''
    if winner_score >=50:
        print("THE WINNER IS:",winner_is+"!!!!!")
        return True
    else:
        return False

def roll_again(p_name):
    '''
    This function asks the players (by turn) if they would like
    to roll again. Only options are "Y", "y", "N", "n", if given
    a different answer a message is displayed.
    Parameters:
    p_name: str, name of player rolling the dice
    returns True if player wants to keep rolling otherwise
    returns False (next player's turn)
    '''
    an_option=""
    while True:
        an_option=input("Roll again, "+p_name+"? (Y/N) ")
        if an_option in ["Y","y","N","n"]:
            break
        print("I don't understand: \""+an_option+"\". Please enter either \"Y\" or \"N\".") 
    if an_option in ["Y","y"]:
        return True
    return False

def play_turn(p_name):
    '''
    This function prints the player's name, keeps track of 
    the points gained after each turn, tells what number was rolled
    and wheter points were earned (more than 1 has to be rolled),
    or not. If no points are earned a message is displayed.
    Parameters:
    p_name: str, name of player holding the current turn
    returns p_points (player's points)
    '''
    print("---------- "+p_name+"'s turn ----------")
    p_points=0
    while True:
        points_earned=random.randint(1,6)
        print("\t<<< "+p_name+" rolls a "+str(points_earned)+" >>>")
        if points_earned==1:
            print("\t!!! PIG! No points earned, sorry "+p_name+" !!!")
            p_points=0
            input("(enter to continue)")
            return p_points
        if points_earned!=1:
            p_points+=points_earned
            print("\tPoints: "+str(p_points))
        if roll_again(p_name):
            continue
        else:
            return p_points

#==========================================================
def main():
    '''
    This program prints the name of the game, asks the players to input
    their names, and calls for the functions created in order to keep
    track of points, scores, turns, and winner.
    '''
    print("\n\nPig Dice")
    p1_name=input(("Enter name for player 1: "))
    p2_name=input(("Enter name for player 2: "))
    print("\tHello",p1_name,"and",p2_name+", welcome to Pig Dice!")
    p1_points=0
    p2_points=0
    print_scores(p1_name,p1_points,p2_name,p2_points)
    
    while True:
        p1_points+=play_turn(p1_name)
        print_scores(p1_name,p1_points,p2_name,p2_points)
        if check_for_winner(p1_name,p1_points)==False:
            p2_points+=play_turn(p2_name)
            print_scores(p1_name,p1_points,p2_name,p2_points)
            if check_for_winner(p2_name,p2_points)==True:
                break
        else:
            break

if __name__ == '__main__':
    main()