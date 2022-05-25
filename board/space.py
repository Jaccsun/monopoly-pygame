from re import X
from tokenize import String
from xmlrpc.client import Boolean, boolean
import pygame
import os
from player import Player
from text import Text
import random
from button import Button

BROWN_P = pygame.image.load(os.path.join('Assets', 'brown.jpg'))
LIGHT_BLUE_P = pygame.image.load(os.path.join('Assets', 'l_blue.jpg'))
PINK_P = pygame.image.load(os.path.join('Assets', 'pink.jpg'))
ORANGE_P = pygame.image.load(os.path.join('Assets', 'orange.jpg'))
RED_P = pygame.image.load(os.path.join('Assets', 'red.jpg'))
YELLOW_P = pygame.image.load(os.path.join('Assets', 'yellow.jpg'))
GREEN_P = pygame.image.load(os.path.join('Assets', 'green.jpg'))
BLUE_P = pygame.image.load(os.path.join('Assets', 'blue.jpg'))

WHITE_P = pygame.image.load(os.path.join('Assets', 'white.jpg'))
BLACK_P = pygame.image.load(os.path.join('Assets', 'black.jpg'))

HOUSE_SCALE, HOTEL_SCALE = (11, 11), (15, 15)
HOUSE_IMAGE = pygame.image.load(os.path.join('Assets', 
'house.jpg'))
HOTEL_IMAGE = pygame.image.load(os.path.join('Assets', 
'hotel.jpg'))
HOUSE = pygame.transform.scale((HOUSE_IMAGE), HOUSE_SCALE)
HOTEL = pygame.transform.scale((HOTEL_IMAGE), HOTEL_SCALE)

BOTTOM_Y = 692
LEFT_X = 150
TOP_Y = 160
RIGHT_X = 696

space_name: str

class Monopoly_Space:

    def __init__(self, space_name : str, x : int, y : int):
        self.space_name = space_name
        self.IS_BUYABLE = False
        self.x = x
        self.y = y

class Monopoly_Card:
    def __init__(self, card_image, card_image_str):

        self.image = pygame.transform.scale(card_image, (50, 70))
        self.image_str = card_image_str
        self.rect = self.image.get_rect()

    def draw(self, WIN):
        WIN.blit(self.image, self.rect)

class Monopoly_Ownable(Monopoly_Space):
    def __init__(self, space_name : str, x : int, y : int, 
    card_image : pygame.Surface, card_image_str : str):
        super().__init__(space_name, x, y)

        self.owner = None
        self.current_tier = 0
        self.IS_BUYABLE = True
        self.card = Monopoly_Card(card_image, card_image_str)
        self.owner_rect = None
        
        # Overrided
        self.mortgage_value = None

    def mortgage(self, player):
        self.current_tier = -1
        player.money += self.mortgage_value

    def unmortgage(self, player):
        if player.money - self.mortgage_value > 0:
            self.current_tier == 0
            player.money -= self.mortgage_value

    def add_property_text(self, texts, buttons, player):
        texts.append(Text(f"{self.space_name}:", 20, 500))
        if self.current_tier > -1:
            buttons.append(Button("Mortgage", 20, 550, 80, 40))
        else:
            buttons.append(Button("Lift Mortgage", 20, 550, 80, 40))

class Monopoly_Utility(Monopoly_Ownable):
    
    def __init__(self, space_name : str, x : int, y : int, 
    p_image : pygame.Surface, p_image_str : str):
        super().__init__(space_name, x, y, p_image, p_image_str)
        self.printed_price = 200
        self.mortgage_value = 75
        self.rent_tiers = (4, 10)

    def increase_tier(self): 
        self.current_tier += 1

    def get_prompt(self):
        return Text("Would you like to buy this Utility?(y/n):", 0, 20)

    def get_current_price(self):
        return self.rent_tiers[self.current_tier]

    def unmortgage(self, player):
        if player.money - self.mortgage_value > 0:
            count = 0
            for p in player.properties:
                if type(p) is Monopoly_Utility:
                    count += 1
            if count == 2:
                self.current_tier = 1
            else:
                self.current_tier = 0
            player.money -= self.mortgage_value

