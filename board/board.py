from board.space import MonopolySpace
import pygame
import os 

BROWN_P = pygame.image.load(os.path.join('Assets', 'brown.jpg'))
LIGHT_BLUE_P = pygame.image.load(os.path.join('Assets', 'l_blue.jpg'))
PINK_P = pygame.image.load(os.path.join('Assets', 'pink.jpg'))
ORANGE_P = pygame.image.load(os.path.join('Assets', 'orange.jpg'))
RED_P = pygame.image.load(os.path.join('Assets', 'red.jpg'))
YELLOW_P = pygame.image.load(os.path.join('Assets', 'yellow.jpg'))
GREEN_P = pygame.image.load(os.path.join('Assets', 'green.jpg'))
BLUE_P = pygame.image.load(os.path.join('Assets', 'blue.jpg'))

WHITE_P = pygame.image.load(os.path.join('Assets', 'white.jpg'))
BLACK_P = pygame.image.load(os.path.join('Assets', 'black.jpg'))


class Board:
    def __init__(self):
        
        BOTTOM_Y = 692
        LEFT_X = 150
        TOP_Y = 160
        RIGHT_X = 696

        self.IMAGE = pygame.image.load(os.path.join('Assets', 'board.jpg'))

        self.show = True

        # SPECIAL JAIL SPACE
        self.JAIL = MonopolySpace(
            name = "Jail",
            type = 'jail', 
            location = (185, 685),
            isOwnable = False
        )

        # SPACE 0
        GO = MonopolySpace(
            name = "GO", 
            type = 'other', 
            location = (690, 690),
            isOwnable = False
        )


        # SPACE 1
        MEDITERRANEAN_AVENUE = MonopolySpace(
            name = "Mediterranean Avenue (Brown)", 
            type = 'property',
            location = (630, BOTTOM_Y),
            isOwnable = True,
            cardImage = BROWN_P,
            printedPrice = 60,
            mortgageValue = 30,
            buildingCosts = 50,
            rentTiers = (2, 4, 10, 30, 90, 160, 250),
            color = 'brown'
        )

        # SPACE 2
        COMMUNITY_CHEST_1 = MonopolySpace(
            name = "Community Chest", 
            type = 'comChest', 
            location = (580, BOTTOM_Y),
            isOwnable = False
        )

        # SPACE 3
        BALTIC_AVENUE = MonopolySpace(
            name = "Baltic Avenue (Brown)",  
            type = 'property',
            location = (530, BOTTOM_Y),
            isOwnable = True,
            cardImage = BROWN_P,
            printedPrice = 60,
            mortgageValue = 30,
            buildingCosts = 50,
            rentTiers = (4, 8, 20, 60, 180, 320, 450),
            color = 'brown'
        )

        # SPACE 4
        INCOME_TAX = MonopolySpace(
            name = "Income Tax", 
            type = 'incomeTax', 
            location = (482, BOTTOM_Y),
            isOwnable = False
        )

        # SPACE 5
        READING_RAILROAD = MonopolySpace(
            name = "Reading Railroad", 
            type = 'railroad', 
            location = (432, BOTTOM_Y), 
            isOwnable = True,
            cardImage = BLACK_P,
        )

        # SPACE 6
        ORIENTAL_AVENUE = MonopolySpace(
            name = "Oriental Avenue (Light Blue)", 
            type = 'property',
            location = (383, BOTTOM_Y),
            isOwnable = True,
            cardImage = LIGHT_BLUE_P,
            printedPrice = 100,
            mortgageValue = 50,
            buildingCosts = 50,
            rentTiers=(6, 12, 30, 90, 270, 400, 550),
            color = 'lightblue'
        )

        # SPACE 7
        CHANCE_1 = MonopolySpace(
            name = "Chance", 
            type = 'chance', 
            location = (332, BOTTOM_Y),
            isOwnable = False
        )

        # SPACE 8
        VERMONT_AVENUE = MonopolySpace(
            name = "Vermont Avenue (Light Blue)", 
            type = 'property',
            location = (285, BOTTOM_Y),
            isOwnable =  True,
            cardImage = LIGHT_BLUE_P,
            printedPrice = 100,
            mortgageValue = 50,
            buildingCosts = 50,
            rentTiers=(6, 12, 30, 90, 270, 400, 550),
            color = 'lightblue'
        )

        # SPACE 9
        CONNECTICUT_AVENUE = MonopolySpace(
            name = "Connecticut Avenue (Light Blue)", 
            type = 'property',
            location = (235, BOTTOM_Y),
            isOwnable = True,
            cardImage = LIGHT_BLUE_P,
            printedPrice = 120,
            mortgageValue = 60,
            buildingCosts = 50,
            rentTiers = (8, 16, 40, 100, 300, 450, 600),
            color = 'lightblue'
        )

        # SPACE 10
        JUST_VISITING = MonopolySpace(
            name = "Just Visting", 
            type = 'other', 
            location = (149, 712),
            isOwnable = False
        )

        # SPACE 11
        ST_CHARLES_PLACE = MonopolySpace(
            name = "St Charles Place (Pink)", 
            type = 'property',
            location = (LEFT_X, 626),
            isOwnable = True,
            cardImage = PINK_P,
            printedPrice = 140,
            mortgageValue = 70,
            buildingCosts = 100,
            rentTiers = (10, 20, 50, 150, 450, 625, 750),
            color = 'lightblue'
        )

        # SPACE 12
        ELECTRIC_COMPANY = MonopolySpace(
            name = "Electric Company", 
            type = 'property',
            location = (LEFT_X, 578),
            isOwnable = True,
            cardImage = WHITE_P 
        )

        # SPACE 13
        STATES_AVENUE = MonopolySpace(
            name = "States Avenue (Pink)", 
            type = 'property',
            location = (LEFT_X, 528),
            isOwnable =True,
            cardImage = PINK_P,
            printedPrice = 140,
            mortgageValue = 70,
            buildingCosts = 100,
            rentTiers=(10, 20, 50, 150, 450, 625, 750),
            color = 'pink'
        )

        # SPACE 14
        VIRGINIA_AVENUE = MonopolySpace(
            name = "Virginia Avenue (Pink)", 
            type = 'property',
            location = (LEFT_X, 478),
            isOwnable = True,
            cardImage = PINK_P,
            printedPrice = 160,
            mortgageValue = 80,
            buildingCosts = 100,
            rentTiers= (12, 24, 60, 180, 500, 700, 900),
            color = 'pink'
            
        )

        # SPACE 15
        PENNSYLVANIA_RAILROAD = MonopolySpace(
            name = "Pennsylvania Railroad",
            type = 'railroad', 
            location = (LEFT_X, 430),
            isOwnable = True,
            cardImage = BLACK_P
        )

        # SPACE 16
        ST_JAMES_PLACE = MonopolySpace(
            name = "St James Place (Orange)", 
            type = 'property',
            location = (LEFT_X, 380),
            isOwnable = True,
            cardImage = ORANGE_P,
            printedPrice = 180,
            mortgageValue = 90,
            buildingCosts = 100,
            rentTiers= (14, 28, 70, 200, 550, 750, 950),
            color = 'orange'
        )

        # SPACE 17
        COMMUNITY_CHEST_2 = MonopolySpace(
            name = "Community Chest", 
            type = 'comChest', 
            location = (LEFT_X, 331),
            isOwnable = False 
        )
        
        # SPACE 18
        TENNESSEE_AVENUE = MonopolySpace(
            name = "Tennesse Avenue (Orange)", 
            type = 'property',
            location = (LEFT_X, 280),
            isOwnable = True,
            cardImage = ORANGE_P,
            printedPrice = 180,
            mortgageValue = 90,
            buildingCosts = 100,
            rentTiers= (14, 28, 70, 200, 550, 750, 950),
            color='orange'
        )

        # SPACE 19
        NEW_YORK_AVENUE = MonopolySpace(
            name = "New York Avenue (Orange)", 
            type = 'property',
            location = (LEFT_X, 232),
            isOwnable = True,
            cardImage = ORANGE_P,
            printedPrice = 200,
            mortgageValue = 100,
            buildingCosts = 100,
            rentTiers = (16, 32, 80, 220, 600, 800, 1000),
            color = 'orange'
        )

        # SPACE 20
        FREE_PARKING = MonopolySpace(
            name = "Free Parking", 
            type = 'other', 
            location = (LEFT_X, TOP_Y),
            isOwnable = False
        )

        # SPACE 21
        KENTUCKY_AVENUE = MonopolySpace(
            name = "Kentucky Avenue (Red)", 
            type = 'property',
            location = (236, TOP_Y),
            isOwnable = True,
            cardImage = RED_P,
            printedPrice = 220,
            mortgageValue = 110,
            buildingCosts = 150,
            rentTiers = (18, 36, 90, 250, 700, 875, 1050),
            color = 'red'
        )

        # SPACE 22
        CHANCE_2 = MonopolySpace(
            name = "Chance", 
            type = 'chance', 
            location = (282, TOP_Y),
            isOwnable = False
        )

        # SPACE 23
        INDIANA_AVENUE = MonopolySpace(
            name = "Indiana Avenue (Red)", 
            type = 'property',
            location = (335, TOP_Y),
            isOwnable = True,
            cardImage = RED_P,
            printedPrice = 220,
            mortgageValue = 110,
            buildingCosts = 150,
            rentTiers = (18, 36, 90, 250, 700, 875, 1050),
            color = 'red'
        )

        # SPACE 24
        ILLINOIS_AVENUE = MonopolySpace(
            name = "Illinois Avenue (Red)", 
            type = 'property',
            location = (385, TOP_Y),
            isOwnable = True,
            cardImage = RED_P,
            printedPrice = 240,
            mortgageValue = 120,
            buildingCosts = 150,
            rentTiers = (20, 40, 100, 300, 750, 925, 1100),
            color = 'red'
        )

        # SPACE 25
        B_O_RAILROAD = MonopolySpace(
            name = "B & O Railroad",
            type = 'property',
            location = (432, TOP_Y),
            isOwnable = True,
            cardImage = BLACK_P
        )

        # SPACE 26
        ATLANTIC_AVENUE = MonopolySpace(
            name = "Atlantic Avenue (Yellow)", 
            type = 'property',
            location = (480, TOP_Y),
            isOwnable = True,
            cardImage = YELLOW_P,
            printedPrice = 260,
            mortgageValue = 130,
            buildingCosts = 150,
            rentTiers = (22, 44, 110, 330, 800, 975, 1150),
            color = 'yellow'
        )


        # SPACE 27
        VENTNOR_AVENUE = MonopolySpace(
            name = "Ventnor Avenue (Yellow)", 
            type = 'property',
            location = (530, TOP_Y),
            isOwnable = True,
            cardImage = YELLOW_P,
            printedPrice = 260,
            mortgageValue = 130,
            buildingCosts = 150,
            rentTiers = (22, 44, 110, 330, 800, 975, 1150),
            color = 'yellow'
        )


        # SPACE 28
        WATER_WORKS = MonopolySpace(
            name = "Water Works", 
            type = 'property',
            location = (585, TOP_Y), 
            isOwnable = True,
            cardImage = WHITE_P
        )

        # SPACE 29
        MARVIN_GARDENS = MonopolySpace(
            name = "Marvin Gardens (Yellow)", 
            type = 'property',
            location = (630, TOP_Y),
            isOwnable = True,
            cardImage = YELLOW_P,
            printedPrice = 280,
            mortgageValue = 140,
            buildingCosts = 150,
            rentTiers = (24, 28, 120, 360, 850, 1025, 1200),
            color = 'yellow'
        )


        # SPACE 30
        GO_TO_JAIL = MonopolySpace(
            name = "Go to Jail", 
            type = 'goToJail', 
            location = (RIGHT_X, TOP_Y),
            isOwnable = False
        )        

        # SPACE 31
        PACIFIC_AVENUE = MonopolySpace(
            name = "Pacific Avenue (Green)", 
            type = 'property',
            location = (RIGHT_X, 231),
            isOwnable = True,
            cardImage = GREEN_P,
            printedPrice = 300,
            mortgageValue = 150,
            buildingCosts = 200,
            rentTiers = (26, 52, 130, 390, 900, 1100, 1275),
            color = 'green'
        )

        # SPACE 32
        NORTH_CAROLINA_AVENUE = MonopolySpace(
            name = "North Carolina Avenue (Green)", 
            type = 'property',
            location = (RIGHT_X, 283),
            isOwnable = True,
            cardImage = GREEN_P,
            printedPrice = 300,
            mortgageValue = 150,
            buildingCosts = 200,
            rentTiers = (26, 52, 130, 390, 900, 1100, 1275),
            color = 'green'
        )

        # SPACE 33
        COMMUNITY_CHEST_3 = MonopolySpace(
            name = "Community Chest", 
            type = 'comChest', 
            location = (696, 333),
            isOwnable = False
        )
        
        # SPACE 34
        PENNSYLVANIA_AVENUE = MonopolySpace(
            name = "Pennsylvania Avenue (Green)", 
            type = 'property',
            location = (RIGHT_X, 380),
            isOwnable = True,
            cardImage = GREEN_P,
            printedPrice = 320,
            mortgageValue = 160,
            buildingCosts = 200,
            rentTiers = (28, 56, 150, 450, 1000, 1200, 1400),
            color = 'green'
        )

        # SPACE 35
        SHORT_LINE = MonopolySpace(
            name = "Short Line Railroad", 
            type = 'property', 
            location = (RIGHT_X, 430), 
            isOwnable = True,
            cardImage = BLACK_P
        )

        # SPACE 36
        CHANCE_3 = MonopolySpace(
            name = "Chance", 
            type = 'chance', 
            location = (RIGHT_X, 480),
            isOwnable = False
        )

        # SPACE 37
        PARK_PLACE = MonopolySpace(
            name = "Park Place (Blue)", 
            type = 'property',
            location = (RIGHT_X, 528),
            isOwnable = True,
            cardImage = BLUE_P,
            printedPrice = 350,
            mortgageValue = 175,
            buildingCosts = 200,
            rentTiers = (35, 70, 175, 500, 1100, 1300, 1500),
            color = 'blue'
        )

        # SPACE 38
        LUXURY_TAX = MonopolySpace(
            name = "Luxury Tax", 
            type = 'luxTax', 
            location = (696, 581),
            isOwnable = False
        )
        
        # SPACE 39       
        BOARDWALK = MonopolySpace(
            name = "Boardwalk (Blue)", 
            type = 'property',
            location = (RIGHT_X, 624),
            isOwnable = True,
            cardImage = BLUE_P,
            printedPrice = 400,
            mortgageValue = 200,
            buildingCosts = 200,
            rentTiers = (50, 100, 200, 600, 1400, 1700, 2000),
            color = 'blue'
        )   

        self.space = (GO, MEDITERRANEAN_AVENUE, COMMUNITY_CHEST_1, BALTIC_AVENUE, INCOME_TAX, READING_RAILROAD, ORIENTAL_AVENUE, CHANCE_1,
                 VERMONT_AVENUE, CONNECTICUT_AVENUE, JUST_VISITING, ST_CHARLES_PLACE, ELECTRIC_COMPANY, STATES_AVENUE, VIRGINIA_AVENUE,
                 PENNSYLVANIA_RAILROAD, ST_JAMES_PLACE, COMMUNITY_CHEST_2, TENNESSEE_AVENUE, NEW_YORK_AVENUE, FREE_PARKING, KENTUCKY_AVENUE, CHANCE_2,
                 INDIANA_AVENUE, ILLINOIS_AVENUE, B_O_RAILROAD, ATLANTIC_AVENUE, VENTNOR_AVENUE, WATER_WORKS, MARVIN_GARDENS, GO_TO_JAIL,
                 PACIFIC_AVENUE, NORTH_CAROLINA_AVENUE, COMMUNITY_CHEST_3, PENNSYLVANIA_AVENUE, SHORT_LINE, CHANCE_3, PARK_PLACE, LUXURY_TAX, BOARDWALK)

