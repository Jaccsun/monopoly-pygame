
from board.space_types.property import Monopoly_Property


def enter_selection(current_player, board):
    in_selection = True

    # Entering selection screen, player can roll,
    # manage their properties, trade, or forfeit thegame.

    while (in_selection):

        input("-It's your turn-")

        print("Current position: " + str(current_player.position), 
        "Money: " + str(current_player.money) + "$")

        select = input("0 - Roll | 1 - Property manager | 2 - Trade | 3 - Forfeit ")

        # Rolls the die upon player selection.
        match select:
            case "0":
                select_roll(current_player, board)
                in_selection = False
            case "1":
                select_property_manager(current_player)
            case "2":
                select_trade()
            case "3":
                print("Thanks for playing.")
                in_selection = False
                turn_cycle = False
            case _:
                print("Invalid input")
        
        print("Your current cash: " + str(current_player.money) + "$")

def select_roll(current_player, board):
    player_roll = current_player.roll() 

    # Tells the player what they rolled.
    input("You rolled a " + str(player_roll.value)) 
    current_player.move(player_roll)

    # Uses the info from the roll and the new player position to determine the space they landed on.
    landed_on_space = board.space[current_player.position]
    print("You landed on " + str(landed_on_space.space_name))

    # Property space type.
    if(isinstance(landed_on_space, Monopoly_Property)):
        select_roll_prompt_property(landed_on_space, current_player)
        

# Property prompt system.
def select_roll_prompt_property(landed_on_space, current_player):
    if (landed_on_space.owner == None):
        in_prompt = True
        while(in_prompt):
            property_prompt = input(
                "Would you like to buy this property? (y/n): ")
            if (property_prompt == "y"):
                if(current_player.money - landed_on_space.printed_price < 0):
                    print("You don't have enough money to purchase this property.")
                    in_prompt = False
                else:
                    print("You have purchased " +
                          str(landed_on_space.space_name) + "!")     

                    current_player.buy(landed_on_space)
                    in_prompt = False
            elif (property_prompt == "n"):
                print("You decided not to buy " + str(landed_on_space.space_name))
                in_prompt = False
            else:
                print("Input not understood")
    elif (landed_on_space.owner == current_player):
        print("You own this property")
    else:   
        print("This property is owned by " + landed_on_space.owner)
        print("Amount owned: " + landed_on_space.get_current_price())
        in_selection = True
        while in_selection:
            input("0 - Pay | 1 - Mortage")

# Visual property manager to view properties and build.      
def select_property_manager(current_player):
    EXIT = "0"
    if len(current_player.properties) == 0:
        print("You don't have any properties.")
    else: 
       
        print("Your current properties")
        current_player.print_owned_properties()

        selection = True
        while selection:

            select = input("0 - Exit | (1-" + str(len(current_player.properties)) +" - Select Property)")
            is_valid_property_selection = select.isnumeric and (int(select) - 1) < len(current_player.properties)

            if select == EXIT:
                return None
            elif is_valid_property_selection: 
                
                selected_property = current_player.properties[int(select) - 1]
                
                print("You selected " + selected_property.space_name)
                print(selected_property.give_tier_description())

                if selected_property.current_tier == 1: 
                    return None
                
            else:
                print("Invalid Selection.")

def select_trade():
    print("test")
 
