import pygame

propertyTypeList = [1, 3 ,2]

class Monopoly_Space:

    def __init__(self, name : str, type : str, 
    location : tuple, isOwnable = False, 
    cardImage = None, printedPrice = None, 
    mortgageValue = None, buildingCosts = None, 
    rentTiers = None):
        self.name = name
        self.type = type
        self.x = location[0]
        self.y = location[1]
        self.isOwnable = isOwnable

        if isOwnable:
            self.cardImage = pygame.transform.scale(cardImage, (50, 70))
            self.cardImageRect = self.image.get_rect()

            self.owner = None
            self.ownerRect = None
            self.mortgageValue = None
            self.currentTier = 0

            self.printed_price = 200
            self.mortgage_value = 75
            self.rent_tiers
            self.printedPrice = printedPrice
            self.mortgageValue = mortgageValue
            self.rentTiers = rentTiers
        if type =="property":
            self.buildingCosts = buildingCosts
