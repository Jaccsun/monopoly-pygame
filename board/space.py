from turtle import isdown
import pygame

class MonopolySpace:

    name : str
    type : str
    x : int
    y : int
    isOwnable : bool
    cardImage : pygame.Surface
    cardImageRect : pygame.rect.Rect
    owner : str

    def __init__(self, name : str, type : str, 
    location : tuple, isOwnable : bool = False, 
    cardImage : pygame.Surface = None, printedPrice : int = None, 
    mortgageValue : int = None, buildingCosts : int = None, 
    rentTiers : list[int]= None, color : str =None):
        self.name = name
        self.type = type
        self.x = location[0]
        self.y = location[1]
        self.isOwnable = isOwnable

        if isOwnable:
            self.owner = 'none'
            self.cardImage = pygame.transform.scale(cardImage, (50, 70))
            self.cardImageRect = self.cardImage.get_rect()

            # self.owner = None
            self.ownerRect = None
            self.currentTier = 0

            self.printedPrice = printedPrice
            self.mortgageValue = mortgageValue
            self.rentTiers = rentTiers
            self.printedPrice = printedPrice
            self.mortgageValue = mortgageValue
            self.rentTiers = rentTiers
        if type =="property":
            self.color = color
            self.buildingCosts = buildingCosts

    def get_current_price(self):
        if self.isOwnable:
            return self.rentTiers[self.currentTier]
        else: 
            raise TypeError("Space isn't ownable.")

