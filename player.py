import itertools
import imp
from roll import Roll
class Player:
    id = itertools.count(start = 1).__next__
    def __init__(self):
        self.id = Player.id()
        self.position = 0
        self.money = 1500
        self.properties = []
        self.railroads_owned = 0

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
            
    def print_owned_properties(self):
        for owned_property in  self.properties:
            print(str(self.properties.index(owned_property) + 1) + " " + owned_property.space_name)





        