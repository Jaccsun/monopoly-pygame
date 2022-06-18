from text import Text
import pygame
import random

class Button:

    name: str 
    text: Text
    rect: pygame.rect.Rect

    def __init__(self, text : str, x : int, y : int, 
    x_size : int, y_size, color=(40, 40, 40)):
        self.name = text
        self.x, self.y, self.x_size, self.y_size  = x, y, x_size, y_size
        self.text = Text(text, x, y, color=(255, 255, 255))
        self.color = color 
        self.color_over = (90, 90, 90)
        self.rect = pygame.Rect(x, y, x_size, y_size)
        self.current_color = self.color
    
    def run(self, game):
        if (self.name == "Start"):
            game.buttons = [Button("Roll (Order)", 280, 0, 90, 40)]
            game.texts = [Text("Roll to determine game order:", 0, 0)]
        if (self.name == "Roll (Order)"):
            game.texts.clear()
            game.buttons.clear()
            rolls = [random.randint(2, 12) for x in range(4)]
            game.players = [x[1] for x in sorted(zip(rolls, game.players),
            key= lambda test: test[0], reverse=True)]
            game.texts.extend([Text(f"Player 1 "
            f"rolled: {str(rolls[0])}", 0, 60), 
            Text(f"Player 2 rolled: {str(rolls[1])}", 200, 60), 
            Text(f"Player 3 rolled: {str(rolls[2])}", 400, 60),
            Text(f"Player 4 rolled: {str(rolls[3])}", 600, 60)])
            game.buttons  = [Button("Play", 0, 0, 70, 40)]
        if (self.name == "Play"):
            game.texts.clear()
            game.buttons.clear()
            game.update_player_text()
            game.handle_turn()
        if (self.name == "next"):
            if game.currentTurn == 3:
                game.currentTurn = 0
            else:
                game.currentTurn += 1
            game.texts.clear()
            game.buttons.clear()
            game.update_player_text()
            game.handle_turn()
        # Handles a roll
        if (self.name == "Roll"):
            game.player.roll(game)
            game.update_player_text()
        # buy button for newly-unowned properties     
        if (self.name == "Buy"):
            game.buttons.clear()
            game.texts.clear()
            if(game.player.money - game.landed_on_space.printed_price < 0):
                game.texts.append(Text("You don't have enough money "
                f"to purchase this property.", 0, 20))
            else: 
                game.texts.append(Text(f"You have purchased "
                f"{str(game.landed_on_space.space_name)}!", 0, 20))
                game.player.buy(game.landed_on_space)
            game.update_player_text()
            game.buttons.clear()
            game.buttons.append(Button("next",0, 50, 70, 40))
            
        # dont buy property 
        if (self.name == "Don't Buy"): 
            game.buttons = []
            game.texts = []
            game.texts.append(Text(f"You decided not to buy"
            + f" {str(game.landed_on_space.space_name)}", 0, 20)),
            game.buttons = [Button("next",0, 50, 70, 40)]
        # pay player if landed on their property
        if (self.name == "Pay"):
            game.player.pay(game)
        # bankrupt properties button
        if (self.name == "Bankrupt"):
            print("Thanks for playing!")
            game.buttons = [Button("next",0, 50, 70, 40)]
        if (self.name == "Trade"):
            game.texts = []
            game.buttons = []

            game.money_exchange = [0, 0]
            game.show_board = False
            game.current_trade = 1
            game.trade_list.extend([game.player, game.player_2])

            game.update_trade_text()

            game.buttons.extend([Button("Next Player", 790, 0, 105, 40),
            Button("Back", 0, 0, 40, 40),
            Button("Increase", 140, 600, 75, 40),
            Button("Decrease", 240, 600, 75, 40),
            Button("Increase", 580, 600, 75, 40),
            Button("Decrease", 680, 600, 75, 40),
            Button("Make Trade", 20, 700, 120, 50)])

        if (self.name == "Next Player"):
            if game.current_trade == 3:
                game.current_trade = 1
            else:
                game.current_trade += 1

            game.money_exchange = [0, 0]    

            game.trade_list[0].properties.extend(game.property_exchange[0])
            game.trade_list[1].properties.extend(game.property_exchange[1])
            game.property_exchange = [[],[]]

            player = game.PLAYER_LIST[game.current_trade]
            game.trade_list[1] = player    

        
            game.update_trade_text()
        if (self.name == "Back"):
            if game.in_manager:
                game.in_manager = False
            else:
                game.trade_list[0].properties.extend(game.property_exchange[0])
                game.trade_list[1].properties.extend(game.property_exchange[1])
                game.property_exchange = [[],[]]
                game.trade_list = []
            
            game.texts = []
            game.buttons = []
            game.show_board = True
            game.update_player_text()
            game.texts.append(Text(f"It's your turn!", 0, 0))
            game.buttons.extend([Button('Roll', 0, 25, 40, 30), Button("Property Manager",50, 25, 165, 30), 
            Button('Trade', 225, 25, 55, 30)])
        if (self.name == "Increase"):
            if self.x == 140 and game.money_exchange[0] + 50 <= game.trade_list[0].money:
                game.money_exchange[0] += 50
            if self.x == 580 and game.money_exchange[1] + 50 <= game.trade_list[1].money:
                game.money_exchange[1] += 50
            game.update_trade_text()
        if (self.name == "Decrease"):
            if self.x == 240 and game.money_exchange[0] - 50 >= 0:
                game.money_exchange[0] -= 50
            if self.x == 680 and game.money_exchange[1] - 50 >= 0:
                game.money_exchange[1] -= 50
            game.update_trade_text()
        if (self.name == "Make Trade"):
            player, player_2, player_exchange, player_2exchange = (game.trade_list[0], game.trade_list[1], 
            game.property_exchange[0], game.property_exchange[1])

            accept = player_2.evaluate_trade(game)
            if accept:
                for property in player_exchange:
                    property.owner_rect[1] = player_2.color
                for property in player_2exchange:
                    property.owner_rect[1] = player.color
                player.properties.extend(player_2exchange)  
                player_2.properties.extend(player_exchange)  
                game.property_exchange = [[], []]      
                player.money -= game.money_exchange[0]   
                player.money += game.money_exchange[1] 

                player_2.money -= game.money_exchange[1]   
                player_2.money += game.money_exchange[0]    

                game.money_exchange = [0, 0]
                game.update_trade_text()
                
            else:
                game.rejected_offer = True
                game.update_trade_text()
            
        
        if (self.name == "Property Manager"):
            game.texts = []
            game.buttons = []
            game.update_player_text()
            game.buttons.append(Button("Back", 0, 0, 40, 40))
            game.show_board = False
            game.in_manager = True
        if (self.name == "Build"):
            if ((game.player.money - game.selected_property.building_costs) >= 0 
            and game.selected_property.current_tier != 6):
                game.selected_property.increase_tier() 
                game.player.money -= game.selected_property.building_costs 
                game.texts = []
                game.buttons = []
                game.update_player_text()
                game.buttons.append(Button("Back", 0, 0, 40, 40))
                game.selected_property.add_property_text(game.texts, game.buttons, game.player)
        if (self.name == "Sell"):
            if game.selected_property.current_tier >= 2:
                game.selected_property.current_tier -= 1
                game.player.money += game.selected_property.building_costs 
                game.texts = []
                game.buttons = []
                game.update_player_text()
                game.buttons.append(Button("Back", 0, 0, 40, 40))
                game.selected_property.add_property_text(game.texts, game.buttons, game.player)
        if (self.name == "Mortgage"):
            game.player.mortgage(game.selected_property)
            game.texts = []
            game.buttons = []
            game.selected_property.add_property_text(game.texts, game.buttons, game.player)
            game.buttons.append(Button("Back", 0, 0, 40, 40))
            game.update_player_text()
        if (self.name == "Lift Mortgage"):
            game.player.unmortgage(game.selected_property)
            game.texts = []
            game.buttons = []
            game.buttons.append(Button("Back", 0, 0, 40, 40))
            game.selected_property.add_property_text(game.texts, game.buttons, game.player)
            game.update_player_text()
        if (self.name == "Turn"):
            game.buttons.clear()
            player = game.players[game.currentTurn]
            player.roll(game)
