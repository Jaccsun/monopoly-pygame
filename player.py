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

    def roll(self):
        roll = Roll(self)
        return roll

    def move(self, roll):
        if(self.position + roll.value >= 40):
            self.position = (self.position + roll.value) - 40
        else: 
            self.position += roll.value


        