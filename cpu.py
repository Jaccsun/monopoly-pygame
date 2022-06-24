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

    # Cpu evaluation of the quality of a trade. 
    # Based on amount of points given.
    def evaluate_trade(self, game):

        # Points that indicate quality of trade.
        points = 0 

        cpu_prop = game.property_exchange[1]
        player_prop = game.property_exchange[0]

        cpu_money = game.money_exchange[1]
        player_money = game.money_exchange[0]

        cpu_eval = game.get_total_value(1)
        player_eval = game.get_total_value(0)
        # Value evaluation.
        if cpu_eval == 0:
            points += 10
        if player_eval > cpu_eval:
            points += 1
        if player_eval >= cpu_eval + 200:
            points += 1
        if player_eval >= cpu_eval + 400:
            points += 1
        m_count = {}
        # Monopoly completion evaluation
        for p in game.trade_list[1].properties:
            if p.card.image_str not in m_count:
               m_count[p.card.image_str] = 0
            m_count[p.card.image_str] = m_count.get(p.card.image_str) + 1
        m_count_2 = {}
        for p in player_prop:
            if p.card.image_str not in m_count_2:
               m_count_2[p.card.image_str] = 0
            m_count_2[p.card.image_str] =  m_count_2.get(p.card.image_str) + 1
        for key in list(m_count):
            if m_count_2.get(key) is not None:
                if m_count.get(key) + m_count_2.get(key) == 3:
                    points += 2
                elif (m_count.get(key) + m_count_2.get(key) == 2
                    and key == "BROWN_P" or key == "BLUE_P"):
                        points += 2      
        if points >= 2:
            return True
        else:
            return False

                    


        
        
