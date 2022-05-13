from random import random
from player import Player
import random
class CPU(Player):
    
    def __init__(self, color):
        super().__init__(color)

    def play(self, board, currentTurn): 

        self.move(random.randrange(0, 12))

        # Uses the info from the roll and the new player position to determine the space they landed on.
        landed_on_space = board.space[self.position]
        
        self.rectangle.x = landed_on_space.x
        self.rectangle.y = landed_on_space.y

        if landed_on_space.IS_BUYABLE and landed_on_space.owner == None:
            self.buy(landed_on_space)
            print("CPU bought " + landed_on_space.space_name)
        else: 
            print("CPU didn't buy property")


        if currentTurn == 3:
            currentTurn = 0
        else:
            currentTurn += 1

        return currentTurn