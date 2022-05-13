from unittest import skip
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
        # keeps track of the current turn in the game loop
        self.currentTurn = 0 
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
                    self.buttons = {"roll_order" : pygame.Rect(550, 10, 70, 40)}
                    self.texts = [Text('arial', 50, "Roll to determine game order:", self.BLACK, 0, 0)]
                if (button == self.buttons.get("multi")):
                    print("multi")
                if (button == self.buttons.get("roll_order")):
                    self.texts = []
                    self.buttons = {}
                    rolls = [random.randint(2, 12) for x in range(4)]
                    self.players = [x[1] for x in sorted(zip(rolls, self.players), key= lambda test: test[0], reverse=True)]
                    self.texts.extend([Text('arial', 25, f"Player 1 rolled: {str(rolls[0])}", self.BLACK, 0, 60), 
                    Text('arial', 25, f"Player 2 rolled: {str(rolls[1])}", self.BLACK, 200, 60), 
                    Text('arial', 25, f"Player 3 rolled: {str(rolls[2])}", self.BLACK, 400, 60),
                    Text('arial', 25, f"Player 4 rolled: {str(rolls[3])}", self.BLACK, 600, 60)])
                    self.buttons  = {"next" : pygame.Rect(0, 0, 70, 40)}
                if (button == self.buttons.get("next")):
                    self.texts = []
                    self.buttons = {"next" : pygame.Rect(200, 0, 70, 40)}
                    self.handle_turn()

                if (button == self.buttons.get('roll')):

                    self.buttons = {}
                    self.texts = []
                    current_player = self.players[self.currentTurn]
                    player_roll = random.randrange(0, 12)

                    self.texts.append(Text('arial', 25, f"You rolled a {str(player_roll)}", self.BLACK, 0, 0))
                    # Tells the player what they rolled.
                    current_player.move(player_roll)

                    # Uses the info from the roll and the new player position to determine the space they landed on.
                    landed_on_space = self.board.space[current_player.position]

                    current_player.rectangle.x = landed_on_space.x
                    current_player.rectangle.y = landed_on_space.y 

                    # Property space type.
                    if landed_on_space.IS_BUYABLE:
                        if (landed_on_space.owner == None):
                            self.texts.append(landed_on_space.get_prompt(self.BLACK))
                            self.buttons['buy'] = pygame.Rect(0, 40, 70, 40)
                            self.buttons['d_buy'] = pygame.Rect(50, 40, 70, 40)
                        elif (landed_on_space.owner == current_player):
                            self.texts.append(Text('arial', 25, f"You own this propety", self.BLACK, 600, 20))
                        else:   
                            self.texts.append(Text('arial', 25, f"This property is owned by Player {str(landed_on_space.owner.id)}", self.BLACK, 600, 60))
                            self.texts.append(Text('arial', 25, f"Amount owned: {str(landed_on_space.get_current_price())}$", self.BLACK, 600, 60))

                            self.buttons['pay'] = pygame.Rect(0, 10, 70, 40)
                            self.buttons['mortgage'] = pygame.Rect(200, 10, 70, 40)
                            self.buttons['bankrupt'] = pygame.Rect(400, 10, 70, 40)
                    else:
                        self.texts.append(Text('arial', 25, f"Not buyable.", self.BLACK, 0, 20))
                        self.buttons  = {"next" : pygame.Rect(0, 0, 70, 40)}

                # buy button for newly-unowned properties     
                if (button == self.buttons.get('buy')):
                    current_player = self.players[self.currentTurn]   
                    if(current_player.money - landed_on_space.printed_price < 0):
                        print("You don't have enough money to purchase this property.")
                    else: 
                        print("You have purchased " + str(landed_on_space.space_name) + "!") 
                        self.texts.append(Text('arial', 25, f"You have purchased {str(landed_on_space.space_name)}!", self.BLACK, 0, 20))
                        current_player.buy(landed_on_space)
                # dont buy property 
                if (button == self.buttons.get('d_buy')): 
                    skip
                # pay player if landed on their property
                if (button == self.buttons.get('pay')):
                    if (current_player.money - landed_on_space.get_current_price() < 0):
                        print("You don't have enough money to pay.")
                    else:
                        print("You paid" + " Player " + str(landed_on_space.owner.id) + " " + str(landed_on_space.get_current_price()) + "$")
                        current_player.pay(landed_on_space.owner, landed_on_space)
                        in_selection = False
                # mortgage properties button
                if (button == self.buttons.get('mortgage')):
                    print("Mortage properties?")
                # bankrupt properties button
                if (button == self.buttons.get('bankrupt')):
                    print("Thanks for playing!")
                    
    def handle_turn(self):
        player = self.players[self.currentTurn]
        
        if type(player) == CPU:
            self.currentTurn = player.play(self.board, self.currentTurn)
            self.texts.append((Text('arial', 25, f"It's Player {player.id}'s turn! (CPU)", self.BLACK, 0, 0)))
        else:
            self.texts.append((Text('arial', 25, f"It's your turn!", self.BLACK, 0, 0)))
            self.texts.append((Text('arial', 25, f"Roll", self.WHITE, 0, 25)))
            self.buttons['roll'] = pygame.Rect(0, 25, 40, 30)
            self.texts.append((Text('arial', 25, f"Property Manager", self.WHITE, 50, 25)))
            self.buttons['p_manage'] = pygame.Rect(50, 25, 165, 30)
            self.texts.append((Text('arial', 25, f"Trade", self.WHITE, 225, 25)))
            self.buttons['trade'] = pygame.Rect(225, 25, 55, 30)

        

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


