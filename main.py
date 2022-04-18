from board.board import Board
from player import Player
from player_interface import *
from cpu import CPU
from roll import Roll

# Monopoly V0.0
print("Welcome to monopoly!")

in_selection = True

SINGLEPLAYER = "0"
MULTIPLAYER = "1"

while in_selection:
    mode = input("Select a mode: 0 - Singleplayer Mode, 1 - Multiplayer mode: ")
    if mode == SINGLEPLAYER:

        input("-Thank you for selecting Singleplayer mode-")
        in_selection = False
    elif mode == MULTIPLAYER:
        input("-Thank you for selecting Multiplayer mode-")
        in_selection = False
    else:
        print("Your answer is not valid, please enter another.")

board = Board()

if mode == SINGLEPLAYER:

    # Creates the player objects that will be used throughout the game.
    player, player_2, player_3, player_4 = Player(), CPU(), CPU(), CPU()

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
            print ("------------------------------------------")
            if current_player.id == 1:
                enter_selection(current_player, board)
            else: 
                print("AI turn.")
                current_player.play(board)


        






