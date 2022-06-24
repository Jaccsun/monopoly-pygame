import pygame
import os
import random
from text import Text
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
    def __init__(self, card_image : pygame.Surface, 
    card_image_str : str):

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

    def increase_tier(self):
        self.current_tier += 1
    
    def add_property_text(self, texts, buttons, player):
        texts.append(Text(f"{self.space_name}:", 20, 500))
        if self.current_tier > -1:
            buttons.append(Button("Mortgage", 20, 550, 80, 40))
        else:
            buttons.append(Button("Lift Mortgage", 20, 550, 80, 40))

    def get_current_price(self):
        return self.rent_tiers[self.current_tier]

class Monopoly_Utility(Monopoly_Ownable):
    
    def __init__(self, space_name : str, x : int, y : int, 
    p_image : pygame.Surface, p_image_str : str):
        super().__init__(space_name, x, y, p_image, p_image_str)
        self.printed_price = 200
        self.mortgage_value = 75
        self.rent_tiers = (4, 10)

    def get_prompt(self):
        return Text("Would you like to buy this Utility?(y/n):", 0, 20)


class Monopoly_Railroad(Monopoly_Ownable):
    
    def __init__(self, space_name : str, x : int, y : int, 
    p_image : pygame.Surface, p_image_str : str):

        super().__init__(space_name, x, y, p_image, p_image_str)

        self.printed_price = 200
        self.mortgage_value = 100
        self.rent_tiers = (25, 50, 100, 200)

    def get_prompt(self):
        return Text("Would you like to buy this Railroad? (y/n):", 0, 20)


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
    

class Monopoly_Community_Chest(Monopoly_Space):
    
    def __init__(self, space_name : str, x : int, y : int):
        super().__init__(space_name, x, y)

    def draw_card(self):
        r = random.randint(0, 16)
        return r

class Monopoly_Chance(Monopoly_Space):
    
    def __init__(self, space_name : str, x : int, y : int):
        super().__init__(space_name, x, y)
        self.chance = 0

    def draw_card(self):
        r = random.randint(0, 14)
        return r