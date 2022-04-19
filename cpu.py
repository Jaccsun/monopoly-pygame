from player import Player
class CPU(Player):
    
    def __init__(self, color):
        super().__init__(color)

    def play(self, board): 

        cpu_roll = self.roll() 
        input("Player " + str(self.id) + " rolled a " + str(cpu_roll.value))

        self.move(cpu_roll)

        # Uses the info from the roll and the new player position to determine the space they landed on.
        landed_on_space = board.space[self.position]
        input("Player " + str(self.id) + " landed on " + landed_on_space.space_name)
        
        if landed_on_space.IS_BUYABLE and landed_on_space.owner == None:
            self.buy(landed_on_space)
            input("CPU bought " + landed_on_space.space_name)
        else: 
            print("CPU didn't buy property")