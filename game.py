import os
from cpu import CPU
import pygame
from window.text import Text
from window.button import Button
from tradesystem import TradeSystem
from propertymanager import PropertyManager
from board.board import Board
from player import Player
from board.space import Monopoly_Space
class Game():

    def __init__(self):
        # Color constants.
        self.WHITE, self.BLUE, self.BLACK, self.RED, self.GREEN, self.PURPLE, self.GREY  = ((255, 255, 255), 
        (0, 0, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (255, 0, 255), (200, 200, 200))
        
        WIDTH, HEIGHT = 900, 900
        self.FPS = 60
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.board = Board()

        PIECE_SCALE = (45, 45)
        HAT = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', 'hat.png')), PIECE_SCALE)
        BATTLESHIP = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', 'battleship.png')), PIECE_SCALE)
        CAR = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', 'car.png')), PIECE_SCALE)
        BOOT = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', 'boot.png')), PIECE_SCALE)

        self.player1 = Player(self.RED, HAT)
        self.player2 = CPU(self.BLUE, BATTLESHIP)
        self.player3 = CPU(self.GREEN, CAR)
        self.player4 = CPU(self.PURPLE, BOOT)

        # Constant list that never changes.
        self.PLAYER_LIST = [self.player1, self.player2, self.player3, self.player4]
        # List of players that will be reorganized.
        self.players = [self.player, self.player2, self.player3, self.player4]
        
        self.ownerRects = []      
        self.currentTurn = 0 
        pygame.display.set_caption("Monopoly")
        self.clock = pygame.time.Clock()
        pygame.font.init()

        self.texts = []
        self.texts.append([Text("Welcome to monopoly!", 0, 0)])
        self.buttons = []
        self.buttons.append(Button("Start", 20, 40, 120, 40))

        self.tradeSystem = TradeSystem()
        self.propertyManager = PropertyManager()

        # Formatted text of all current player cash.
        self.player_cash_texts = None

        # Tracker variable to get information about the current space a player has landed on.
        self.landed_on_space = None

        #-- Drawing information --#

        self.drawPlayerPieces = True
        self.drawPropertyCards = True

    # --- Information-----
    def get_all_known_properties(self) -> list[Monopoly_Space]:
        allKnownPropertyList = []
        for player in self.PLAYER_LIST:
            for property in player.properties:
                allKnownPropertyList.append(property)
        for propertyList in self.tradeSystem.propertyExchange:
            for property in propertyList:
                allKnownPropertyList.append(property)
        return allKnownPropertyList

    # -------

    # Method used to advance the game to the next turn.                
    def advance_turn(self):
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
            Button('Trade',225, 25, 55, 30),
            Button('Bankrupt', 290, 25, 80, 30)])
        else:
            in_jail = player.position == -1
            if in_jail:
                self.texts.append(Text(f"Player {player.id} is in jail.", 0, 0))
            else:
                self.texts.append((Text(f"It's Player {player.id}'s turn! (CPU)", 0, 0)))
            self.buttons = [(Button("Turn", 0, 70, 70, 40))]           

    # --------UPDATE -------------------

    def update_player_text(self):
        for t in self.texts:
            if t in self.player_cash_texts:
                self.texts.remove(t)
        self.CASH_TEXT_X_POS = 700
        self.player_cash_texts = [Text(f"Your Cash:       "      
        f"${str(self.player.money)}", self.CASH_TEXT_X_POS, 0), 
        Text(f"Player 2 Cash: ${str(self.player2.money)}", 
        self.CASH_TEXT_X_POS, 20),
        Text(f"Player 3 Cash: ${str(self.player3.money)}", 
        self.CASH_TEXT_X_POS, 40),
        Text(f"Player 4 Cash: ${str(self.player4.money)}", 
        self.CASH_TEXT_X_POS, 60)]
        self.texts.extend(self.player_cash_texts)

    def update_trade_text(self):
        self.texts = []
        player = self.PLAYER_LIST[self.current_trade]
        self.texts.extend([Text(f"You (Current cash: ${self.player.money})", 50, 0),
        Text(f"Player {str(player.id)} (Current cash: ${player.money})", 450, 0),
        Text(f"Cash: ${str(self.tradeSystem.money_exchange[0])}", 20, 600),
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
        
    # ------HANDLING ALL HOVER AND CLICK FUNCTIONALITY ---------------------------------

    def handle_mouse_position_event(self, mouseDown : pygame.event.Event):
        mousePos = pygame.mouse.get_pos()

        # Always do a button scan. 
        button = self._find_hovered_button(self.buttons, mousePos)
        property = None

        # Only look for properties if needed.
        if self.propertyManager.turnedOn or self.tradeSystem.turnedOn:
            property = self._find_hovered_property(self.get_all_known_properties()) 

        # If mouse is over button. 
        if button:
            print("test1")
        # If mouse if over property.
        if property:
            print("test2")
        # Finally, advance to mouse down action.
        if mouseDown:
            self.handle_mouse_down(button, property)
    
    def handle_mouse_down(self, button : Button, property : Monopoly_Space):
        # WE ARE NOW HANDLING ACTIONS.
        self._handle_mouse_down_button(button)
        if self.tradeSystem.turnedOn:
            self.tradeSystem.handle_property_click(property)
        if self.propertyManager.turnedOn:
            self._handle_mouse_down_card_p_manage()
        

    # Handles what happens when a button is hovered over.
    # Takes in passed button event if it is clicked.
    def _handle_mouse_down_button(self, button):
        button.run(self)

    #--------------------------------------------#

    def _find_hovered_button(self, buttons : list[Button], mousePos) -> Button:
        for button in buttons:
            mouse_over_button = (button.rect.x <= mousePos[0] 
            <= button.rect.x + button.rect.width and
            button.rect.y <= mousePos[1] <= button.rect.y 
            + button.rect.height)
            if (mouse_over_button):
                return button
        return None

    # Check the list of properties to find 
    def _find_hovered_property(self, mousePos, propertyList : list[Monopoly_Space] = None
    ) -> Monopoly_Space.cardImageRect:
        for property in propertyList:
            cardImageRect = property.cardImageRect
            mouse_over_card = (cardImageRect.x <= mousePos[0] <= cardImageRect.x + cardImageRect.width and
            cardImageRect.y <= mousePos[1] <= cardImageRect.y + cardImageRect.height)
            if mouse_over_card:
                return property
        return None
    
    #--- Handling all the drawing for the game ---# 

    def draw(self):
        
        self.WIN.fill((70, 70, 70))      

        # Property and trade systems.
        if self.tradeSystem.turnedOn:          
            self.__draw_property_cards(self.trade_list[0].properties, 
            0, 40, edgeCase=False)
            self.__draw_property_cards(self.trade_list[1].properties, 
            400, 40, edgeCase=False)
            pygame.draw.rect(self.WIN, (90, 90, 90), self.window_1)
            pygame.draw.rect(self.WIN, (90, 90, 90), self.window_2)
            self.__draw_property_cards(self.property_exchange[0], 
            -20, 200)
            self.__draw_property_cards(self.property_exchange[1],
             400, 200)     
        if self.propertyManager.turnedOn:
            self.__draw_property_cards(self.player.properties, -10, 5, edgeCase=False, stack=True) 

        # All buttons and texts.
        for button in self.buttons:
            pygame.draw.rect(self.WIN, button.current_color, button.rect)
            button.text.draw(self.WIN)
        for text in self.texts:
            text.draw(self.WIN)

        # If board is currently shown.
        if self.board.show:
            self.WIN.blit(self.board.IMAGE, (150, 150))
        
        # Players and properties
        if self.drawPlayerPieces:
            for player in self.PLAYER_LIST:
                player.draw(self.WIN)

        if self.drawPropertyCards:
            self._draw_property_cards(self.player.properties,
                (55, 760), True, self.player)
            self._draw_property_cards(self.player2.properties,
                (-55, 200), player=self.player2)
            self._draw_property_cards(self.player3.properties,
                (700, 200), player=self.player3) 
            self._draw_property_cards(self.player4.properties,
                (400, 760), True, self.player4)  

        for player in self.PLAYER_LIST:
            for p in player.properties:
                rect = p.owner_rect 
                pygame.draw.rect(self.WIN, rect[1], rect[0])
                if p.type is 'property' and p.current_tier >= 2:
                    p.draw_houses(self.WIN)

        pygame.display.update()

    def _draw_property_cards(self, properties : list[Monopoly_Space], 
    startingCoords : tuple[int, int], edgeCase : bool,
    stack : bool =False):
        baseX = startingCoords[0]
        baseY = startingCoords[1]
        seen = []
        for property in properties:
            card = property.card 
            image_str = card.image_str
            
            if image_str in seen and stack:
                old_x = seen[seen.index(image_str) + 1]
                multiplier = seen[seen.index(image_str) + 2]
                multiplier += 1
                seen[seen.index(image_str) + 2] = multiplier 

                card.rect.x = old_x
                if edgeCase:
                    old_y = seen[seen.index(image_str) + 3]
                    card.rect.y = old_y + (10 * multiplier)
                else:
                    card.rect.y = baseY + (10 * multiplier)
                card.draw(self.WIN)
            else:
                # if edgeCase:
                #     if player is self.player2 and 55 == baseX:
                #         baseX = -55
                #         baseY += 80
                #     if player is self.player3 and 800 < baseX:
                #         baseX = 700
                #         baseY += 80    
                baseX += 55
                seen.extend([image_str, baseX, 0])
                if edgeCase:
                    seen.append(baseY)
                card.rect.x, card.rect.y = baseX, baseY
                card.draw(self.WIN)


        

