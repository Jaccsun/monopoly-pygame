from modes import singleplayer
import time

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


if mode == SINGLEPLAYER:
    singleplayer.main()



