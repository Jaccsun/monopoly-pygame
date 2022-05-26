from random import random
from board.board import Board
from board.space import *
from player import Player
from text import Text
import random

class CPU(Player):
    
    def __init__(self, color, image):
        super().__init__(color, image)

    def roll(self, game, r=None): 
        super().roll(game, cpu=True, r=r)

    def attempt_mortgage(self, cost):
        for p in self.properties:
            if type(p) is Monopoly_Ownable:
                p.mortgage()
            if self.money >= cost:
                return True
        return False

    def draw_card(self, community_chest: Monopoly_Community_Chest, board: Board, players):
        return super().draw_card(community_chest, board, players)