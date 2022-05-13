
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
 