class Monopoly_Railroad(Monopoly_Ownable):
    
    def __init__(self, space_name : str, x : int, y : int, 
    p_image : pygame.Surface, p_image_str : str):

        super().__init__(space_name, x, y, p_image, p_image_str)

        self.printed_price = 200
        self.mortgage_value = 100
        self.rent_tiers = (25, 50, 100, 200)

    def get_prompt(self):
        return Text("Would you like to buy this Railroad? (y/n):", 0, 20)

    def get_current_price(self):
        return self.rent_tiers[self.current_tier]

    def increase_tier(self): 
        self.current_tier += 1

    def unmortgage(self, player):
        if player.money - self.mortgage_value > 0:
            count = 0
            for p in player.properties:
                if type(p) is Monopoly_Utility:
                    count += 1
            if count == 1:
                self.current_tier = 0
            elif count == 2:
                self.current_tier = 1
            elif count == 3:
                self.current_tier = 2
            elif count == 4:
                self.current_tier = 3
            player.money -= self.mortgage_value

class Monopoly_Property(Monopoly_Ownable):

    def __init__(self, space_name : str, x : int
    , y : int, printed_price : int, mortgage_value : int, 
    building_costs : int, rent_tiers : list[int],
     p_image : pygame.Surface, p_image_str : str):

        super().__init__(space_name, x, y, p_image, p_image_str)

        self.printed_price = printed_price
        self.mortgage_value = mortgage_value
        self.rent_tiers = rent_tiers

        self.building_costs = building_costs

    def get_current_price(self):
        return self.rent_tiers[self.current_tier]

    def increase_tier(self): 
        self.current_tier += 1

    def get_prompt(self):
        return Text("Would you like to buy this Property? (y/n):", 0, 20)

    def is_monopoly(self, player):
        color, count = self.card.image_str, 0
        for property in player.properties:
            if property.card.image_str == color:
                count += 1
        if count == 3 or (count == 2 and 
        (color == "BROWN_P" or color == "BLUE_P")):
            return True
        return False

    def add_property_text(self, texts, buttons, player):
        if self.current_tier == -1:
            buttons.append(Button("Lift Mortgage", 20, 550, 80, 40))
        else:
            if self.current_tier == 0 or self.current_tier == 1:
                buttons.append(Button("Mortgage", 20, 550, 80, 40))
            if self.is_monopoly(player):
                buttons.extend([Button("Build", 20, 610, 80, 40), 
                Button("Sell", 20, 670, 80, 40)])
                if self.current_tier == 6:
                    texts.append(Text(f"1 hotel", 300, 500))
                else:
                    texts.append(Text(f"{self.current_tier - 1} houses", 300, 500))
        texts.append(Text(f"{self.space_name}:", 20, 500)) 

    def draw_houses(self, WIN):
        house, hotel = HOUSE, HOTEL
        add_x, add_y = 0, 0

        if self.x == LEFT_X:
            add_x += 65
        elif self.x == RIGHT_X:
            add_x -= 20 
        if self.y == BOTTOM_Y:
            add_y -= 20
        elif self.y == TOP_Y:
            add_y += 53

        if self.x == LEFT_X or self.x == RIGHT_X:
            house = pygame.transform.rotate(HOUSE, 90)
            hotel = pygame.transform.rotate(HOTEL, 90)
        
        if self.current_tier == 6:
            if self.y == BOTTOM_Y or self.y == TOP_Y:  
                add_y -= 1 
                add_x += 8
            else:
                add_x += -3
                add_y += 9
            WIN.blit(hotel, (self.x + add_x, self.y + add_y))
        else:
            increment = 0
            for _ in range(1, self.current_tier):
                if self.y == BOTTOM_Y or self.y == TOP_Y:
                    add_x = -7
                    WIN.blit(house, (self.x + add_x + increment, self.y + add_y))
                else:
                    add_y = -2
                    WIN.blit(house, (self.x + add_x, self.y + add_y + increment))
                increment += 12
    def unmortgage(self, player):
        if player.money - self.mortgage_value > 0:
            if self.is_monopoly(player):
                self.current_tier = 1
            else:
                self.current_tier = 0
            player.money -= self.mortgage_value

