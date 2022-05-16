from random import random
from board.board import Board
from board.space import Monopoly_Property
from player import Player
from text import Text
import random

class CPU(Player):
    
    def __init__(self, color):
        super().__init__(color)

    def play(self, board : Board, owner_rects, texts : list[Text]): 

        roll = random.randrange(2, 12)
        self.move(roll)

        # Uses the info from the roll and the new player position to determine the space they landed on.
        landed_on_space = board.space[self.position]
        texts.append(Text(f"CPU rolled a {roll} and landed on {landed_on_space.space_name}", 0, 20)) 
        
        self.rectangle.x = landed_on_space.x
        self.rectangle.y = landed_on_space.y


        if landed_on_space.IS_BUYABLE:
            if (landed_on_space.owner == None):
                self.buy(landed_on_space, owner_rects)
                texts.append(Text(f"CPU bought {landed_on_space.space_name}", 0, 40)) 
            elif (landed_on_space.owner == self):
                texts.append(Text("CPU owns the property.", 0, 20))
            else:   
                if (self.money - landed_on_space.get_current_price() < 0):
                    texts.append(Text("CPU can't afford to pay.", 0, 20))
                else: 
                    self.pay(landed_on_space.owner, landed_on_space)
                    texts.append(Text(f"CPU landed on Player {str(landed_on_space.owner.id)}'s property and paid them {landed_on_space.get_current_price()}", 0, 40))

        