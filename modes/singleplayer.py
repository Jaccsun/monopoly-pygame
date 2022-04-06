from ast import YieldFrom
import imp
from msilib.schema import Property
from tkinter.tix import Y_REGION
from turtle import ycor
from board import Board
from space import Monopoly_Space
from player import Player
import time
def main():
    #Creates the Board object that will be played on.
    board = Board()
    #Creates the player objects that will be used throughout the game.
    player, player_2, player_3, player_4 = Player(), Player(), Player(), Player()

    time.sleep(1)
    #Ask for dice input to determine playing order.
    print("-Roll Dice to Determine order-")
    input("Press Enter to roll:")

    #Player rolls the dice.
    roll = player.roll()

    time.sleep(1)
    #Tells the player what number they rolled.
    print("You rolled " + str(roll.value))
    time.sleep(1)
    #Rolls the dice for the other players and gives the values.
    roll_2, roll_3, roll_4, = player_2.roll(), player_3.roll(), player_4.roll()
    print("Player 2 rolled: " + str(roll_2.value) + " | Player 3 rolled: " + str(roll_3.value) + " | Player 4 rolled: " + str(roll_4.value))
    
    #Determines the order of the game.
    order = [roll, roll_2, roll_3, roll_4]
    order.sort(key = lambda x: x.value, reverse=True)
    order = [order[0].player, order[1].player, order[2].player, order[3].player]
    del roll, roll_2, roll_3, roll_4
    time.sleep(1)
    #Tells the player the order of the game.
    if order[0].id == 1:
        print("You will play first.")
    else: print("Player " + str(order[0].id) + " will play first.")

    turn_cycle = True
    while turn_cycle:
        for p in order:
            time.sleep(1)
            if p.id == 1:
                print("-It's your turn-")
                time.sleep(1)
                print("Current position: " + str(p.position), "Money: " + str(p.money) + "$")
                in_selection = True
                while (in_selection):
                    select = input("0 - Roll | 1 - Property manager | 2 - Trade | 3 - Forfeit ")
                    if select == "0":
                        player_roll = p.roll()
                        time.sleep(1)
                        print("You rolled a " + str(player_roll.value))
                        time.sleep(1)
                        print("Moving...")
                        p.move(player_roll)
                        time.sleep(1)
                        space = board.space[p.position]
                        print("You landed on " + str(space.S_name))
                        if(space.S_type == 'P'):
                            if (space.owner == None):
                                in_prompt = True
                                while(in_prompt):
                                    property_prompt = input("Would you like to buy this property? (y/n): ")
                                    if (property_prompt == "y"):
                                        if(p.money - space.printed_price < 0):
                                            print("You don't have enough money to purchase this property.")
                                        else:
                                            print("You have purchased " + str(board.space[p.position].S_name) + "!")
                                            p.money -= board.space[p.position].printed_price
                                            p.properties.append(board.space[p.position])
                                            board.space[p.position].owner = p
                                            in_prompt = False
                                    elif (property_prompt == "n"):
                                        print("You decided not to buy " + str(board.space[p.position].S_name))
                                        in_prompt = False
                                    else: 
                                        print ("Input not understood")

                        print("Your current cash: " + str(p.money) + "$")
                        
                        in_selection = False
                    elif select == "1":
                        print("Current Properties Owned:")
                    elif select == "2":
                        print("Who do you want to trade with?: 0 - Player 2 | 1 - Player 3 | 2 - Player 4")
                    elif select == "3":
                        print("Thanks for playing.")
                        in_selection = False
                        turn_cycle = False
                    else:
                        print("Invalid input")
            else:
                print("CPU turn")

        
    

if __name__ == "__main__":
    main()