import itertools
from typing import Tuple
import pygame

# Color constants.
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)

class Player:

    id = itertools.count(start = 1).__next__
    
    def __init__(self, color : Tuple):
        self.id = Player.id()
        self.position = 0
        self.money = 1500
        self.properties = []
        self.monopolies = []
        self.railroads_owned = 0
        self.color = color
        self.rectangle = pygame.Rect(690, 690, 35, 35) 

    def move(self, roll : int, board):
        if(self.position + roll >= 40):
            self.position = (self.position + roll) - 40
        else: 
            self.position += roll

        landed_on_space = board.space[self.position]
        
        self.rectangle.x = landed_on_space.x
        self.rectangle.y = landed_on_space.y 

        return landed_on_space

    def teleport(self, space, board):
        self.position = space
        s = board.space[self.position]
        self.rectangle.x = s.x
        self.rectangle.y = s.y 


    def buy(self, landed_on_space):

        self.money -= landed_on_space.printed_price
        self.properties.append(landed_on_space)
        landed_on_space.owner = self
        landed_on_space.increase_tier()
        
        BOTTOM_Y = 692
        LEFT_X = 150
        RIGHT_X = 696

        x = landed_on_space.x
        y = landed_on_space.y

        if (landed_on_space.x == LEFT_X):
            x += 80
            y += 11
        elif (landed_on_space.x == RIGHT_X):
            x -= 34
            y += 10
        elif (landed_on_space.y == BOTTOM_Y):
            y -= 30
            x += 15
        else:
            x += 12
            y += 70
        landed_on_space.owner_rect = [pygame.Rect(x, y, 10, 10), self.color]
    def pay(self, player, landed_on_space):
        self.money -= landed_on_space.get_current_price()
        player.money += landed_on_space.get_current_price()

    def print_owned_properties(self):
        for owned_property in  self.properties:
            print(str(self.properties.index(owned_property) + 1) + " " + owned_property.space_name)

    def draw(self, WIN): 
        pygame.draw.rect(WIN, self.color, self.rectangle)

def draw_all_players(players : list, WIN):
    for player in players:
        player.draw(WIN)








        