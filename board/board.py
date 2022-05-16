from xml.etree.ElementTree import PI

from board.space import *
import pygame
import os 

class Board:
    def __init__(self):
        
        self.IMAGE = pygame.image.load(os.path.join('Assets', 'board.jpg'))

        GO = Monopoly_Space("GO", 690, 690)

        COMMUNITY_CHEST_1 = Monopoly_Community_Chest("Community Chest", 580, 692)
        COMMUNITY_CHEST_2 = Monopoly_Community_Chest("Community Chest", 150, 331)
        COMMUNITY_CHEST_3 = Monopoly_Community_Chest("Community Chest", 696, 333)
        
        CHANCE_1 = Monopoly_Chance("Chance", 332, 692)
        CHANCE_2 = Monopoly_Chance("Chance", 282, 160)
        CHANCE_3 = Monopoly_Chance("Chance", 696, 480)

        LUXURY_TAX = Monopoly_Space("Luxury Tax", 696, 581)
        
        JUST_VISITING = Monopoly_Space("Just Visting", 149, 712)
        FREE_PARKING = Monopoly_Space("Free Parking", 150, 160)
        GO_TO_JAIL = Monopoly_Space("Go to Jail", 696, 160)

        
        # BROWN 
        MEDITERRANEAN_AVENUE = Monopoly_Property("Mediterranean Avenue (Brown)", 630, 692,
        60, 30, 50, (2, 4, 10, 30, 90, 160, 250), BROWN_P)
        BALTIC_AVENUE = Monopoly_Property("Baltic Avenue (Brown)",  530, 692,
        60, 30, 50, (4, 8, 20, 60, 180, 320, 450), BROWN_P)
        INCOME_TAX = Monopoly_Space("Income Tax", 482, 692)

        # LIGHT BLUE
        ORIENTAL_AVENUE = Monopoly_Property("Oriental Avenue (Light Blue)", 383, 692,
        100, 50, 50, (6, 12, 30, 90, 270, 400, 550), LIGHT_BLUE_P)
        VERMONT_AVENUE = Monopoly_Property("Vermont Avenue (Light Blue)", 285, 692, 
        100, 50, 50, (6, 12, 30, 90, 270, 400, 550), LIGHT_BLUE_P)
        CONNECTICUT_AVENUE = Monopoly_Property("Connecticut Avenue (Light Blue)", 235, 692,
        120, 60, 50, (8, 16, 40, 100, 300, 450, 600), LIGHT_BLUE_P)

        # PINK

        ST_CHARLES_PLACE = Monopoly_Property("St Charles Place (Pink)", 151, 629,
        140, 70, 100, (50, 150, 450, 625, 750), PINK_P)
        STATES_AVENUE = Monopoly_Property("States Avenue (Pink)", 150, 528,
        140, 70, 100, (50, 150, 450, 625, 750), PINK_P)
        VIRGINIA_AVENUE = Monopoly_Property("Virginia Avenue (Pink)", 150, 483,
        160, 80, 100, (12, 24, 60, 180, 500, 700, 900), PINK_P)

        #ORANGE

        ST_JAMES_PLACE = Monopoly_Property("St James Place (Orange)", 151, 380,
        180, 90, 100, (14, 28, 70, 200, 550, 750, 950), ORANGE_P)
        TENNESSEE_AVENUE = Monopoly_Property("Tennesse Avenue (Orange)", 150, 280,
        180, 90, 100, (14, 28, 70, 200, 550, 750, 950), ORANGE_P)
        NEW_YORK_AVENUE = Monopoly_Property("New York Avenue (Orange)", 150, 232, 
        200, 100, 100, (16, 32, 80, 220, 600, 800, 1000), ORANGE_P)

        # RED

        KENTUCKY_AVENUE = Monopoly_Property("Kentucky Avenue (Red)", 234, 160,
        220, 110, 150, (18, 36, 90, 250, 700, 875, 1050), RED_P)
        INDIANA_AVENUE = Monopoly_Property("Indiana Avenue (Red)", 335, 160,
        220, 110, 150, (18, 36, 90, 250, 700, 875, 1050), RED_P)
        ILLINOIS_AVENUE = Monopoly_Property("Illinois Avenue (Red)", 382, 160,
        240, 120, 150, (20, 40, 100, 300, 750, 925, 1100), RED_P)

        # YELLOW

        ATLANTIC_AVENUE = Monopoly_Property("Atlantic Avenue (Yellow)", 480, 160, 
        260, 130, 150, (22, 44, 110, 330, 800, 975, 1150), YELLOW_P)
        VENTNOR_AVENUE = Monopoly_Property("Ventnor Avenue (Yellow)", 530, 160,
        260, 130, 150, (22, 44, 110, 330, 800, 975, 1150), YELLOW_P)
        MARVIN_GARDENS = Monopoly_Property("Marvin Gardens (Yellow)", 625, 160 ,
        280, 140, 150, (24, 28, 120, 360, 850, 1025, 1200), YELLOW_P)

        # GREEN

        PACIFIC_AVENUE = Monopoly_Property("Pacific Avenue (Green)", 696, 231,  
        300, 150, 200, (26, 52, 130, 390, 900, 1100, 1275), GREEN_P)
        NORTH_CAROLINA_AVENUE = Monopoly_Property("North Carolina Avenue (Green)", 696, 283,
        300, 150, 200, (26, 52, 130, 390, 900, 1100, 1275), GREEN_P)
        PENNSYLVANIA_AVENUE = Monopoly_Property("Pennsylvania Avenue (Green)",  696, 380,
        320, 160, 200, (28, 56, 150, 450, 1000, 1200, 1400), GREEN_P)

        # DARK BLUE

        PARK_PLACE = Monopoly_Property("Park Place (Blue)", 696, 533,
        350, 175, 200, (35, 70, 175, 500, 1100, 1300, 1500), BLUE_P)
        BOARDWALK = Monopoly_Property("Boardwalk (Blue)", 696, 629,
        400, 200, 200, (50, 100, 200, 600, 1400, 1700, 2000), BLUE_P)

        # STATIONS

        READING_RAILROAD = Monopoly_Railroad("Reading Railroad", 432, 692, BLACK_P)
        PENNSYLVANIA_RAILROAD = Monopoly_Railroad("Pennsylvania Railroad", 150, 430, BLACK_P)
        B_O_RAILROAD = Monopoly_Railroad("B & O Railroad", 432, 160, BLACK_P)
        SHORT_LINE = Monopoly_Railroad("Short Line Railroad", 696, 430, BLACK_P)

        # UTILITIES

        ELECTRIC_COMPANY = Monopoly_Utility("Electric Company", 150, 578, WHITE_P)
        WATER_WORKS = Monopoly_Utility("Water Works", 585, 160, WHITE_P)

        self.space = (GO, MEDITERRANEAN_AVENUE, COMMUNITY_CHEST_1, BALTIC_AVENUE, INCOME_TAX, READING_RAILROAD, ORIENTAL_AVENUE, CHANCE_1,
                 VERMONT_AVENUE, CONNECTICUT_AVENUE, JUST_VISITING, ST_CHARLES_PLACE, ELECTRIC_COMPANY, STATES_AVENUE, VIRGINIA_AVENUE,
                 PENNSYLVANIA_RAILROAD, ST_JAMES_PLACE, COMMUNITY_CHEST_2, TENNESSEE_AVENUE, NEW_YORK_AVENUE, FREE_PARKING, KENTUCKY_AVENUE, CHANCE_2,
                 INDIANA_AVENUE, ILLINOIS_AVENUE, B_O_RAILROAD, ATLANTIC_AVENUE, VENTNOR_AVENUE, WATER_WORKS, MARVIN_GARDENS, GO_TO_JAIL,
                 PACIFIC_AVENUE, NORTH_CAROLINA_AVENUE, COMMUNITY_CHEST_3, PENNSYLVANIA_AVENUE, SHORT_LINE, CHANCE_3, PARK_PLACE, LUXURY_TAX, BOARDWALK)

