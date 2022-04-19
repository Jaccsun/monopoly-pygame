from tkinter import SINGLE
from board.board import Board
from player import Player
from player import draw_all_players
from player_interface import *
from cpu import CPU
from roll import Roll
import os
import pygame

class Game():

    def __init__(self):
        # Color constants.
        self.WHITE, self.BLUE, self.BLACK, self.RED, self.GREEN, self.PURPLE, self.GREY  = ((255, 255, 255), 
        (0, 0, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (255, 0, 255), (200, 200, 200))
        # Window constants.
        WIDTH, HEIGHT = 900, 900
        self.FPS = 60
        # Creates the window and sets the name of the window.
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        # Creates the board and player objects.
        self.board = Board()
        self.players = [Player(self.RED), CPU(self.GREEN), CPU(self.BLUE), CPU(self.PURPLE)]
        pygame.display.set_caption("Monopoly")
        # Create pygame clock.
        self.clock = pygame.time.Clock()
        # Create the fonts that we'll be using.
        pygame.font.init()
        font_test = pygame.font.SysFont('arial', 50)
        self.welcome_text = font_test.render("Welcome to monopoly!", True, self.BLACK)

        # Creates the starter buttons that will be used during the game.
        self.singleplayer_button, self.multiplayer_button  = pygame.Rect(20, 60, 70, 40), pygame.Rect(100, 60, 70, 40)

        # List of all buttons that are currently on canvas. 
        # Initialized with the two mode buttons as they are 
        # visibile on launch.
        self.buttons = [self.singleplayer_button, self.multiplayer_button]

    def handle_button_logic(self, mouse):
        for button in self.buttons:
            is_mouse_over_button = (button.x <= mouse[0] <= button.x + button.width and
            button.y <= mouse[1] <= button.y + button.height)
            if (is_mouse_over_button):
                if button == self.singleplayer_button:
                    print("Initializing singleplayer")
                    self.intialize_singleplayer()
                if button == self.multiplayer_button:
                    print("multiplayer")
                    self.mode = self.MULTIPLAYER

    def draw_window(self):
        self.WIN.fill((180, 180, 180))
        self.WIN.blit(self.board.IMAGE, (150, 150))
        draw_all_players(self.players, self.WIN)
        for button in self.buttons:
            pygame.draw.rect(self.WIN, self.BLACK, button)
        self.WIN.blit(self.welcome_text, (0, 0))
        pygame.display.update()


    def intialize_singleplayer(self):
        
        self.buttons = []

        # Player rolls the dice.
        # roll = Game.Player.roll()

        # Rolls the dice for the other players and gives the values.
        # roll_2, roll_3, roll_4, = Game.Player_2.roll(), Game.Player_3.roll(), Game.Player_4.roll()


        # Determines the order of the game.
        #order = [roll, roll_2, roll_3, roll_4]
        # order.sort(key=lambda x: x.value, reverse=True)
        # order = [order[0].player, order[1].player,
        #         order[2].player, order[3].player]
        # del roll, roll_2, roll_3, roll_4
        # Tells the player the order of the game.
        # if order[0].id == 1:
        #     print("You will play first.")
        # else:
        #     print("Player " + str(order[0].id) + " will play first.")

        # Turn cycle boolean to track each player.
        # turn_cycle = True

        #
        # while turn_cycle:
        #   for current_player in order:
        #        print("------------------------------------------")
        #        if current_player.id == 1:
        #            enter_selection(current_player, board)
        #        else:
        #            print("AI turn.")
        #             current_player.play(board)



def main():
    
    game = Game()
    run = True
    while run:
        game.clock.tick(game.FPS)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_button_logic(mouse)
                
            game.draw_window()

main()           

pygame.quit()


