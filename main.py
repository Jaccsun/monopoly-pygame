from unittest import skip
from board.board import Board
from board.space import Monopoly_Chance, Monopoly_Community_Chest, Monopoly_Property
from player import Player
from player import draw_all_players
from player_interface import *
from cpu import CPU
import pygame
import random
from text import Text
from button import Button

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
         # Store the players in a special variables so we can modify them more easily.
        self.player, self.player_2, self.player_3, self.player_4 = Player(self.RED), CPU(self.GREEN), CPU(self.BLUE), CPU(self.PURPLE)
        # Put the other player in a list.
        self.players = [self.player, self.player_2, self.player_3, self.player_4]
        # Owner_rects that visualize owndership of properties
        self.owner_rects = []      
        # keeps track of the current turn in the game loop
        self.currentTurn = 0 
        pygame.display.set_caption("Monopoly")
        # Create pygame clock.
        self.clock = pygame.time.Clock()
        # Create the fonts that we'll be using.
        pygame.font.init()

        self.texts = [Text("Welcome to monopoly!", 0, 0)]
        # List of all buttons that are currently on canvas. 
        # Initialized with the two mode buttons as they are 
        # visibile on launch.
        self.buttons = [Button("Start", 20, 40, 120, 40)]


        # Formatted text of all current player cash.
        self.CASH_TEXT_X_POS = 700
        self.player_cash_texts = [Text(f"Your Cash:      ${str(self.player.money)}", self.CASH_TEXT_X_POS, 0), 
        Text(f"Player 2 Cash: ${str(self.player_2.money)}", self.CASH_TEXT_X_POS, 20),
        Text(f"Player 3 Cash: ${str(self.player_3.money)}", self.CASH_TEXT_X_POS, 40),
        Text(f"Player 4 Cash: ${str(self.player_4.money)}", self.CASH_TEXT_X_POS, 60)]

        # Tracker variable to get information about the current space a player has landed on.
        self.landed_on_space = None

    def handle_button_logic(self, mouse):
        # loops through each current button and checks if they've been pressed
        for button in self.buttons:
            # boolean variable to determine if a mouse is over a button
            mouse_over_button = (button.rect.x <= mouse[0] <= button.rect.x + button.rect.width and
            button.rect.y <= mouse[1] <= button.rect.y + button.rect.height)
            # condition checks for the type of button that has been pressed.
            if (mouse_over_button):
                if (button.name == "Start"):
                    self.buttons = [Button("Roll (Order)", 280, 0, 90, 40)]
                    self.texts = [Text("Roll to determine game order:", 0, 0)]
                if (button.name == "Roll (Order)"):
                    self.texts = []
                    self.buttons = []
                    rolls = [random.randint(2, 12) for x in range(4)]
                    self.players = [x[1] for x in sorted(zip(rolls, self.players), key= lambda test: test[0], reverse=True)]
                    self.texts.extend([Text(f"Player 1 rolled: {str(rolls[0])}", 0, 60), 
                    Text(f"Player 2 rolled: {str(rolls[1])}", 200, 60), 
                    Text(f"Player 3 rolled: {str(rolls[2])}", 400, 60),
                    Text(f"Player 4 rolled: {str(rolls[3])}", 600, 60)])
                    self.buttons  = [Button("Play", 0, 0, 70, 40)]
                if (button.name == "Play"):
                    self.texts = []
                    self.update_player_text()
                    self.buttons = []
                    self.handle_turn()
                if (button.name == "next"):
                    if self.currentTurn == 3:
                        self.currentTurn = 0
                    else:
                        self.currentTurn += 1
                    self.texts = []
                    self.update_player_text()
                    self.buttons = []
                    self.handle_turn()
                if (button.name == "roll"):
                    self.buttons = []
                    self.texts = []
                    self.update_player_text()
                    player_roll = random.randrange(2, 12)

                    self.landed_on_space = self.player.move(player_roll, self.board)

                    self.texts.append(Text(f"You rolled a {str(player_roll)} and landed on {self.landed_on_space.space_name}", 0, 0))

                    # Property space type.
                    if self.landed_on_space.IS_BUYABLE:
                        if (self.landed_on_space.owner == None):
                            self.texts.append(self.landed_on_space.get_prompt())
                            self.buttons.extend([Button('buy', 0, 50, 70, 40), Button('d_buy', 100, 50, 70, 40)])
                        elif (self.landed_on_space.owner == self.player):
                            self.texts.append(Text("You own this property.", 0, 20))
                            self.buttons = [Button("next",0, 50, 70, 40)]
                        else:   
                            self.texts.extend([Text(f"This property is owned by Player {str(self.landed_on_space.owner.id)}", 0, 100),
                            Text(f"Amount owned: {str(self.landed_on_space.get_current_price())}$", 350, 100)])
                            self.buttons.extend([Button("pay", 0, 50, 70, 40), Button("mortgage", 100, 50, 70, 40), 
                            Button("bankrupt", 200, 50, 70, 40)])
                    elif type(self.landed_on_space) is Monopoly_Chance: 
                        card_text = self.landed_on_space.draw_card(self.player, self.players, self.board)
                        self.texts.append(card_text)
                        self.buttons = [Button("next",0, 50, 70, 40)]
                    elif type(self.landed_on_space) is Monopoly_Community_Chest:
                        card_text = self.landed_on_space.draw_card(self.player, self.board, self.players)
                        self.texts.append(card_text)
                        self.buttons = [Button("next",0, 50, 70, 40)]
                    else:
                        self.texts.append(Text("Not buyable.", 0, 20))
                        self.buttons = [Button("next",0, 50, 70, 40)]

                # buy button for newly-unowned properties     
                if (button.name == "buy"):
                    self.buttons = []
                    self.texts = []
                    if(self.player.money - self.landed_on_space.printed_price < 0):
                        self.texts.append(Text("You don't have enough money to purchase this property.", 0, 20))
                    else: 
                        self.texts.append(Text(f"You have purchased {str(self.landed_on_space.space_name)}!", 0, 20))
                        self.player.buy(self.landed_on_space, self.owner_rects)
                    self.update_player_text()
                    self.buttons = [Button("next",0, 50, 70, 40)]
                    
                # dont buy property 
                if (button.name == "d_buy"): 
                    self.buttons = []
                    self.texts = []
                    self.texts.extend([Text(f"You decided not to buy {str(self.landed_on_space.space_name)}", 0, 20)],
                    self.player_cash_texts)
                    self.buttons = [Button("next",0, 50, 70, 40)]
                # pay player if landed on their property
                if (button.name == "pay"):
                    self.texts = []
                    if (self.player.money - self.landed_on_space.get_current_price() < 0):
                        self.texts.append(Text("You don't have enough money to pay.", 0, 0))
                    else:
                        self.texts.append(Text(f"You paid Player {str(self.landed_on_space.owner.id)} {str(self.landed_on_space.get_current_price())}$", 
                        0, 0))
                        self.player.pay(self.landed_on_space.owner, self.landed_on_space)
                    self.buttons = [Button("next",0, 50, 70, 40)]
                    self.update_player_text()
                # mortgage properties button
                if (button.name == "mortgage"):
                    print("Mortage properties?")
                    self.buttons = [Button("next",0, 50, 70, 40)]
                # bankrupt properties button
                if (button.name == "bankrupt"):
                    print("Thanks for playing!")
                    self.buttons = [Button("next",0, 50, 70, 40)]
                    
    def handle_turn(self):
        player = self.players[self.currentTurn]
        
        if player == self.player:
            self.texts = []
            self.update_player_text()
            self.texts.append(Text(f"It's your turn!", 0, 0))
            self.buttons.extend([Button('roll', 0, 25, 40, 30), Button('p_manage',50, 25, 165, 30), 
            Button('trade',225, 25, 55, 30)])
        else:
            self.texts.append((Text(f"It's Player {player.id}'s turn! (CPU)", 0, 0)))
            player.play(self.board, self.owner_rects, self.texts, self.players)      
            self.buttons = [Button("next",0, 70, 70, 40)]   

    def draw_window(self):
        
        # Fill screen with default board image.
        self.WIN.fill((180, 180, 180))
        self.WIN.blit(self.board.IMAGE, (150, 150))
        # Draw all players
        draw_all_players(self.players, self.WIN)
        # Draw all buttons
        for button in self.buttons:
            pygame.draw.rect(self.WIN, self.BLACK, button.rect)
            button.text.draw(self.WIN)
        for text in self.texts:
            text.draw(self.WIN)
        for rect in self.owner_rects:
            pygame.draw.rect(self.WIN, rect[1], rect[0])
        
        x = -55
        seen = []
        for property in self.player.properties:
            for k in range(len(seen)):
                if (property.p_image is seen[k][0]):
                    self.WIN.blit(property.p_image, (seen.get(property.p_image), 760 + 40))
            x += 55
            seen.append((property.p_image, x))
            self.WIN.blit(property.p_image, (x, 760))
        

        pygame.display.update()

    def update_player_text(self):
        self.player_cash_texts = [Text(f"Your Cash:      ${str(self.player.money)}", self.CASH_TEXT_X_POS, 0), 
        Text(f"Player 2 Cash: ${str(self.player_2.money)}", self.CASH_TEXT_X_POS, 20),
        Text(f"Player 3 Cash: ${str(self.player_3.money)}", self.CASH_TEXT_X_POS, 40),
        Text(f"Player 4 Cash: ${str(self.player_4.money)}", self.CASH_TEXT_X_POS, 60)]
        self.texts.extend(self.player_cash_texts)
        
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


