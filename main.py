from board.board import Board
from player import Player
from player import draw_all_players
from player_interface import *
from cpu import CPU
import pygame
import random
from text import Text

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
        welcome_text = font_test.render("Welcome to monopoly!", True, self.BLACK)
        welcome_text = Text('arial', 50, "Welcome to monopoly!", self.BLACK, 0, 0)

        self.texts = [welcome_text]

        # List of all buttons that are currently on canvas. 
        # Initialized with the two mode buttons as they are 
        # visibile on launch.
        self.buttons = {"single": pygame.Rect(20, 60, 70, 40), "multi" : pygame.Rect(100, 60, 70, 40)}

    def handle_button_logic(self, mouse):
        for button in self.buttons.values():
            mouse_over_button = (button.x <= mouse[0] <= button.x + button.width and
            button.y <= mouse[1] <= button.y + button.height)
            if (mouse_over_button):
                if (button == self.buttons.get("single")):
                    self.buttons = {"roll" : pygame.Rect(550, 10, 70, 40)}
                    self.texts = [Text('arial', 50, "Roll to determine game order:", self.BLACK, 0, 0)]
                if (button == self.buttons.get("multi")):
                    print("multi")
                if (button == self.buttons.get("roll")):
                    self.texts = []
                    self.buttons = {}
                    rolls = [random.randint(2, 12) for x in range(4)]
                    self.players = [x for x, x in sorted(zip(rolls, self.players))]
                    print(self.players)
                    self.texts.extend([Text('arial', 25, f"Player 1 rolled: {str(rolls[0])}", self.BLACK, 0, 60), 
                    Text('arial', 25, f"Player 2 rolled: {str(rolls[1])}", self.BLACK, 200, 60), 
                    Text('arial', 25, f"Player 3 rolled: {str(rolls[2])}", self.BLACK, 400, 60),
                    Text('arial', 25, f"Player 4 rolled: {str(rolls[3])}", self.BLACK, 600, 60)])


    def draw_window(self):
        
        # Fill screen with default board image.
        self.WIN.fill((180, 180, 180))
        self.WIN.blit(self.board.IMAGE, (150, 150))
        # Draw all players
        draw_all_players(self.players, self.WIN)
        # Draw all buttons
        for button in self.buttons.values():
            pygame.draw.rect(self.WIN, self.BLACK, button)
        for text in self.texts:
            text.draw(self.WIN)

        pygame.display.update()

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


