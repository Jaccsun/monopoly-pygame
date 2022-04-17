from board.space import Monopoly_Space

class Monopoly_Property(Monopoly_Space):

    def __init__(self, space_name, printed_price, mortgage_value, building_costs, rent_tiers):

        super().__init__(space_name)

        self.printed_price = printed_price
        self.mortgage_value = mortgage_value
        self.building_costs = building_costs
        self.rent_tiers = rent_tiers

        self.owner = None
        self.current_tier = 0

    def get_current_price(self):
        return self.rent_tiers[self.current_tier]

    def increase_tier(self): 
        self.current_tier += 1

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





