from msilib.schema import Property
from unittest import skip
from board.board import Board
from board.space import Monopoly_Chance, Monopoly_Community_Chest, Monopoly_Property
from player import Player
from player import draw_all_players
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
        self.show_board = True
         # Store the players in a special variables so we can modify them more easily.
        self.player, self.player_2, self.player_3, self.player_4 = Player(self.RED), CPU(self.BLUE), CPU(self.GREEN), CPU(self.PURPLE)
        # Put the other player in a list.
        self.players = [self.player, self.player_2, self.player_3, self.player_4]
        # List of players that will be untouched
        self.PLAYER_LIST = [self.player, self.player_2, self.player_3, self.player_4]
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


        # Trade Stuff
        self.trade_list = []
        self.current_trade = 1

        # Exchange windows
        self.money_exchange = []
        self.property_exchange = [[],[]]

        self.window_1, self.window_2 = pygame.Rect(20, 200, 400, 400), pygame.Rect(450, 200, 400, 400)

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
                if (button.name == "Roll"):
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
                        card_text = self.landed_on_space.draw_card(self.player, self.players, self.board)
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
                        self.player.buy(self.landed_on_space)
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
                if (button.name == "Trade"):
                    self.texts = []
                    self.buttons = []

                    self.money_exchange = [0, 0]
                    self.show_board = False
                    self.current_trade = 1
                    self.trade_list.extend([self.player, self.player_2])

                    self.update_trade_text()

                    self.buttons.extend([Button("Next Player", 790, 0, 105, 40),
                    Button("Back", 0, 0, 40, 40),
                    Button("Increase", 140, 600, 75, 40),
                    Button("Decrease", 240, 600, 75, 40),
                    Button("Increase", 580, 600, 75, 40),
                    Button("Decrease", 680, 600, 75, 40),
                    Button("Make Trade", 20, 700, 120, 50)])

                if (button.name == "Next Player"):
                    if self.current_trade == 3:
                        self.current_trade = 1
                    else:
                        self.current_trade += 1

                    self.money_exchange = [0, 0]    

                    self.trade_list[0].properties.extend(self.property_exchange[0])
                    self.trade_list[1].properties.extend(self.property_exchange[1])
                    self.property_exchange = [[],[]]

                    player = self.PLAYER_LIST[self.current_trade]
                    self.trade_list[1] = player    

                
                    self.update_trade_text()
                if (button.name == "Back"):
                    self.trade_list[0].properties.extend(self.property_exchange[0])
                    self.trade_list[1].properties.extend(self.property_exchange[1])
                    self.property_exchange = [[],[]]
                    self.texts = []
                    self.buttons = []
                    self.show_board = True
                    self.trade_list = []
                    self.update_player_text()
                    self.texts.append(Text(f"It's your turn!", 0, 0))
                    self.buttons.extend([Button('Roll', 0, 25, 40, 30), Button("Property Manager",50, 25, 165, 30), 
                    Button('Trade', 225, 25, 55, 30)])
                if (button.name == "Increase"):
                    if button.x == 140 and self.money_exchange[0] + 50 <= self.trade_list[0].money:
                        self.money_exchange[0] += 50
                    if button.x == 580 and self.money_exchange[1] + 50 <= self.trade_list[1].money:
                        self.money_exchange[1] += 50
                    self.update_trade_text()
                if (button.name == "Decrease"):
                    if button.x == 240 and self.money_exchange[0] - 50 >= 0:
                        self.money_exchange[0] -= 50
                    if button.x == 680 and self.money_exchange[1] - 50 >= 0:
                        self.money_exchange[1] -= 50
                    self.update_trade_text()
                if (button.name == "Make Trade"):
                    player, player_2, player_exchange, player_2exchange = (self.trade_list[0], self.trade_list[1], 
                    self.property_exchange[0], self.property_exchange[1])

                    for property in player_exchange:
                        property.owner_rect[1] = player_2.color
                    for property in player_2exchange:
                        property.owner_rect[1] = player.color
                    player.properties.extend(player_2exchange)  
                    player_2.properties.extend(player_exchange)  
                    self.property_exchange = [[], []]      
                    player.money -= self.money_exchange[0]   
                    player.money += self.money_exchange[1] 

                    player_2.money -= self.money_exchange[1]   
                    player_2.money += self.money_exchange[0]    

                    self.money_exchange = [0, 0]
                    self.update_trade_text() 


                
    def handle_turn(self):
        player = self.players[self.currentTurn]
        
        if player == self.player:
            self.texts = []
            self.update_player_text()
            self.texts.append(Text(f"It's your turn!", 0, 0))
            self.buttons.extend([Button('Roll', 0, 25, 40, 30), Button('p_manage',50, 25, 165, 30), 
            Button('Trade',225, 25, 55, 30)])
        else:
            self.texts.append((Text(f"It's Player {player.id}'s turn! (CPU)", 0, 0)))
            player.play(self.board, self.owner_rects, self.texts, self.players)      
            self.buttons = [Button("next",0, 70, 70, 40)]   

    def update_player_text(self):
        self.player_cash_texts = [Text(f"Your Cash:      ${str(self.player.money)}", self.CASH_TEXT_X_POS, 0), 
        Text(f"Player 2 Cash: ${str(self.player_2.money)}", self.CASH_TEXT_X_POS, 20),
        Text(f"Player 3 Cash: ${str(self.player_3.money)}", self.CASH_TEXT_X_POS, 40),
        Text(f"Player 4 Cash: ${str(self.player_4.money)}", self.CASH_TEXT_X_POS, 60)]
        self.texts.extend(self.player_cash_texts)

    def update_trade_text(self):
        self.texts = []
        player = self.PLAYER_LIST[self.current_trade]
        self.texts.extend([Text(f"You (Current cash: ${self.player.money})", 50, 0),
                    Text(f"Player {str(player.id)} (Current cash: ${player.money})", 450, 0),
                    Text(f"Cash: ${str(self.money_exchange[0])}", 20, 600),
                    Text(f"Cash: ${str(self.money_exchange[1])}", 450, 600)])
        
    def handle_click_card(self, mouse):
        i = 0
        done = False
        for property_list in self.property_exchange:
            for p_2 in property_list:
                card_rect = p_2.card.rect
                
                mouse_over_card = (card_rect.x <= mouse[0] <= card_rect.x + card_rect.width and
                card_rect.y <= mouse[1] <= card_rect.y + card_rect.height)
                if mouse_over_card:
                    if property_list is self.property_exchange[0]:
                        self.trade_list[0].properties.append(p_2)
                        self.property_exchange[0].remove(p_2)
                        done = True
                    if property_list is self.property_exchange[1]:
                        self.trade_list[1].properties.append(p_2)
                        self.property_exchange[1].remove(p_2)
                        done = True
        if done is not True:
            for player in self.trade_list:
                properties = player.properties
                for p in properties:
                    card_rect = p.card.rect
                    
                    mouse_over_card = (card_rect.x <= mouse[0] <= card_rect.x + card_rect.width and
                    card_rect.y <= mouse[1] <= card_rect.y + card_rect.height)
                    if mouse_over_card:
                        if player is self.trade_list[0]:
                            self.property_exchange[0].append(p)
                            self.trade_list[0].properties.remove(p)
                        if player is self.trade_list[1]:
                            self.property_exchange[1].append(p)
                            self.trade_list[1].properties.remove(p)
                    i += 1


    def draw_properties(self, properties : list[Property], base_x : int, base_y : int, edge_case=True, player=None):
        seen = []
        for property in properties:
            card = property.card 
            image_str = card.image_str
            
            if image_str in seen:
                old_x = seen[seen.index(image_str) + 1]
                multiplier = seen[seen.index(image_str) + 2]
                multiplier += 1
                seen[seen.index(image_str) + 2] = multiplier 

                card.rect.x = old_x
                card.rect.y = base_y + (10 * multiplier)
                card.draw(self.WIN)
            else:
                if edge_case:
                    if player is self.player_2 and 55 == base_x:
                        base_x = -55
                        base_y += 80
                    if player is self.player_3 and 800 < base_x:
                        base_x = 700
                        base_y += 80    
                base_x += 55
                seen.extend([image_str, base_x, 0])

                card.rect.x, card.rect.y = base_x, base_y
                card.draw(self.WIN)

    def draw_window(self):
        
        # Fill screen with default board image.
        self.WIN.fill((180, 180, 180))      
              
        if self.trade_list:
            
            self.draw_properties(self.trade_list[0].properties, 0, 40, edge_case=False)
            self.draw_properties(self.trade_list[1].properties, 400, 40, edge_case=False)
            pygame.draw.rect(self.WIN, (80, 80, 80), self.window_1)
            pygame.draw.rect(self.WIN, (80, 80, 80), self.window_2)
            self.draw_properties(self.property_exchange[0], -20, 200)
            self.draw_properties(self.property_exchange[1], 400, 200)
            
        # Draw all buttons
        for button in self.buttons:
            pygame.draw.rect(self.WIN, self.BLACK, button.rect)
            button.text.draw(self.WIN)
        for text in self.texts:
            text.draw(self.WIN)
        if self.show_board:
            self.WIN.blit(self.board.IMAGE, (150, 150))
            draw_all_players(self.players, self.WIN)
            self.draw_properties(self.player.properties, -55, 760, player=self.player)
            self.draw_properties(self.player_2.properties, -55, 200, player=self.player_2)
            self.draw_properties(self.player_3.properties, 700, 200, player=self.player_3) 
            self.draw_properties(self.player_4.properties, 400, 760, player=self.player_4)  
            for player in self.PLAYER_LIST:
                for p in player.properties:
                    rect = p.owner_rect 
                    pygame.draw.rect(self.WIN, rect[1], rect[0])

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
                if game.show_board is False:
                    game.handle_click_card(mouse)

        game.draw_window()
            

    
        

main()           

pygame.quit()


