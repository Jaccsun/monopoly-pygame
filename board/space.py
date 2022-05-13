from text import Text

class Monopoly_Space:

    def __init__(self, space_name, x, y):
        self.space_name = space_name
        self.IS_BUYABLE = False
        self.x = x
        self.y = y

class Monopoly_Utility(Monopoly_Space):
    
    def __init__(self, space_name, x, y):
        super().__init__(space_name, x, y)

        self.owner = None
        self.current_tier = 0
        self.printed_price = 200
        self.mortgage_value = 75
        self.rent_tiers = (0, 1)
        self.IS_BUYABLE = True

    def increase_tier(self): 
        self.current_tier += 1

    def get_prompt(self, color):
        return Text('arial', 25, "Would you like to buy this Utility?(y/n):", color, 0, 20)

    def get_current_price(self):
        return self.rent_tiers[self.current_tier]

class Monopoly_Railroad(Monopoly_Space):
    
    def __init__(self, space_name, x, y):
        super().__init__(space_name, x, y)

        self.owner = None
        self.current_tier = 0
        self.printed_price = 200
        self.mortgage_value = 100
        self.rent_tiers = (25, 50, 100, 200)
        self.IS_BUYABLE = True

    def get_prompt(self, color):
        return Text('arial', 25, "Would you like to buy this Railroad? (y/n):", color, 0, 20)

    def get_current_price(self):
        return self.rent_tiers[self.current_tier]

    def increase_tier(self): 
        self.current_tier += 1

class Monopoly_Property(Monopoly_Space):

    def __init__(self, space_name, x, y, printed_price, mortgage_value, building_costs, rent_tiers):

        super().__init__(space_name, x, y)

        self.printed_price = printed_price
        self.mortgage_value = mortgage_value
        self.building_costs = building_costs
        self.rent_tiers = rent_tiers

        self.owner = None
        self.current_tier = 0
        self.IS_BUYABLE = True
    

    def get_current_price(self):
        return self.rent_tiers[self.current_tier]

    def increase_tier(self): 
        self.current_tier += 1

    def get_prompt(self, color):
        return Text('arial', 25, "Would you like to buy this Property? (y/n):", color, 0, 20)

    def give_tier_description(self):
        tier_description = ""
        match self.current_tier:
            case 1:
                tier_description = "You don't have a monopoly, therefore you cannot build on this property."
            case 2:
                tier_description = "This property has no Houses."
            case 3:
                tier_description =  "This property has 1 House."
            case 4:
                tier_description =  "This property has 2 Houses."
            case 5:
                tier_description =  "This property has 3 Houses."
            case 5:
                tier_description = "This property has 4 Houses." 
            case 6:
                tier_description = "This property has a Hotel."
        return tier_description

class Monopoly_Community_Chest(Monopoly_Space):
    
    def __init__(self, space_name, x, y):
        super().__init__(space_name, x, y)
        self.random = 0

class Monopoly_Chance(Monopoly_Space):
    
    def __init__(self, space_name, x, y):
        super().__init__(space_name, x, y)
        self.chance = 0


