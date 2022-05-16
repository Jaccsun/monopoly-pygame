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

    def draw_card(self, player : Player):
        r = random.randint(0, 12)
        y = 20
        match r:
            case 0:
                player.position = 0
                return Text("Advance to GO. (Collect 200$", y=y)
            case 1:
                return Text("Bank error in your favor. Collect $200.", y=y)  
            case 3:
                return Text("Doctor's fees. Pay $50.", y=y)  
            case 4:
                return Text("From sale of stock you get $50.", y=y) 
            case 5:
                return Text("Get Out of Jail Free. ", y=y)
            case 6:
                return Text("Go to Jail", y=y)
            case 7:
                return Text("Go to Jail", y=y)
            case 8:
                return Text("Grand Opera Night. Collect $50 from every player for opening night seats.", y=y)
            case 9:
                return Text("Holiday Fund matures. Recieve $100", y=y)
            case 10:
                return Text("Income tax refund. Collect $20.", y=y) 
            case 11:
                return Text("It is your birthday. Collect $10 from every player.", y=y) 
            case 12:
                return Text("Life insurance matures – Collect $100", y=y)
            case 13:
                return Text("Life insurance matures – Collect $100", y=y)
            case 14:
                return Text("School fees. Pay $50.", y=y)
            case 16:
                return Text("Receive $25 consultancy fee.", y=y)
            case 17:
                return Text("You are assessed for street repairs: Pay $40 per house and $115 per hotel you own.", y=y)
            case 18:
                return Text("You have won second prize in a beauty contest. Collect $10.", y=y)
            case 19:
                return Text("You inherit $100.", y=y)

class Monopoly_Chance(Monopoly_Space):
    
    def __init__(self, space_name : str, x : int, y : int):
        super().__init__(space_name, x, y)
        self.chance = 0

    def draw_card(self):
        print("test")


