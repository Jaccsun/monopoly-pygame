import os
import itertools
import random
from typing import Tuple
from board.board import Board
from board.space import *
from window.text import Text
from window.button import Button
import pygame
from pygame import Rect

# Color constants.
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)

HAT = pygame.image.load(os.path.join('Assets', 'hat.png'))
BATTLESHIP = pygame.image.load(os.path.join('Assets', 'battleship.png'))
CAR = pygame.image.load(os.path.join('Assets', 'car.png'))
BOOT = pygame.image.load(os.path.join('Assets', 'boot.png'))

class Player:

    id = itertools.count(start = 1).__next__

    def __init__(self, color : Tuple, image):

        self.id = Player.id()
        self.position = 0

        self.money = 1500
        self.properties = []
        self.monopolies = []
        self.railroads_owned = 0

        self.color = color
        self.rectangle = pygame.Rect(690, 690, 35, 35) 
        self.image = image

        self.jail_turn = -1
        self.roll_num = None


    def get_prop_monopoly_status(self, property):
        color, count = self.card.image_str, 0
        for property in self.properties:
            if property.card.image_str == color:
                count += 1
        if count == 3 or (count == 2 and 
        (color == "BROWN_P" or color == "BLUE_P")):
            return True
        return False

    def has_monopoly_for_color(self, color : str): 
        count = 0 
        for property in self.properties:
            if property.color == color: 
                count += 1
        if count == 3 or (count == 2 and 
        (color == 'brown' or color == 'blue')):
            return True
        return False



