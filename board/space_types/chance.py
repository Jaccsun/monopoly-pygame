from board.space import Monopoly_Space

class Monopoly_Chance(Monopoly_Space):
    
    def __init__(self, space_name):
        super().__init__(space_name)
        self.chance = 0

    