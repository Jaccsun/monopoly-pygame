import itertools
from roll import Roll
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
    def __init__(self, color):
        self.id = Player.id()
        self.position = 0
        self.money = 1500
        self.properties = []
        self.railroads_owned = 0
        self.color = color
        self.rectangle = pygame.Rect(690, 690, 35, 35) 

    def roll(self):
        roll = Roll(self)
        return roll

    def move(self, roll):
        if(self.position + roll.value >= 40):
            self.position = (self.position + roll.value) - 40
        else: 
            self.position += roll.value

    def buy(self, landed_on_space):
        self.money -= landed_on_space.printed_price
        self.properties.append(landed_on_space)
        landed_on_space.owner = self
        landed_on_space.increase_tier()

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








        