from xmlrpc.client import Boolean, boolean
import pygame
import os
from player import Player
from text import Text
import random

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

space_name: str

class Monopoly_Space:

    def __init__(self, space_name : str, x : int, y : int):
        self.space_name = space_name
        self.IS_BUYABLE = False
        self.x = x
        self.y = y

class Monopoly_Utility(Monopoly_Space):
    
    def __init__(self, space_name : str, x : int, y : int, p_image : pygame.Surface):
        super().__init__(space_name, x, y)

        self.owner = None
        self.current_tier = 0
        self.printed_price = 200
        self.mortgage_value = 75
        self.rent_tiers = (0, 1)
        self.IS_BUYABLE = True

        self.p_image = pygame.transform.scale(p_image, (50, 70))

    def increase_tier(self): 
        self.current_tier += 1

    def get_prompt(self):
        return Text("Would you like to buy this Utility?(y/n):", 0, 20)

    def get_current_price(self):
        return self.rent_tiers[self.current_tier]

class Monopoly_Railroad(Monopoly_Space):
    
    def __init__(self, space_name : str, x : int, y : int, p_image : pygame.Surface):
        super().__init__(space_name, x, y)

        self.owner = None
        self.current_tier = 0
        self.printed_price = 200
        self.mortgage_value = 100
        self.rent_tiers = (25, 50, 100, 200)
        self.IS_BUYABLE = True

        self.p_image = pygame.transform.scale(p_image, (50, 70))

    def get_prompt(self):
        return Text("Would you like to buy this Railroad? (y/n):", 0, 20)

    def get_current_price(self):
        return self.rent_tiers[self.current_tier]

    def increase_tier(self): 
        self.current_tier += 1

class Monopoly_Property(Monopoly_Space):

    def __init__(self, space_name : str, x : int, y : int, printed_price : int, mortgage_value : int, building_costs : int, rent_tiers : list[int], p_image : pygame.Surface):

        super().__init__(space_name, x, y)

        self.printed_price = printed_price
        self.mortgage_value = mortgage_value
        self.building_costs = building_costs
        self.rent_tiers = rent_tiers

        self.owner = None
        self.current_tier = 0
        self.IS_BUYABLE = True

        self.p_image = pygame.transform.scale(p_image, (50, 70))
    

    def get_current_price(self):
        return self.rent_tiers[self.current_tier]

    def increase_tier(self): 
        self.current_tier += 1

    def get_prompt(self):
        return Text("Would you like to buy this Property? (y/n):", 0, 20)

    def give_tier_description(self):
        tier_description = ""
        match self.current_tier:
            case 1:
                tier_description = "You don't have a monopoly, therefore you cannot build on this property."
            case 2:
                tier_description = "This property has no Houses."
            case 3:
                tier_description =  "This property has 1 House."
            case 4:
                tier_description =  "This property has 2 Houses."
            case 5:
                tier_description =  "This property has 3 Houses."
            case 5:
                tier_description = "This property has 4 Houses." 
            case 6:
                tier_description = "This property has a Hotel."
        return tier_description

class Monopoly_Community_Chest(Monopoly_Space):
    
    def __init__(self, space_name : str, x : int, y : int):
        super().__init__(space_name, x, y)

    def draw_card(self, player : Player, players : list[Player], board, y_pos=20):
        r = random.randint(0, 19)
        y = y_pos
        match r:
            case 0:
                player.teleport(0, board)
                player.money += 200
                return Text("Advance to GO. (Collect 200$", y=y)
            case 1:
                player.money += 200
                return Text("Bank error in your favor. Collect $200.", y=y)  
            case 3:
                player.money -= 50
                return Text("Doctor's fees. Pay $50.", y=y)  
            case 4:
                player.money += 50
                return Text("From sale of stock you get $50.", y=y) 
            case 5:
                # need to figure this one out.
                return Text("Get Out of Jail Free. ", y=y)
            case 7:
                return Text("Go to Jail", y=y)
            case 8:
                for p in players:
                    if p is not player:
                        p -= 50
                player.money += 50
                return Text("Grand Opera Night. Collect $50 from every player for opening night seats.", y=y)
            case 9:
                player.money += 100
                return Text("Holiday Fund matures. Recieve $100", y=y)
            case 10:
                player.money += 20
                return Text("Income tax refund. Collect $20.", y=y) 
            case 11:
                for p in players:
                    if p is not player:
                        p -= 10
                player.money += 10
                return Text("It is your birthday. Collect $10 from every player.", y=y) 
            case 12:
                player.money += 100
                return Text("Life insurance matures – Collect $100", y=y)
            case 13:
                player.money += 100
                return Text("Life insurance matures – Collect $100", y=y)
            case 14:
                player.money -= 50 
                return Text("School fees. Pay $50.", y=y)
            case 16:
                player.money += 25
                return Text("Receive $25 consultancy fee.", y=y)
            case 17:
                for p in player.properties:
                    if p.current_tier > 2:
                        for _ in range(2, p.current_tier):
                            player.money -= 40
                    if p.current_tier == 6:
                        player.money -= 115

                return Text("You are assessed for street repairs: Pay $40 per house and $115 per hotel you own.", y=y)
            case 18:
                player.money += 10
                return Text("You have won second prize in a beauty contest. Collect $10.", y=y)
            case 19:
                player.money += 100
                return Text("You inherit $100.", y=y)
        return Text("Broken.", y=y)

