from board.space import *
import pygame
import os 

class Board:
    def __init__(self):
        
        self.IMAGE = pygame.image.load(os.path.join('Assets', 'board.jpg'))

        GO = Monopoly_Space("GO", 690, 690)

        COMMUNITY_CHEST_1 = Monopoly_Community_Chest("Community Chest", 573, 692)
        COMMUNITY_CHEST_2 = Monopoly_Community_Chest("Community Chest", 150, 325)
        COMMUNITY_CHEST_3 = Monopoly_Community_Chest("Community Chest", 696, 333)
        
        CHANCE_1 = Monopoly_Chance("Chance", 328, 692)
        CHANCE_2 = Monopoly_Chance("Chance", 279, 160)
        CHANCE_3 = Monopoly_Chance("Chance", 696, 480)

        LUXURY_TAX = Monopoly_Space("Luxury Tax", 696, 581)
        
        JUST_VISITING = Monopoly_Space("Just Visting", 149, 712)
        FREE_PARKING = Monopoly_Space("Free Parking", 150, 160)
        GO_TO_JAIL = Monopoly_Space("Go to Jail", 696, 160)

        
        # BROWN 
        MEDITERRANEAN_AVENUE = Monopoly_Property("Mediterranean Avenue (Brown)", 623, 692,
        60, 30, 50, (2, 4, 10, 30, 90, 160, 250))
        BALTIC_AVENUE = Monopoly_Property("Baltic Avenue (Brown)",  525, 692,
        60, 30, 50, (4, 8, 20, 60, 180, 320, 450))
        INCOME_TAX = Monopoly_Space("Income Tax", 474, 692)

        # LIGHT BLUE
        ORIENTAL_AVENUE = Monopoly_Property("Oriental Avenue (Light Blue)", 378, 692,
        100, 50, 50, (6, 12, 30, 90, 270, 400, 550))
        VERMONT_AVENUE = Monopoly_Property("Vermont Avenue (Light Blue)", 278, 692, 
        100, 50, 50, (6, 12, 30, 90, 270, 400, 550))
        CONNECTICUT_AVENUE = Monopoly_Property("Connecticut Avenue (Light Blue)", 229, 692,
        120, 60, 50, (8, 16, 40, 100, 300, 450, 600))

        # PINK

        ST_CHARLES_PLACE = Monopoly_Property("St Charles Place (Pink)", 151, 620,
        140, 70, 100, (50, 150, 450, 625, 750))
        STATES_AVENUE = Monopoly_Property("States Avenue (Pink)", 150, 523,
        140, 70, 100, (50, 150, 450, 625, 750))
        VIRGINIA_AVENUE = Monopoly_Property("Virginia Avenue (Pink)", 150, 457,
        160, 80, 100, (12, 24, 60, 180, 500, 700, 900))

        #ORANGE

        ST_JAMES_PLACE = Monopoly_Property("St James Place (Orange)", 151, 620,
        180, 90, 100, (14, 28, 70, 200, 550, 750, 950))
        TENNESSEE_AVENUE = Monopoly_Property("Tennesse Avenue (Orange)", 150, 276,
        180, 90, 100, (14, 28, 70, 200, 550, 750, 950))
        NEW_YORK_AVENUE = Monopoly_Property("New York Avenue (Orange)", 150, 228, 
        200, 100, 100, (80, 220, 600, 800, 1000))

        # RED

        KENTUCKY_AVENUE = Monopoly_Property("Kentucky Avenue (Red)", 229, 160,
        220, 110, 150, (18, 36, 90, 250, 700, 875, 1050))
        INDIANA_AVENUE = Monopoly_Property("Indiana Avenue (Red)", 229, 160,
        220, 110, 150, (18, 36, 90, 250, 700, 875, 1050))
        ILLINOIS_AVENUE = Monopoly_Property("Illinois Avenue (Red)", 373, 160,
        240, 120, 150, (20, 40, 100, 300, 750, 925, 1100))

        # YELLOW

        ATLANTIC_AVENUE = Monopoly_Property("Atlantic Avenue (Yellow)", 474, 160, 
        260, 130, 150, (22, 44, 110, 330, 800, 975, 1150))
        VENTNOR_AVENUE = Monopoly_Property("Ventnor Avenue (Yellow)", 552, 160,
        260, 130, 150, (22, 44, 110, 330, 800, 975, 1150))
        MARVIN_GARDENS = Monopoly_Property("Marvin Gardens (Yellow)", 621, 160 ,
        280, 140, 150, (24, 28, 120, 360, 850, 1025, 1200))

        # GREEN

        PACIFIC_AVENUE = Monopoly_Property("Pacific Avenue (Green)", 696, 231,  
        300, 150, 200, (26, 52, 130, 390, 900, 1100, 1275))
        NORTH_CAROLINA_AVENUE = Monopoly_Property("North Carolina Avenue (Green)", 696, 283,
        300, 150, 200, (26, 52, 130, 390, 900, 1100, 1275))
        PENNSYLVANIA_AVENUE = Monopoly_Property("Pennsylvania Avenue (Green)",  696, 380,
        320, 160, 200, (28, 56, 150, 450, 1000, 1200, 1400))

        # DARK BLUE

        PARK_PLACE = Monopoly_Property("Park Place (Blue)", 696, 524,
        350, 175, 200, (35, 70, 175, 500, 1100, 1300, 1500))
        BOARDWALK = Monopoly_Property("Boardwalk (Blue)", 696, 629,
        400, 200, 200, (50, 100, 200, 600, 1400, 1700, 2000))

        # STATIONS

        READING_RAILROAD = Monopoly_Railroad("Reading Railroad", 425, 692)
        PENNSYLVANIA_RAILROAD = Monopoly_Railroad("Pennsylvania Railroad", 150, 425)
        B_O_RAILROAD = Monopoly_Railroad("B & O Railroad", 427, 160)
        SHORT_LINE = Monopoly_Railroad("Short Line Railroad", 696, 425)

        # UTILITIES

        ELECTRIC_COMPANY = Monopoly_Utility("Electric Company", 150, 573)
        WATER_WORKS = Monopoly_Utility("Water Works", 570, 160)

        self.space = (GO, MEDITERRANEAN_AVENUE, COMMUNITY_CHEST_1, BALTIC_AVENUE, INCOME_TAX, READING_RAILROAD, ORIENTAL_AVENUE, CHANCE_1,
                 VERMONT_AVENUE, CONNECTICUT_AVENUE, JUST_VISITING, ST_CHARLES_PLACE, ELECTRIC_COMPANY, STATES_AVENUE, VIRGINIA_AVENUE,
                 PENNSYLVANIA_RAILROAD, ST_JAMES_PLACE, COMMUNITY_CHEST_2, TENNESSEE_AVENUE, NEW_YORK_AVENUE, FREE_PARKING, KENTUCKY_AVENUE, CHANCE_2,
                 INDIANA_AVENUE, ILLINOIS_AVENUE, B_O_RAILROAD, ATLANTIC_AVENUE, VENTNOR_AVENUE, WATER_WORKS, MARVIN_GARDENS, GO_TO_JAIL,
                 PACIFIC_AVENUE, NORTH_CAROLINA_AVENUE, COMMUNITY_CHEST_3, PENNSYLVANIA_AVENUE, SHORT_LINE, CHANCE_3, PARK_PLACE, LUXURY_TAX, BOARDWALK)

