from board.space import Monopoly_Space
from board.space_types.chance import Monopoly_Chance
from board.space_types.property import Monopoly_Property
from board.space_types.community_chest import Monopoly_Community_Chest

class Board:
    def __init__(self):
        
        GO = Monopoly_Space("GO")
        COMMUNITY_CHEST = Monopoly_Community_Chest("Community Chest")
        INCOME_TAX = Monopoly_Space("Income Tax")
        LUXURY_TAX = Monopoly_Space("Luxury Tax")
        CHANCE = Monopoly_Chance("Chance")
        JUST_VISITING = Monopoly_Space("Just Visting")
        FREE_PARKING = Monopoly_Space("Free Parking")
        GO_TO_JAIL = Monopoly_Space("Go to Jail")

        # BROWN
        MEDITERRANEAN_AVENUE = Monopoly_Property("Mediterranean Avenue (Brown)",
                             60, 30, 50, (2, 4, 10, 30, 90, 160, 250))
        BALTIC_AVENUE = Monopoly_Property("Baltic Avenue (Brown)",  60, 30,
                     50, (4, 8, 20, 60, 180, 320, 450))

        # LIGHT BLUE
        ORIENTAL_AVENUE = Monopoly_Property("Oriental Avenue (Light Blue)", 
                       100, 50, 50, (6, 12, 30, 90, 270, 400, 550))
        VERMONT_AVENUE = Monopoly_Property("Vermont Avenue (Light Blue)",  100,
                      50, 50, (6, 12, 30, 90, 270, 400, 550))
        CONNECTICUT_AVENUE = Monopoly_Property("Connecticut Avenue (Light Blue)",
                           120, 60, 50, (8, 16, 40, 100, 300, 450, 600))

        # PINK

        ST_CHARLES_PLACE = Monopoly_Property("St Charles Place (Pink)",  140,
                        70, 100, (50, 150, 450, 625, 750))
        STATES_AVENUE = Monopoly_Property("States Avenue (Pink)",  140,
                     70, 100, (50, 150, 450, 625, 750))
        VIRGINIA_AVENUE = Monopoly_Property("Virginia Avenue (Pink)",  160,
                       80, 100, (12, 24, 60, 180, 500, 700, 900))

        #ORANGE

        ST_JAMES_PLACE = Monopoly_Property("St James Place (Orange)",  180,
                      90, 100, (14, 28, 70, 200, 550, 750, 950))
        TENNESSEE_AVENUE = Monopoly_Property("Tennesse Avenue (Orange)",  180,
                        90, 100, (14, 28, 70, 200, 550, 750, 950))
        NEW_YORK_AVENUE = Monopoly_Property("New York Avenue (Orange)",  200,
                       100, 100, (80, 220, 600, 800, 1000))

        # RED

        KENTUCKY_AVENUE = Monopoly_Property("Kentucky Avenue (Red)",  220, 110,
                       150, (18, 36, 90, 250, 700, 875, 1050))
        INDIANA_AVENUE = Monopoly_Property("Indiana Avenue (Red)",  220, 110,
                      150, (18, 36, 90, 250, 700, 875, 1050))
        ILLINOIS_AVENUE = Monopoly_Property("Illinois Avenue (Red)",  240, 120,
                       150, (20, 40, 100, 300, 750, 925, 1100))

        # YELLOW

        ATLANTIC_AVENUE = Monopoly_Property("Atlantic Avenue (Yellow)",  260,
                       130, 150, (22, 44, 110, 330, 800, 975, 1150))
        VENTNOR_AVENUE = Monopoly_Property("Ventnor Avenue (Yellow)",  260,
                      130, 150, (22, 44, 110, 330, 800, 975, 1150))
        MARVIN_GARDENS = Monopoly_Property("Marvin Gardens (Yellow)",  280, 140,
                      150, (24, 28, 120, 360, 850, 1025, 1200))

        # GREEN

        PACIFIC_AVENUE = Monopoly_Property("Pacific Avenue (Green)",  300, 150,
                      200, (26, 52, 130, 390, 900, 1100, 1275))
        NORTH_CAROLINA_AVENUE = Monopoly_Property("North Carolina Avenue (Green)",
                              300, 150, 200, (26, 52, 130, 390, 900, 1100, 1275))
        PENNSYLVANIA_AVENUE = Monopoly_Property("Pennsylvania Avenue (Green)", 
                           320, 160, 200, (28, 56, 150, 450, 1000, 1200, 1400))

        # DARK BLUE

        PARK_PLACE = Monopoly_Property("Park Place (Blue)",  350, 175, 200,
                  (35, 70, 175, 500, 1100, 1300, 1500))
        BOARDWALK = Monopoly_Property("Boardwalk (Blue)",  400, 200, 200,
                 (50, 100, 200, 600, 1400, 1700, 2000))

        # STATIONS

        READING_RAILROAD = Monopoly_Property("Reading Railroad", 200,
                        100, None, (25, 50, 100, 200))
        PENNSYLVANIA_RAILROAD = Monopoly_Property("Pennsylvania Railroad",
                              200, 100, None, (25, 50, 100, 200))
        B_O_RAILROAD = Monopoly_Property("B & O Railroad",  200,
                    100, None, (25, 50, 100, 200))
        SHORT_LINE = Monopoly_Property("Short Line Railroad",  200,
                  100, None, (25, 50, 100, 200))

        # UTILITIES

        ELECTRIC_COMPANY = Monopoly_Space("Electric Company")
        WATER_WORKS = Monopoly_Space("Water Works")

        self.space = (GO, MEDITERRANEAN_AVENUE, COMMUNITY_CHEST, BALTIC_AVENUE, INCOME_TAX, READING_RAILROAD, ORIENTAL_AVENUE, CHANCE,
                 VERMONT_AVENUE, CONNECTICUT_AVENUE, JUST_VISITING, ST_CHARLES_PLACE, ELECTRIC_COMPANY, STATES_AVENUE, VIRGINIA_AVENUE,
                 PENNSYLVANIA_RAILROAD, ST_JAMES_PLACE, COMMUNITY_CHEST, TENNESSEE_AVENUE, NEW_YORK_AVENUE, FREE_PARKING, KENTUCKY_AVENUE, CHANCE,
                 INDIANA_AVENUE, ILLINOIS_AVENUE, B_O_RAILROAD, ATLANTIC_AVENUE, VENTNOR_AVENUE, WATER_WORKS, MARVIN_GARDENS, GO_TO_JAIL,
                 PACIFIC_AVENUE, NORTH_CAROLINA_AVENUE, COMMUNITY_CHEST, PENNSYLVANIA_AVENUE, SHORT_LINE, CHANCE, PARK_PLACE, LUXURY_TAX, BOARDWALK)

