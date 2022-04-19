from board.board import Board
from player import Player
from player import draw_all_players
from player_interface import *
from cpu import CPU
from roll import Roll
import os
import pygame

# Color constants.
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
GREY = (200, 200, 200)

# Creates the board and player objects.
board = Board()
player, player_2, player_3, player_4 = Player(RED), CPU(GREEN), CPU(BLUE), CPU(PURPLE)
players = [player, player_2, player_3, player_4]

# Mode constants.
SINGLEPLAYER = "0"
MULTIPLAYER = "1"

# Window constants.
WIDTH, HEIGHT = 900, 900
FPS = 60

# Creates the window and sets the name of the window.
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monopoly")

# Pygame clock.
clock = pygame.time.Clock()

# Board image.

BOARD_IMAGE = pygame.image.load(os.path.join('Assets', 'board.jpg'))

pygame.font.init()


font_test = pygame.font.SysFont('arial', 50)
welcome_text = font_test.render("Welcome to monopoly!", True, BLACK)

button = pygame.Rect(20, 60, 70, 40) 

def draw_window():
    WIN.fill((180, 180, 180))
    WIN.blit(BOARD_IMAGE, (150, 150))
    draw_all_players(players, WIN)
    pygame.draw.rect(WIN, BLACK, button)
    WIN.blit(welcome_text, (0, 0))
    pygame.display.update()

run = True

while run:
    clock.tick(FPS)
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40:
                print("click")
        draw_window()

pygame.quit()

in_selection = True
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

    # Creates the player objects that will be used throughout the game.
    

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






        






