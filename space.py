from enum import Enum
class Monopoly_Space(Enum):

    GO = ("GO", 'G')
    COMMUNITY_CHEST = ("Community Chest", 'C_C')
    INCOME_TAX = ("Income Tax", 'T')
    LUXURY_TAX = ("Luxury Tax", 'T')
    CHANCE = ("Chance", 'C')
    JUST_VISITING = ("Just Visting", 'N')
    FREE_PARKING = ("Free Parking", 'N')
    GO_TO_JAIL = ("Go to Jail", 'T_J')

    #BROWN
    MEDITERRANEAN_AVENUE = ("Mediterranean Avenue (Brown)", 'P', 60, 30, 50, (2, 4, 10, 30, 90, 160, 250))
    BALTIC_AVENUE = ("Baltic Avenue (Brown)", 'P', 60, 30, 50, (4, 8, 20, 60, 180, 320, 450))

    #LIGHT BLUE
    ORIENTAL_AVENUE = ("Oriental Avenue (Light Blue)", 'P', 100, 50, 50, (6, 12, 30, 90, 270, 400, 550))
    VERMONT_AVENUE = ("Vermont Avenue (Light Blue)", 'P', 100, 50, 50, (6, 12, 30, 90, 270, 400, 550))
    CONNECTICUT_AVENUE = ("Connecticut Avenue (Light Blue)", 'P', 120, 60, 50, (8, 16, 40, 100, 300, 450, 600))

    #PINK

    ST_CHARLES_PLACE = ("St Charles Place (Pink)", 'P', 140, 70, 100, (50, 150, 450, 625, 750))
    STATES_AVENUE = ("States Avenue (Pink)", 'P', 140, 70, 100, (50, 150, 450, 625, 750))
    VIRGINIA_AVENUE = ("Virginia Avenue (Pink)", 'P', 160, 80, 100, (12, 24, 60, 180, 500, 700, 900))

    #ORANGE

    ST_JAMES_PLACE = ("St James Place (Orange)", 'P', 180, 90, 100, (14, 28, 70, 200, 550, 750, 950))
    TENNESSEE_AVENUE = ("Tennesse Avenue (Orange)", 'P', 180, 90, 100, (14, 28, 70, 200, 550, 750, 950))
    NEW_YORK_AVENUE = ("New York Avenue (Orange)", 'P', 200, 100, 100, (80, 220, 600, 800, 1000))

    #RED

    KENTUCKY_AVENUE = ("Kentucky Avenue (Red)", 'P', 220, 110, 150, (18, 36, 90, 250, 700, 875, 1050))
    INDIANA_AVENUE = ("Indiana Avenue (Red)", 'P', 220, 110, 150, (18, 36, 90, 250, 700, 875, 1050))
    ILLINOIS_AVENUE = ("Illinois Avenue (Red)", 'P', 240, 120, 150, (20, 40, 100, 300, 750, 925, 1100))

    #YELLOW

    ATLANTIC_AVENUE = ("Atlantic Avenue (Yellow)", 'P', 260, 130, 150, (22, 44, 110, 330, 800, 975, 1150))
    VENTNOR_AVENUE = ("Ventnor Avenue (Yellow)", 'P', 260, 130, 150, (22, 44, 110, 330, 800, 975, 1150))
    MARVIN_GARDENS = ("Marvin Gardens (Yellow)", 'P', 280, 140, 150, (24, 28, 120, 360, 850, 1025, 1200))

    #GREEN

    PACIFIC_AVENUE = ("Pacific Avenue (Green)", 'P', 300, 150, 200, (26, 52, 130, 390, 900, 1100, 1275))
    NORTH_CAROLINA_AVENUE = ("North Carolina Avenue (Green)", 'P', 300, 150, 200, (26, 52, 130, 390, 900, 1100, 1275))
    PENNSYLVANIA_AVENUE = ("Pennsylvania Avenue (Green)", 'P',320, 160, 200, (28, 56, 150, 450, 1000, 1200, 1400))

    #DARK BLUE

    PARK_PLACE = ("Park Place (Blue)", 'P', 350, 175, 200, (35, 70, 175, 500, 1100, 1300, 1500))
    BOARDWALK = ("Boardwalk (Blue)", 'P', 400, 200, 200, (50, 100, 200, 600, 1400, 1700, 2000))

    #STATIONS

    READING_RAILROAD = ("Reading Railroad", 'R', 200, 100, None, (25, 50, 100, 200))
    PENNSYLVANIA_RAILROAD = ("Pennsylvania Railroad", 'R', 200, 100, None, (25, 50, 100, 200))
    B_O_RAILROAD = ("B. & O. Railroad", 'R', 200, 100, None, (25, 50, 100, 200))
    SHORT_LINE = ("Short Line Railroad", 'R', 200, 100, None, (25, 50, 100, 200))

    #UTILITIES

    ELECTRIC_COMPANY = ("Electric Company", 150, 75, None, (4 * 1, 12 * 1))
    WATER_WORKS = ("Water Works", 150, 75, None, (4 * 1, 12 * 1))

    def __init__(self, S_name, S_type, printed_price = None, mortgage_value = None, building_costs = None, rent_tier = None):
        self.S_name = S_name
        self.S_type = S_type

        self.printed_price = printed_price
        self.mortgage_value = mortgage_value
        self.building_costs = building_costs
        self.rent_tier = rent_tier

        self.owner = None

        
      
    