# ---------OLD ----------------------------------------------------------------------------


    # Moves player to a position on the board, accounts
    # for moving past GO.
    def move(self, roll : int, board : Board):
        if(self.position + roll >= 40):
            self.money += 200
            self.position = (self.position + roll) - 40
        else: 
            self.position += roll

        landedOnSpace = board.space[self.position]
        
        self.rectangle.x = landedOnSpace.x
        self.rectangle.y = landedOnSpace.y 

        return landedOnSpace

    def evauluate_ownable(self, game, landedOnSpace, roll, cpu=False):

        who = f"Player {self.id}" if cpu else "You"
        texts, buttons = game.texts, game.buttons
        if (landedOnSpace.owner == None):

            # If cpu can afford, they will purchase property.
            # (Should actually be a dice roll)
            if cpu and self.money - landedOnSpace.printed_price > 0:
                buttons.clear()
                texts.append(Text(who + f" bought {landedOnSpace.name}", (0, 20)))
                self.buy(landedOnSpace)
                buttons.append(Button("next", Rect(0, 50, 70, 40)))
            elif cpu:
                texts.append(Text(who + f" can't afford to pay.", (0, 20)))
                buttons.append(Button("next", Rect(0, 50, 70, 40)))
                # Attempt mortgage
            if not cpu:
                buttons.clear()
                # Provide buy and don't buy buttons to player.
                buttons.extend([Button('Buy', Rect(0, 50, 70, 40)), 
                Button("Don't Buy", Rect(100, 50, 70, 40))])    
        # If player is owner.
        elif (landedOnSpace.owner == self):
            # Print text that player owns and move to next turn.
            if cpu:
                texts.append(Text(who + f" owns the property.", (0, 20)))
            else:
                texts.append(Text(who + " own the property.", (0, 20)))
            buttons.clear()
            buttons.append(Button("next", Rect(0, 50, 70, 40)))
        # If owner is other player.
        else:   
            # If cpu can afford.
            if cpu and self.money - landedOnSpace.get_current_price() > 0:
                # Pay the other player.
                self.pay(game, roll, cpu=True)
                if landedOnSpace.type != 'utility':
                    texts.append(Text(who + f" landed on Player {str(landedOnSpace.owner.id)}'s "
                    + f"property and paid them {landedOnSpace.get_current_price()}$", (0, 20)))
                buttons.clear()
                buttons.append(Button("next", Rect(0, 50, 70, 40)))
            # If cpu can't afford.
            elif cpu:
                attempt_mortgage = self.attempt_mortgage(landedOnSpace.get_current_price())
                if attempt_mortgage:
                    texts.append(Text(f"CPU landed on Player {str(landedOnSpace.owner.id)}'s "
                    + f"property and had to mortgage.", (0, 40)))
                else:
                    self.bankrupt(game)
                
                buttons.clear()
                buttons.append(Button("next", Rect(0, 50, 70, 40)))
            # If player.
            if not cpu:
                buttons.clear()
                # Tell who owner is.
                texts.append(Text(f"This property is owned by Player " + 
                + str(landedOnSpace.owner), (0, 100)))

                # If not mortaged.
                if landedOnSpace.current_tier > -1:
                    texts.append(Text(f"Amount owned: " 
                    + f"{str(landedOnSpace.get_current_price())}$", (350, 100)))
                    buttons.extend([Button("Pay", Rect(0, 50, 70, 40)), 
                    Button("Property Manager", Rect(100, 50, 70, 40)), 
                    Button("Bankrupt", Rect(200, 50, 70, 40))])
                # If mortgaged.
                else:
                    texts.append(Text(f"Property is mortagaged", (350, 100)))
                    buttons.clear()
                    buttons.append(Button("next", Rect(0, 50, 70, 40)))

    def roll(self, game, r=None, cpu=False):
        
        who = f"Player {self.id}" if cpu else "You"
        # Boolean to determine if player is in jail.
        IN_JAIL = (self.position == -1)
        # Set pointers for each value.
        board = game.board
        texts = game.texts
        players = game.players
        buttons = game.buttons

        # Clear all current text.
        texts.clear()
        # Roll is random, unless specificed.
        roll = r if r else random.randrange(2, 12)
        self.roll_num = roll
        # Escape by default is true.
        escape = True
        # If player is in jail
        if IN_JAIL:
            # If player has exhausted all rolls.
            if self.jail_turn == 3:
                texts.append(Text(who + " must pay $50 to escape jail.", (0, 80)))
                self.money -= 50
                self.jail_turn = -1
                # Set position to just visiting and evalute roll.
                self.position = 10
                escape = True
            # Attempt a roll if not.
            else:
                roll_1 = random.randrange(1, 6)
                roll_2 = random.randrange(1, 6)
                # If roll is successful.
                if roll_1 == roll_2:
                    texts.append(Text(who + f" rolled a {str(roll_1 + roll_2)} "
                    + f"with doubles and escaped jail.", (0, 80)))
                    self.position = 10
                    escape = True
                # If roll fails.
                else:
                    texts.append(Text(who + f" rolled a {str(roll_1 + roll_2)} "
                    + f"with no double and didn't escape jail.", (0, 80)))
                    self.jail_turn += 1
                    buttons.clear()
                    buttons.append(Button("next", Rect(0, 50, 70, 40)))    
                    escape = False
        # If player has escaped jail, proceed as normal.
        if escape:
            # Calclulate the space and communicate info to player.
            landedOnSpace = self.move(roll, board)
            game.landedOnSpace = landedOnSpace
            texts.append(Text(who + f" rolled a {roll} and "
            + f"landed on {landedOnSpace.name}", (0, 0))) 

            # Update the rectangle of the player.
            self.rectangle.x = landedOnSpace.x
            self.rectangle.y = landedOnSpace.y

            # If the space is ownable
            if landedOnSpace.isOwnable:
                # Evaluate the ownable property.
                self.evauluate_ownable(game, landedOnSpace, roll, cpu) 
            # If space of chance or community chest type.
            elif (landedOnSpace.type == 'chance'
            or landedOnSpace.type == 'comChest'): 

                # Call the draw card method.
                buttons.clear()
                card_text = self.draw_card(landedOnSpace, board, players)
                texts.append(card_text)
                buttons.append(Button("next", Rect(0, 50, 70, 40)))
        
            # If space is one of the two taxes.
            elif (landedOnSpace.name == "Luxury Tax" 
            or landedOnSpace.name == "Income Tax"):
                self.pay(game, roll, cpu=cpu)
            elif (landedOnSpace.name == "Go to Jail"):
                self.teleport(-1, game.board)
                buttons.clear()
                buttons.append(Button("next", Rect(0, 50, 70, 40)))
            elif (landedOnSpace.name == "GO"):
                texts.append(Text("Collect $200", (0, 20)))
                self.money += 200
                buttons.clear()
                buttons.append(Button("next", Rect(0, 50, 70, 40)))
            else:
                texts.append(Text("Not buyable.", (0, 20)))
                buttons.clear()
                buttons.append(Button("next", Rect(0, 50, 70, 40)))
            game.update_player_text() 

    # Teleports the player to a certain position on the board.
    def teleport(self, space : int, board : Board):
        self.position = space
        if space != -1:
            s = board.space[self.position]
        else:
            s = board.JAIL
            self.jail_turn = 0
        self.rectangle.x = s.x
        self.rectangle.y = s.y 


    # Adds property to players inventory and calculates
    # the position of the owner_rect.
    def buy(self, landedOnSpace : MonopolySpace):

        self.money -= landedOnSpace.printed_price
        self.properties.append(landedOnSpace)
        landedOnSpace.owner = self
        if landedOnSpace.type == 'property':
            landedOnSpace.increase_tier()
        
        BOTTOM_Y = 692
        LEFT_X = 150
        RIGHT_X = 696

        x = landedOnSpace.x
        y = landedOnSpace.y

        if (landedOnSpace.x == LEFT_X):
            x += 80
            y += 11
        elif (landedOnSpace.x == RIGHT_X):
            x -= 34
            y += 10
        elif (landedOnSpace.y == BOTTOM_Y):
            y -= 30
            x += 15
        else:
            x += 12
            y += 70
        landedOnSpace.owner_rect = [pygame.Rect(x, y, 10, 10), self.color]
        landedOnSpace.owner = "player" + str(self.id)

    # Pays the price owed on a space. Also works for the Taxes.
    def pay(self, game, roll=None, cpu=False):    
        who = f"Player {self.id}" if cpu else "You"
        game.texts.clear() 
        game.buttons.clear()
        landedOnSpace = game.landedOnSpace

        roll = self.roll_num 

        is_income = landedOnSpace.name == "Income Tax"
        is_luxury = landedOnSpace.name == "Luxury Tax"
        is_tax = is_income or is_luxury
        is_railroad = landedOnSpace.type == 'railroad'
        is_utility = landedOnSpace.type == 'utility'

        if is_income:
            price = 200
        elif is_luxury :
            price = 100
        elif is_railroad:
            owner = landedOnSpace.owner
            tier = -1
            for p in owner.properties:
                if p.type == 'railroad':
                    tier += 1
            landedOnSpace.current_tier = tier
            price = landedOnSpace.get_current_price()
        elif is_utility:
            owner = landedOnSpace.owner
            tier = -1
            for p in owner.properties:
                if p.type == 'railroad':
                    tier += 1     
            landedOnSpace.current_tier = tier
            price = landedOnSpace.get_current_price() * roll
                         
        else:
            price = landedOnSpace.get_current_price()
        texts = game.texts
        if (self.money - price < 0):
            w = "doesn't" if cpu else "don't"
            texts.append(Text(who + " " + w   
            + " have enough money to pay.", (0, 20)))
        
        else:
            if is_tax:
                texts.append(Text(who + " paid the fee.", (0, 20)))
            else:
                texts.append(Text(who + f" paid Player {str(landedOnSpace.owner.id)} "
                f"{str(price)}$", (0, 0)))
                landedOnSpace.owner.money += price
            self.money -= price
        game.buttons = [Button("next", Rect(0, 50, 70, 40))]

    # Bankrupts the player.
    def bankrupt(self, game):
        players = game.players
        players.remove(self)

    # Determines whether the property is a monopoly.
    def is_monopoly(self, property : MonopolySpace):
        color, count = property.card.image_str, 0
        for p in self.properties:
            if p.card.image_str == color:
                count += 1
        if count == 3 or (count == 2 and 
        (color == "BROWN_P" or color == "BLUE_P")):
            return True
        return False     

    # Mortgage a property.
    def mortgage(self, property : MonopolySpace):
        property.current_tier = -1
        self.money += property.mortgage_value

    # Unmortgage a property.
    def unmortgage(self, property : MonopolySpace):
        if property.type == 'utility':
            if self.money - property.mortgage_value > 0:
                count = 0
                for p in self.properties:
                    if p.type == 'utility':
                        count += 1
                if count == 2:
                    property.current_tier = 1
                else:
                    property.current_tier = 0
                self.money -= property.mortgage_value
        if property.type == 'railroad':
            if self.money - property.mortgage_value > 0:
                count = 0
                for p in self.properties:
                    if p.type == 'railroad':
                        count += 1
                if count == 1:
                    property.current_tier = 0
                elif count == 2:
                    property.current_tier = 1
                elif count == 3:
                    property.current_tier = 2
                elif count == 4:
                    property.current_tier = 3
                self.money -= property.mortgage_value
        if property.type == 'property':
            if self.money - property.mortgage_value > 0:
                if self.is_monopoly(property):
                    property.current_tier = 1
                else:
                    property.current_tier = 0
                self.money -= property.mortgage_value

    def draw_card(self, chance : MonopolySpace, board : Board, players):
        r = chance.draw_card()
        Y_CONST = 20
        match r:
            case 0:
                self.teleport(0, self)
                self.money += 200
                return Text("Advance to \"Go\". (Collect $200)", y=Y_CONST)
            case 1:
                ILLINOIS_INDEX = 24
                if self.position > ILLINOIS_INDEX:
                    self.money += 200
                self.teleport(ILLINOIS_INDEX, board)
                return Text("Advance to Illinois Ave. If you pass Go, collect $200.", y=Y_CONST)
            case 2:
                ST_CHARLES_INDEX = 24
                if self.position > ST_CHARLES_INDEX:
                    self.money += 200
                self.teleport(ST_CHARLES_INDEX, board)
                return Text("Advance to St. Charles Place. If you pass Go, collect $200.", y=Y_CONST)
            case 3:
                ELECTRIC_COMPANY_INDEX = 12
                WATER_WORKS_INDEX = 28
                electric_distance = abs(self.position - ELECTRIC_COMPANY_INDEX)
                water_distance = abs(self.position - WATER_WORKS_INDEX)
                
                if (electric_distance > water_distance):
                    self.teleport(ELECTRIC_COMPANY_INDEX, board)
                else:
                    self.teleport(WATER_WORKS_INDEX, board)
                    
                return Text("Advance token to the nearest Utility. "
                + "If unowned, you may buy it from the Bank." 
                + "If owned, throw dice and pay owner a total "
                + "10 (ten) times the amount thrown.", y=Y_CONST)
            case 4:
                READING_RAILROAD, PENNSYLVANIA_RAILROAD = 5, 15
                B_O_RAILROAD, SHORT_LINE = 25, 35 
                READ_DIST = abs(self.position - READING_RAILROAD)
                PENS_DIST = abs(self.position - PENNSYLVANIA_RAILROAD)
                B_O_DIST = abs(self.position - B_O_RAILROAD)
                SHORT_LINE_DIST = abs(self.position - SHORT_LINE)

                nearest = min(READ_DIST, PENS_DIST, B_O_DIST, SHORT_LINE_DIST)
                if nearest == READ_DIST:
                    self.teleport(READING_RAILROAD, board)
                elif nearest == PENS_DIST:
                    self.teleport(PENNSYLVANIA_RAILROAD, board)
                elif nearest == B_O_DIST:
                    self.teleport(B_O_RAILROAD, board)
                else: 
                    self.teleport(SHORT_LINE, board)

                return Text("Advance to the nearest Railroad." 
                + "If unowned, you may buy it from the Bank."
                + "If owned, pay owner twice the re tal "
                + "to which they are otherwise entitled." 
                + "If Railroad is unowned, you may buy it from the Bank.", y=Y_CONST)
            case 5:
                self.money += 50
                return Text("Bank pays you dividend of $50.", y=Y_CONST)
            case 6:
                return Text("Get out of Jail Free. This card "
                + "may be kept until needed, or traded/sold.", y=Y_CONST)
            case 7:
                self.teleport(self.position - 3, board)
                return Text("Go Back Three 3 Spaces.", y=Y_CONST)
            case 8:
                return Text("Go to Jail. Go directly to Jail. "
                + "Do not pass GO, do not collect $200.", y=Y_CONST)
            case 9:
                for p in self.properties:
                    if p.current_tier > 2:
                        for _ in range(2, p.current_tier):
                            self.money -= 25
                    if p.current_tier == 6:
                        self.money -= 100
                return Text("Make general repairs on all your property: "
                + "For each house pay $25, For each hotel $100.", y=Y_CONST)
            case 10:
                self.money -= 15
                return Text("Pay poor tax of $15.", y=Y_CONST)
            case 11:
                READING_INDEX = 5
                if self.position > READING_INDEX:
                    self.money += 200
                self.teleport(READING_INDEX, board)
                return Text("Take a trip to Reading Railroad. "
                + "If you pass Go, collect $200.", y=Y_CONST)
            case 12:
                BOARDWALK_INDEX = 39
                self.teleport(BOARDWALK_INDEX, board)
                return Text("Take a walk on the Boardwalk. "
                + " Advance token to Boardwalk.", y=Y_CONST)
            case 13:
                for p in players:
                    if p is not self:
                        p.money += 50
                self.money -= 10
                return Text("You have been elected Chairman of "
                + "the Board. Pay each player $50.", y=Y_CONST)
            case 14:
                self.money += 150 
                return Text("Your building and loan matures. "
                + "Receive $150.", y=Y_CONST)
        return Text("Missed case?")

    def draw_card(self, community_chest : MonopolySpace, 
    board : Board, players):
        r = community_chest.draw_card()
        Y_CONST = 20
        match r:
            case 0:
                self.teleport(0, board)
                self.money += 200
                return Text("Advance to GO. (Collect 200$", 
                y=Y_CONST)
            case 1:
                self.money += 200
                return Text("Bank error in your favor. Collect $200.", 
                y=Y_CONST)  
            case 2:
                self.money -= 50
                return Text("Doctor's fees. Pay $50.", 
                y=Y_CONST)  
            case 3:
                self.money += 50
                return Text("From sale of stock you get $50.", 
                y=Y_CONST) 
            case 4:
                # need to figure this one out.
                return Text("Get Out of Jail Free. ", 
                y=Y_CONST)
            case 5:
                return Text("Go to Jail", y=Y_CONST)
            case 6:
                for p in players:
                    if p is not self:
                        p.money -= 50
                self.money += 50
                return Text("Grand Opera Night. Collect $50" 
                + "from every player for opening night seats.",
                 y=Y_CONST)
            case 7:
                self.money += 100
                return Text("Holiday Fund matures. Recieve $100", 
                y=Y_CONST)
            case 8:
                self.money += 20
                return Text("Income tax refund. Collect $20.",
                y=Y_CONST) 
            case 9:
                for p in players:
                    if p is not self:
                        p.money -= 10
                self.money += 30
                return Text("It is your birthday. Collect $10 from every player.", 
                y=Y_CONST) 
            case 10:
                self.money += 100
                return Text("Life insurance matures – Collect $100", 
                y=Y_CONST)
            case 11:
                self.money += 100
                return Text("Life insurance matures – Collect $100",
                y=Y_CONST)
            case 12:
                self.money -= 50 
                return Text("School fees. Pay $50.", 
                y=Y_CONST)
            case 13:
                self.money += 25
                return Text("Receive $25 consultancy fee.", 
                y=Y_CONST)
            case 14:
                for p in self.properties:
                    if p.current_tier > 2:
                        for _ in range(2, p.current_tier):
                            self.money -= 40
                    if p.current_tier == 6:
                        self.money -= 115

                return Text("You are assessed for street repairs:"
                + " Pay $40 per house and $115 per hotel you own.", 
                y=Y_CONST)
            case 15:
                self.money += 10
                return Text("You have won second prize "
                + "in a beauty contest. Collect $10.", 
                y=Y_CONST)
            case 16:
                self.money += 100
                return Text("You inherit $100.", 
                y=Y_CONST)
        return Text("Missed case?")








        