class Monopoly_Community_Chest(Monopoly_Space):
    
    def __init__(self, space_name : str, x : int, y : int):
        super().__init__(space_name, x, y)

    def draw_card(self, player : Player, players : list[Player], board):
        r = random.randint(0, 19)
        Y_CONST = 40
        match r:
            case 0:
                player.teleport(0, board)
                player.money += 200
                return Text("Advance to GO. (Collect 200$", 
                y=Y_CONST)
            case 1:
                player.money += 200
                return Text("Bank error in your favor. Collect $200.", 
                y=Y_CONST)  
            case 3:
                player.money -= 50
                return Text("Doctor's fees. Pay $50.", 
                y=Y_CONST)  
            case 4:
                player.money += 50
                return Text("From sale of stock you get $50.", 
                y=Y_CONST) 
            case 5:
                # need to figure this one out.
                return Text("Get Out of Jail Free. ", 
                y=Y_CONST)
            case 7:
                return Text("Go to Jail", y=Y_CONST)
            case 8:
                for p in players:
                    if p is not player:
                        p.money -= 50
                player.money += 50
                return Text("Grand Opera Night. Collect $50" 
                + "from every player for opening night seats.",
                 y=Y_CONST)
            case 9:
                player.money += 100
                return Text("Holiday Fund matures. Recieve $100", 
                y=Y_CONST)
            case 10:
                player.money += 20
                return Text("Income tax refund. Collect $20.",
                y=Y_CONST) 
            case 11:
                for p in players:
                    if p is not player:
                        p.money -= 10
                player.money += 10
                return Text("It is your birthday. Collect $10 from every player.", 
                y=Y_CONST) 
            case 12:
                player.money += 100
                return Text("Life insurance matures – Collect $100", 
                y=Y_CONST)
            case 13:
                player.money += 100
                return Text("Life insurance matures – Collect $100",
                y=Y_CONST)
            case 14:
                player.money -= 50 
                return Text("School fees. Pay $50.", 
                y=Y_CONST)
            case 16:
                player.money += 25
                return Text("Receive $25 consultancy fee.", 
                y=Y_CONST)
            case 17:
                for p in player.properties:
                    if p.current_tier > 2:
                        for _ in range(2, p.current_tier):
                            player.money -= 40
                    if p.current_tier == 6:
                        player.money -= 115

                return Text("You are assessed for street repairs:"
                + " Pay $40 per house and $115 per hotel you own.", 
                y=Y_CONST)
            case 18:
                player.money += 10
                return Text("You have won second prize "
                + "in a beauty contest. Collect $10.", 
                y=Y_CONST)
            case 19:
                player.money += 100
                return Text("You inherit $100.", 
                y=Y_CONST)
        return Text("Broken.", y=Y_CONST)