class Monopoly_Chance(Monopoly_Space):
    
    def __init__(self, space_name : str, x : int, y : int):
        super().__init__(space_name, x, y)
        self.chance = 0

    def draw_card(self, player : Player, players : list[Player], board, y_pos=20):
        r = random.randint(0, 14)
        y = y_pos
        match r:
            case 0:
                player.teleport(0, board)
                player.money += 200
                return Text("Advance to \"Go\". (Collect $200)", y=y)
            case 1:
                ILLINOIS_INDEX = 24
                if player.position > ILLINOIS_INDEX:
                    player.money += 200
                player.teleport(ILLINOIS_INDEX, board)
                return Text("Advance to Illinois Ave. If you pass Go, collect $200.", y=y)
            case 2:
                ST_CHARLES_INDEX = 24
                if player.position > ST_CHARLES_INDEX:
                    player.money += 200
                player.teleport(ST_CHARLES_INDEX, board)
                return Text("Advance to St. Charles Place. If you pass Go, collect $200.", y=y)
            case 3:
                ELECTRIC_COMPANY_INDEX = 12
                WATER_WORKS_INDEX = 28
                electric_distance = abs(player.position - ELECTRIC_COMPANY_INDEX)
                water_distance = abs(player.position - WATER_WORKS_INDEX)
                
                if (electric_distance > water_distance):
                    player.teleport(ELECTRIC_COMPANY_INDEX, board)
                else:
                    player.teleport(WATER_WORKS_INDEX, board)
                    
                return Text("Advance token to the nearest Utility. If unowned, you may buy it from the Bank." 
                + "If owned, throw dice and pay owner a total 10 (ten) times the amount thrown.", y=y)
            case 4:
                READING_RAILROAD, PENNSYLVANIA_RAILROAD, B_O_RAILROAD, SHORT_LINE = 5, 15, 25, 35 
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

                return Text("Advance to the nearest Railroad. If unowned, you may buy it from the Bank."
                + "If owned, pay owner twice the re tal to which they are otherwise entitled." 
                + "If Railroad is unowned, you may buy it from the Bank.", y=y)
            case 5:
                player.money += 50
                return Text("Bank pays you dividend of $50.", y=y)
            case 6:
                return Text("Get out of Jail Free. This card may be kept until needed, or traded/sold.", y=y)
            case 7:
                player.teleport(player.position - 3, board)
                return Text("Go Back Three 3 Spaces.", y=y)
            case 8:
                # NEED
                return Text("Go to Jail. Go directly to Jail. Do not pass GO, do not collect $200.", y=y)
            case 9:
                for p in player.properties:
                    if p.current_tier > 2:
                        for _ in range(2, p.current_tier):
                            player.money -= 25
                    if p.current_tier == 6:
                        player.money -= 100
                return Text("Make general repairs on all your property: For each house pay $25, For each hotel $100.", y=y)
            case 10:
                player.money -= 15
                return Text("Pay poor tax of $15.", y=y)
            case 11:
                READING_INDEX = 5
                if player.position > READING_INDEX:
                    player.money += 200
                player.teleport(READING_INDEX, board)
                return Text("Take a trip to Reading Railroad. If you pass Go, collect $200.", y=y)
            case 12:
                BOARDWALK_INDEX = 39
                player.teleport(BOARDWALK_INDEX, board)
                return Text("Take a walk on the Boardwalk. Advance token to Boardwalk.", y=y)
            case 13:
                for p in players:
                    if p is not player:
                        p += 50
                player.money -= 10
                return Text("You have been elected Chairman of the Board. Pay each player $50.", y=y)
            case 14:
                player.money += 150 
                return Text("Your building and loan matures. Receive $150.", y=y)
        return Text("Broken.", y=y)