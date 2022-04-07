from ast import YieldFrom
import imp
from msilib.schema import Property
from threading import currentThread
from tkinter.tix import Y_REGION
from turtle import ycor
from board import Board
from space import Monopoly_Space
from player import Player

board = Board()
def main():
    # Creates the player objects that will be used throughout the game.
    player, player_2, player_3, player_4 = Player(), Player(), Player(), Player()

    # Ask for dice input to determine playing order.
    input("-Roll Dice to Determine order-")
    input("Press Enter to roll:")

    # Player rolls the dice.
    roll = player.roll()

    # Tells the player what number they rolled.
    input("You rolled " + str(roll.value))
    # Rolls the dice for the other players and gives the values.
    roll_2, roll_3, roll_4, = player_2.roll(), player_3.roll(), player_4.roll()
    input("Player 2 rolled: " + str(roll_2.value) + " | Player 3 rolled: " +
          str(roll_3.value) + " | Player 4 rolled: " + str(roll_4.value))

    # Determines the order of the game.
    order = [roll, roll_2, roll_3, roll_4]
    order.sort(key=lambda x: x.value, reverse=True)
    order = [order[0].player, order[1].player,
             order[2].player, order[3].player]
    del roll, roll_2, roll_3, roll_4
    # Tells the player the order of the game.
    if order[0].id == 1:
        input("You will play first.")
    else:
        input("Player " + str(order[0].id) + " will play first.")

    # Turn cycle boolean to track each player.
    turn_cycle = True

    while turn_cycle:
        for current_player in order:
            if current_player.id == 1:

                enter_selection(current_player)

            else: 
                input("CPU turn")


def enter_selection(current_player):
    in_selection = True

    # Entering selection screen, player can roll,
    # manage their properties, trade, or forfeit thegame.

    while (in_selection):

        input("-It's your turn-")

        print("Current position: " + str(current_player.position), 
        "Money: " + str(current_player.money) + "$")

        select = input("0 - Roll | 1 - Property manager | 2 - Trade | 3 - Forfeit ")

        # Rolls the die upon player selection.
        if select == "0":
            select_roll(current_player)
            in_selection = False
        elif select == "1":
            select_property_manager(current_player)
        elif select == "2":
            select_trade()
        elif select == "3":
            print("Thanks for playing.")
            in_selection = False
            turn_cycle = False
        else:
            print("Invalid input")
        
        print("Your current cash: " + str(current_player.money) + "$")
        

    
def select_roll(current_player):
    player_roll = current_player.roll() 

    # Tells the player what they rolled.
    input("You rolled a " + str(player_roll.value)) 
    current_player.move(player_roll)

    # Uses the info from the roll and the new player position to determine the space they landed on.
    landed_on_space = board.space[current_player.position]
    print("You landed on " + str(landed_on_space.space_name))

    # Property space type.
    if(landed_on_space.space_type == "Property"):
        select_roll_prompt_property(landed_on_space, current_player)
        

# Property prompt system.
def select_roll_prompt_property(landed_on_space, current_player):
    if (landed_on_space.owner == None):
        in_prompt = True
        while(in_prompt):
            property_prompt = input(
                "Would you like to buy this property? (y/n): ")
            if (property_prompt == "y"):
                if(current_player.money - landed_on_space.printed_price < 0):
                    print("You don't have enough money to purchase this property.")
                    in_prompt = False
                else:
                    print("You have purchased " +
                          str(landed_on_space.space_name) + "!")
                          
                    current_player.money -= landed_on_space.printed_price
                    current_player.properties.append(landed_on_space)
                    landed_on_space.owner = current_player
                    in_prompt = False
            elif (property_prompt == "n"):
                print("You decided not to buy " + str(landed_on_space.space_name))
                in_prompt = False
            else:
                print("Input not understood")
    elif (landed_on_space.owner == current_player):
        print("You own this property")
    else:   
        print("This property is owned by " + landed_on_space.owner)
        print("Amount owned: " + landed_on_space.get_current_price())
        in_selection = True
        while in_selection:
            input("0 - Pay | 1 - Mortage")

# Visual property manager to view properties and build.      
def select_property_manager(current_player):
    if len(current_player.properties) == 0:
        print("You don't have any properties.")
    else: 
        print("Your current properties")
        for owned_property in current_player.properties:
            print(str(owned_property) + owned_property.space_name)
        selection = True
        while selection:
            select = input("0 - Exit | (1+ Build on Property)")
            if (select == "0"):
                return None
            else: 
                print("Invalid")
        

def select_trade():
    print("test")


if __name__ == "__main__":
    main()