class Monopoly_Chance(Monopoly_Space):
    
    def __init__(self, space_name : str, x : int, y : int):
        super().__init__(space_name, x, y)
        self.chance = 0

    def draw_card(self, player : Player, players : list[Player], board, ):
        r = random.randint(0, 14)
        Y_CONST = 40
        match r:
            case 0:
                player.teleport(0, board)
                player.money += 200
                return Text("Advance to \"Go\". (Collect $200)", y=Y_CONST)
            case 1:
                ILLINOIS_INDEX = 24
                if player.position > ILLINOIS_INDEX:
                    player.money += 200
                player.teleport(ILLINOIS_INDEX, board)
                return Text("Advance to Illinois Ave. If you pass Go, collect $200.", y=Y_CONST)
            case 2:
                ST_CHARLES_INDEX = 24
                if player.position > ST_CHARLES_INDEX:
                    player.money += 200
                player.teleport(ST_CHARLES_INDEX, board)
                return Text("Advance to St. Charles Place. If you pass Go, collect $200.", y=Y_CONST)
            case 3:
                ELECTRIC_COMPANY_INDEX = 12
                WATER_WORKS_INDEX = 28
                electric_distance = abs(player.position - ELECTRIC_COMPANY_INDEX)
                water_distance = abs(player.position - WATER_WORKS_INDEX)
                
                if (electric_distance > water_distance):
                    player.teleport(ELECTRIC_COMPANY_INDEX, board)
                else:
                    player.teleport(WATER_WORKS_INDEX, board)
                    
                return Text("Advance token to the nearest Utility. "
                + "If unowned, you may buy it from the Bank." 
                + "If owned, throw dice and pay owner a total "
                + "10 (ten) times the amount thrown.", y=Y_CONST)
            case 4:
                READING_RAILROAD, PENNSYLVANIA_RAILROAD = 5, 15
                B_O_RAILROAD, SHORT_LINE = 25, 35 
                READ_DIST = abs(player.position - READING_RAILROAD)
                PENS_DIST = abs(player.position - PENNSYLVANIA_RAILROAD)
                B_O_DIST = abs(player.position - B_O_RAILROAD)
                SHORT_LINE_DIST = abs(player.position - SHORT_LINE)

                nearest = min(READ_DIST, PENS_DIST, B_O_DIST, SHORT_LINE_DIST)
                if nearest == READ_DIST:
                    player.teleport(READING_RAILROAD, board)
                elif nearest == PENS_DIST:
                    player.teleport(PENNSYLVANIA_RAILROAD, board)
                elif nearest == B_O_DIST:
                    player.teleport(B_O_RAILROAD, board)
                else: 
                    player.teleport(SHORT_LINE, board)

                return Text("Advance to the nearest Railroad." 
                + "If unowned, you may buy it from the Bank."
                + "If owned, pay owner twice the re tal "
                + "to which they are otherwise entitled." 
                + "If Railroad is unowned, you may buy it from the Bank.", y=Y_CONST)
            case 5:
                player.money += 50
                return Text("Bank pays you dividend of $50.", y=Y_CONST)
            case 6:
                return Text("Get out of Jail Free. This card "
                + "may be kept until needed, or traded/sold.", y=Y_CONST)
            case 7:
                player.teleport(player.position - 3, board)
                return Text("Go Back Three 3 Spaces.", y=Y_CONST)
            case 8:
                # NEED
                return Text("Go to Jail. Go directly to Jail. "
                + "Do not pass GO, do not collect $200.", y=Y_CONST)
            case 9:
                for p in player.properties:
                    if p.current_tier > 2:
                        for _ in range(2, p.current_tier):
                            player.money -= 25
                    if p.current_tier == 6:
                        player.money -= 100
                return Text("Make general repairs on all your property: "
                + "For each house pay $25, For each hotel $100.", y=Y_CONST)
            case 10:
                player.money -= 15
                return Text("Pay poor tax of $15.", y=Y_CONST)
            case 11:
                READING_INDEX = 5
                if player.position > READING_INDEX:
                    player.money += 200
                player.teleport(READING_INDEX, board)
                return Text("Take a trip to Reading Railroad. "
                + "If you pass Go, collect $200.", y=Y_CONST)
            case 12:
                BOARDWALK_INDEX = 39
                player.teleport(BOARDWALK_INDEX, board)
                return Text("Take a walk on the Boardwalk. "
                + " Advance token to Boardwalk.", y=Y_CONST)
            case 13:
                for p in players:
                    if p is not player:
                        p.money += 50
                player.money -= 10
                return Text("You have been elected Chairman of "
                + "the Board. Pay each player $50.", y=Y_CONST)
            case 14:
                player.money += 150 
                return Text("Your building and loan matures. "
                + "Receive $150.", y=Y_CONST)
        return Text("Broken.", y=Y_CONST)