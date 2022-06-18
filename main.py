from board.board import Board
from board.space import *
import os
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
        
        WIDTH, HEIGHT = 900, 900
        self.FPS = 60
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.board = Board()
        self.show_board = True

        PIECE_SCALE = (45, 45)
        HAT = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', 'hat.png')), PIECE_SCALE)
        BATTLESHIP = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', 'battleship.png')), PIECE_SCALE)
        CAR = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', 'car.png')), PIECE_SCALE)
        BOOT = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', 'boot.png')), PIECE_SCALE)

        self.player   = Player(self.RED, HAT)
        self.player_2 = CPU(self.BLUE, BATTLESHIP)
        self.player_3 = CPU(self.GREEN, CAR)
        self.player_4 = CPU(self.PURPLE, BOOT)

        # Constant list that never changes.
        self.PLAYER_LIST = [self.player, self.player_2, self.player_3, self.player_4]
        # List of players that will be reorganized.
        self.players = [self.player, self.player_2, self.player_3, self.player_4]
        
        self.owner_rects = []      
        self.currentTurn = 0 
        pygame.display.set_caption("Monopoly")
        self.clock = pygame.time.Clock()
        pygame.font.init()

        self.texts = [Text("Welcome to monopoly!", 0, 0)]

        # List of all buttons that are currently on canvas. 
        # Initialized with the two mode buttons as they are 
        # visibile on launch.
        self.buttons = []
        self.buttons.append(Button("Start", 20, 40, 120, 40))

        # Boolean to tell the game if in menu
        self.in_manager = False

        # Trade system tracker variables.
        self.current_trade = 1
        self.trade_recipient = self.PLAYER_LIST[self.current_trade]
        self.trade_list = []
        self.rejected_offer = False
        # Exchange windows
        self.money_exchange = []
        self.property_exchange = [[],[]]

        # Property Manager
        self.selected_property = None

        # Visual representation of trade windows
        self.window_1, self.window_2 = (
        pygame.Rect(20, 200, 400, 400), 
        pygame.Rect(450, 200, 400, 400))

        # Formatted text of all current player cash.
        self.player_cash_texts = None

        # Tracker variable to get information about the current space a player has landed on.
        self.landed_on_space = None


    # Handles what happens when a button is hovered over.
    # Takes in passed button event if it is clicked.
    def handle_button_logic(self, mouse, event):
        for button in self.buttons:
            mouse_over_button = (button.rect.x <= mouse[0] 
            <= button.rect.x + button.rect.width and
            button.rect.y <= mouse[1] <= button.rect.y 
            + button.rect.height)
            if (mouse_over_button):
                button.current_color = button.color_over
                if event:
                    button.run(self)
            else:
                button.current_color = button.color

    # Method used to advance the game to the next turn.                
    def handle_turn(self):
        player = self.players[self.currentTurn]
        
        if player == self.player:
            self.texts = []
            self.update_player_text()
            in_jail = self.player.position == -1
            if in_jail:
                self.texts.append(Text("You're in jail.", 0, 0))
            else:
                self.texts.append(Text(f"It's your turn!", 0, 0))           
            self.buttons.extend([Button('Roll', 0, 25, 40, 30), 
            Button('Property Manager',50, 25, 165, 30), 
            Button('Trade',225, 25, 55, 30)])
        else:
            in_jail = player.position == -1
            if in_jail:
                self.texts.append(Text(f"Player {player.id} is in jail.", 0, 0))
            else:
                self.texts.append((Text(f"It's Player {player.id}'s turn! (CPU)", 0, 0)))
            self.buttons = [(Button("Turn", 0, 70, 70, 40))]           

    def update_player_text(self):
        for t in self.texts:
            if t in self.player_cash_texts:
                self.texts.remove(t)
        self.CASH_TEXT_X_POS = 700
        self.player_cash_texts = [Text(f"Your Cash:       "      
        f"${str(self.player.money)}", self.CASH_TEXT_X_POS, 0), 
        Text(f"Player 2 Cash: ${str(self.player_2.money)}", 
        self.CASH_TEXT_X_POS, 20),
        Text(f"Player 3 Cash: ${str(self.player_3.money)}", 
        self.CASH_TEXT_X_POS, 40),
        Text(f"Player 4 Cash: ${str(self.player_4.money)}", 
        self.CASH_TEXT_X_POS, 60)]
        self.texts.extend(self.player_cash_texts)

    def update_trade_text(self):
        self.texts = []
        player = self.PLAYER_LIST[self.current_trade]
        self.texts.extend([Text(f"You (Current cash: ${self.player.money})", 50, 0),
        Text(f"Player {str(player.id)} (Current cash: ${player.money})", 450, 0),
        Text(f"Cash: ${str(self.money_exchange[0])}", 20, 600),
        Text(f"Cash: ${str(self.money_exchange[1])}", 450, 600),
        Text(f"Total value ${str(self.get_total_value(0))}", 20, 650),
        Text(f"Total value ${str(self.get_total_value(1))}", 450, 650)])
        if self.rejected_offer:
            self.texts.append(Text("Offer Rejected.", 20, 750))

    def get_total_value(self, index):
        total = 0
        for p in self.property_exchange[index]:
            total += p.printed_price 
        total += self.money_exchange[index]
        return total
        
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
                        self.rejected_offer = False
                    if property_list is self.property_exchange[1]:
                        self.trade_list[1].properties.append(p_2)
                        self.property_exchange[1].remove(p_2)
                        done = True
                        self.rejected_offer = False
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
                            self.rejected_offer = False
                        if player is self.trade_list[1]:
                            self.property_exchange[1].append(p)
                            self.trade_list[1].properties.remove(p)
                            self.rejected_offer = False
                    i += 1
        self.update_trade_text()

    # Handle clicking on cards during property management.             
    def handle_click_definition(self, mouse):
        
        for prop in self.player.properties:
            card_rect = prop.card.rect
            mouse_over_card = (card_rect.x <= mouse[0] <= card_rect.x + card_rect.width and
            card_rect.y <= mouse[1] <= card_rect.y + card_rect.height)
            if mouse_over_card:
                self.texts = []
                self.buttons = []
                self.update_player_text()
                self.buttons.append(Button("Back", 0, 0, 40, 40))
                self.selected_property = prop
                prop.add_property_text(self.texts, self.buttons, self.player)


    def draw_properties(self, properties, base_x : int,
     base_y : int, edge_case=True, player=None, no_stack=None):
        seen = []
        for property in properties:
            card = property.card 
            image_str = card.image_str
            
            if image_str in seen and not no_stack:
                old_x = seen[seen.index(image_str) + 1]
                multiplier = seen[seen.index(image_str) + 2]
                multiplier += 1
                seen[seen.index(image_str) + 2] = multiplier 

                card.rect.x = old_x
                if edge_case:
                    old_y = seen[seen.index(image_str) + 3]
                    card.rect.y = old_y + (10 * multiplier)
                else:
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
                if edge_case:
                    seen.append(base_y)
                card.rect.x, card.rect.y = base_x, base_y
                card.draw(self.WIN)


    def draw_window(self):
        
        self.WIN.fill((70, 70, 70))      

             
        if self.trade_list:          
            self.draw_properties(self.trade_list[0].properties, 
            0, 40, edge_case=False)
            self.draw_properties(self.trade_list[1].properties, 
            400, 40, edge_case=False)
            pygame.draw.rect(self.WIN, (90, 90, 90), self.window_1)
            pygame.draw.rect(self.WIN, (90, 90, 90), self.window_2)
            self.draw_properties(self.property_exchange[0], 
            -20, 200)
            self.draw_properties(self.property_exchange[1],
             400, 200)     
        if self.in_manager:
            self.draw_properties(self.player.properties, -10, 5, edge_case=False, no_stack=True) 
        for button in self.buttons:
            pygame.draw.rect(self.WIN, button.current_color, button.rect)
            button.text.draw(self.WIN)
        for text in self.texts:
            text.draw(self.WIN)
        if self.show_board:
            self.WIN.blit(self.board.IMAGE, (150, 150))
            draw_all_players(self.players, self.WIN)
            self.draw_properties(self.player.properties,
             -55, 760, True, self.player)
            self.draw_properties(self.player_2.properties,
             -55, 200, player=self.player_2)
            self.draw_properties(self.player_3.properties,
             700, 200, player=self.player_3) 
            self.draw_properties(self.player_4.properties,
             400, 760, True, self.player_4)  
            for player in self.PLAYER_LIST:
                for p in player.properties:
                    rect = p.owner_rect 
                    pygame.draw.rect(self.WIN, rect[1], rect[0])
                    if type(p) is Monopoly_Property and p.current_tier >= 2:
                        p.draw_houses(self.WIN)

        pygame.display.update()

        

