from board.space import Monopoly_Space

class Monopoly_Community_Chest(Monopoly_Space):
    
    def __init__(self, space_name):
        super().__init__(space_name)
        self.random = 0
        