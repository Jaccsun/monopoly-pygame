import random 
class Roll:
    def __init__(self, Player):
        self.value = random.randint(2, 12)
        self.player = Player
        