def main():
    
    game = Game()
    run = True
    while run:
        game.clock.tick(game.FPS)
        mouse = pygame.mouse.get_pos()
        events = pygame.event.get()
        pass_event = None
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass_event = event
                if game.in_manager:
                    game.handle_click_definition(mouse)
                elif game.show_board is False:
                    game.handle_click_card(mouse)  

        game.handle_button_logic(mouse, pass_event)
        game.draw_window()
            
main()           

pygame.quit()

# DEBUG CODE #
# #if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_k:
#                     game.player.money += 400
#                     game.texts = []
#                     game.update_player_text()
#                 if event.key == pygame.K_1:
#                     player = game.players[game.currentTurn]
#                     player.roll(game, r=1)             
#                 if event.key == pygame.K_2:
#                     player = game.players[game.currentTurn]
#                     player.roll(game, r=2) 
#                 if event.key == pygame.K_3:
#                     player = game.players[game.currentTurn]
#                     player.roll(game, r=3) 
#                 if event.key == pygame.K_4:
#                     player = game.players[game.currentTurn]
#                     player.roll(game, r=4) 
#                 if event.key == pygame.K_5:
#                     player = game.players[game.currentTurn]
#                     player.roll(game, r=5) 
#                 if event.key == pygame.K_6:
#                     player = game.players[game.currentTurn]
#                     player.roll(game, r=6) 
#                 if event.key == pygame.K_7:
#                     player = game.players[game.currentTurn]
#                     player.roll(game, r=7) 
#                 if event.key == pygame.K_8:
#                     player = game.players[game.currentTurn]
#                     player.roll(game, r=8) 
#                 if event.key == pygame.K_9:
#                     player = game.players[game.currentTurn]
#                     player.roll(game, r=9) 
#                 if event.key == pygame.K_KP_1:
#                     game.player.roll(game, r=1)
#                 if event.key == pygame.K_KP_2:
#                     game.player.roll(game, r=2)
#                 if event.key == pygame.K_KP_3:
#                     game.player.roll(game, r=3)
#                 if event.key == pygame.K_KP_4:
#                     game.player.roll(game, r=4)
#                 if event.key == pygame.K_KP_5:
#                     game.player.roll(game, r=5)
#                 if event.key == pygame.K_KP_6:
#                     game.player.roll(game, r=6)
#                 if event.key == pygame.K_KP_7:
#                     game.player.roll(game, r=7)
#                 if event.key == pygame.K_KP_8:
#                     game.player.roll(game, r=8)
#                 if event.key == pygame.K_KP_9:
#                     game.player.roll(game, r=9)


