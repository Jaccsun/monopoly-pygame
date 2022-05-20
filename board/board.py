from xml.etree.ElementTree import PI

from board.space import *
import pygame
import os 

class Board:
    def __init__(self):
        
        BOTTOM_Y = 692
        LEFT_X = 150
        TOP_Y = 160
        RIGHT_X = 696


        self.IMAGE = pygame.image.load(os.path.join('Assets', 'board.jpg'))

        GO = Monopoly_Space("GO", 690, 690)

        COMMUNITY_CHEST_1 = Monopoly_Community_Chest("Community Chest", 580, BOTTOM_Y)
        COMMUNITY_CHEST_2 = Monopoly_Community_Chest("Community Chest", LEFT_X, 331)
        COMMUNITY_CHEST_3 = Monopoly_Community_Chest("Community Chest", 696, 333)
        
        CHANCE_1 = Monopoly_Chance("Chance", 332, BOTTOM_Y)
        CHANCE_2 = Monopoly_Chance("Chance", 282, TOP_Y)
        CHANCE_3 = Monopoly_Chance("Chance", RIGHT_X, 480)

        LUXURY_TAX = Monopoly_Space("Luxury Tax", 696, 581)
        
        JUST_VISITING = Monopoly_Space("Just Visting", 149, 712)
        FREE_PARKING = Monopoly_Space("Free Parking", LEFT_X, TOP_Y)
        GO_TO_JAIL = Monopoly_Space("Go to Jail", RIGHT_X, TOP_Y)

        
        # BROWN 
        MEDITERRANEAN_AVENUE = Monopoly_Property("Mediterranean Avenue (Brown)", 630, BOTTOM_Y,
        60, 30, 50, (2, 4, 10, 30, 90, TOP_Y, 250), BROWN_P, "BROWN_P")
        BALTIC_AVENUE = Monopoly_Property("Baltic Avenue (Brown)",  530, BOTTOM_Y,
        60, 30, 50, (4, 8, 20, 60, 180, 320, 450), BROWN_P, "BROWN_P")
        INCOME_TAX = Monopoly_Space("Income Tax", 482, BOTTOM_Y)

        # LIGHT BLUE
        ORIENTAL_AVENUE = Monopoly_Property("Oriental Avenue (Light Blue)", 383, BOTTOM_Y,
        100, 50, 50, (6, 12, 30, 90, 270, 400, 550), LIGHT_BLUE_P, "LIGHT_BLUE_P")
        VERMONT_AVENUE = Monopoly_Property("Vermont Avenue (Light Blue)", 285, BOTTOM_Y, 
        100, 50, 50, (6, 12, 30, 90, 270, 400, 550), LIGHT_BLUE_P, "LIGHT_BLUE_P")
        CONNECTICUT_AVENUE = Monopoly_Property("Connecticut Avenue (Light Blue)", 235, BOTTOM_Y,
        120, 60, 50, (8, 16, 40, 100, 300, 450, 600), LIGHT_BLUE_P, "LIGHT_BLUE_P")

        # PINK

        ST_CHARLES_PLACE = Monopoly_Property("St Charles Place (Pink)", LEFT_X, 629,
        140, 70, 100, (10, 20, 50, 150, 450, 625, 750), PINK_P, "PINK_P")
        STATES_AVENUE = Monopoly_Property("States Avenue (Pink)", LEFT_X, 528,
        140, 70, 100, (10, 20, 50, 150, 450, 625, 750), PINK_P, "PINK_P")
        VIRGINIA_AVENUE = Monopoly_Property("Virginia Avenue (Pink)", LEFT_X, 483,
        160, 80, 100, (12, 24, 60, 180, 500, 700, 900), PINK_P, "PINK_P")

        #ORANGE

        ST_JAMES_PLACE = Monopoly_Property("St James Place (Orange)", LEFT_X, 380,
        180, 90, 100, (14, 28, 70, 200, 550, 750, 950), ORANGE_P, "ORANGE_P")
        TENNESSEE_AVENUE = Monopoly_Property("Tennesse Avenue (Orange)", LEFT_X, 280,
        180, 90, 100, (14, 28, 70, 200, 550, 750, 950), ORANGE_P, "ORANGE_P")
        NEW_YORK_AVENUE = Monopoly_Property("New York Avenue (Orange)", LEFT_X, 232, 
        200, 100, 100, (16, 32, 80, 220, 600, 800, 1000), ORANGE_P, "ORANGE_P")

        # RED

        KENTUCKY_AVENUE = Monopoly_Property("Kentucky Avenue (Red)", 234, TOP_Y,
        220, 110, 150, (18, 36, 90, 250, 700, 875, 1050), RED_P, "RED_P")
        INDIANA_AVENUE = Monopoly_Property("Indiana Avenue (Red)", 335, TOP_Y,
        220, 110, 150, (18, 36, 90, 250, 700, 875, 1050), RED_P, "RED_P")
        ILLINOIS_AVENUE = Monopoly_Property("Illinois Avenue (Red)", 382, TOP_Y,
        240, 120, 150, (20, 40, 100, 300, 750, 925, 1100), RED_P, "RED_P")

        # YELLOW

        ATLANTIC_AVENUE = Monopoly_Property("Atlantic Avenue (Yellow)", 480, TOP_Y, 
        260, 130, 150, (22, 44, 110, 330, 800, 975, 1150), YELLOW_P, "YELLOW_P")
        VENTNOR_AVENUE = Monopoly_Property("Ventnor Avenue (Yellow)", 530, TOP_Y,
        260, 130, 150, (22, 44, 110, 330, 800, 975, 1150), YELLOW_P, "YELLOW_P")
        MARVIN_GARDENS = Monopoly_Property("Marvin Gardens (Yellow)", 625, TOP_Y ,
        280, 140, 150, (24, 28, 120, 360, 850, 1025, 1200), YELLOW_P, "YELLOW_P")

        # GREEN

        PACIFIC_AVENUE = Monopoly_Property("Pacific Avenue (Green)", RIGHT_X, 231,  
        300, 150, 200, (26, 52, 130, 390, 900, 1100, 1275), GREEN_P, "GREEN_P")
        NORTH_CAROLINA_AVENUE = Monopoly_Property("North Carolina Avenue (Green)", RIGHT_X, 283,
        300, 150, 200, (26, 52, 130, 390, 900, 1100, 1275), GREEN_P, "GREEN_P")
        PENNSYLVANIA_AVENUE = Monopoly_Property("Pennsylvania Avenue (Green)",  RIGHT_X, 380,
        320, 160, 200, (28, 56, 150, 450, 1000, 1200, 1400), GREEN_P, "GREEN_P")

        # DARK BLUE

        PARK_PLACE = Monopoly_Property("Park Place (Blue)", RIGHT_X, 533,
        350, 175, 200, (35, 70, 175, 500, 1100, 1300, 1500), BLUE_P, "BLUE_P")
        BOARDWALK = Monopoly_Property("Boardwalk (Blue)", RIGHT_X, 629,
        400, 200, 200, (50, 100, 200, 600, 1400, 1700, 2000), BLUE_P, "BLUE_P")

        # STATIONS

        READING_RAILROAD = Monopoly_Railroad("Reading Railroad", 432, BOTTOM_Y, BLACK_P, "BLACK_P")
        PENNSYLVANIA_RAILROAD = Monopoly_Railroad("Pennsylvania Railroad", LEFT_X, 430, BLACK_P, "BLACK_P")
        B_O_RAILROAD = Monopoly_Railroad("B & O Railroad", 432, TOP_Y, BLACK_P, "BLACK_P")
        SHORT_LINE = Monopoly_Railroad("Short Line Railroad", RIGHT_X, 430, BLACK_P, "BLACK_P")

        # UTILITIES

        ELECTRIC_COMPANY = Monopoly_Utility("Electric Company", LEFT_X, 578, WHITE_P, "WHITE_P")
        WATER_WORKS = Monopoly_Utility("Water Works", 585, TOP_Y, WHITE_P, "WHITE_P")

        self.space = (GO, MEDITERRANEAN_AVENUE, COMMUNITY_CHEST_1, BALTIC_AVENUE, INCOME_TAX, READING_RAILROAD, ORIENTAL_AVENUE, CHANCE_1,
                 VERMONT_AVENUE, CONNECTICUT_AVENUE, JUST_VISITING, ST_CHARLES_PLACE, ELECTRIC_COMPANY, STATES_AVENUE, VIRGINIA_AVENUE,
                 PENNSYLVANIA_RAILROAD, ST_JAMES_PLACE, COMMUNITY_CHEST_2, TENNESSEE_AVENUE, NEW_YORK_AVENUE, FREE_PARKING, KENTUCKY_AVENUE, CHANCE_2,
                 INDIANA_AVENUE, ILLINOIS_AVENUE, B_O_RAILROAD, ATLANTIC_AVENUE, VENTNOR_AVENUE, WATER_WORKS, MARVIN_GARDENS, GO_TO_JAIL,
                 PACIFIC_AVENUE, NORTH_CAROLINA_AVENUE, COMMUNITY_CHEST_3, PENNSYLVANIA_AVENUE, SHORT_LINE, CHANCE_3, PARK_PLACE, LUXURY_TAX, BOARDWALK)

