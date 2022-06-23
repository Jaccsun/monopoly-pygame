from typing import Tuple
from window.text import Text
import random
import pygame

class Button:

    text: Text
    rect: pygame.rect.Rect

    # Initialize new button, if text is a string it will 
    # create a text object out of the value.
    def __init__(self, text : Text, rect : pygame.rect.Rect , 
    color=(40, 40, 40), colorOver = (90, 90, 90), event = None,
    eventArgs : list = [], eventClearTextAndButton = True, eventUpdatePlayerText = True):
        if type(text) is str:
            self.text= Text(text, (rect.x, rect.y))
        elif type(text) is Text:
            self.text = text 
        else:
            raise TypeError("Invalid text argument, "
            + "must be text object or string.")

        self.rect = rect
        self.color = color 
        self.colorOver = colorOver
        self.currentColor = color

        #-- Settings for the event that is connected to this button.

        self.event = event
        self.eventArgs = eventArgs
        self.eventClearTextAndButton = eventClearTextAndButton
        self.eventUpdatePlayerText = eventUpdatePlayerText

    # DEPRECATED
    # def run(self, game):
    #     # buy button for newly-unowned properties     
    #     if (self.text == "Buy"):
    #         game.buttons.clear()
    #         game.texts.clear()
    #         if(game.player.money - game.landed_on_space.printed_price < 0):
    #             game.texts.append(Text("You don't have enough money "
    #             f"to purchase this property.", 0, 20))
    #         else: 
    #             game.texts.append(Text(f"You have purchased "
    #             f"{str(game.landed_on_space.space_name)}!", 0, 20))
    #             game.player.buy(game.landed_on_space)
    #         game.update_player_text()
    #         game.buttons.clear()
    #         game.buttons.append(Button("next",0, 50, 70, 40))
            
    #     # dont buy property 
    #     if (self.text == "Don't Buy"): 
    #         game.buttons = []
    #         game.texts = []
    #         game.texts.append(Text(f"You decided not to buy"
    #         + f" {str(game.landed_on_space.space_name)}", 0, 20)),
    #         game.buttons = [Button("next",0, 50, 70, 40)]
    #     # pay player if landed on their property
    #     if (self.text == "Pay"):
    #         game.player.pay(game)
    #     # bankrupt properties button
    #     if (self.text == "Bankrupt"):
    #         game.buttons.clear()
    #         game.texts.clear()
    #         game.show_board = False
    #         game.texts.append(Text("Thanks for playing!", 270, 200, size=50))
    #         game.buttons.append(Button("Play again", 385, 270, 100, 50))
    #     if (self.text == "Play again"):
    #         print("test")
        

        
    #     if (self.text == "Property Manager"):
    #         game.texts = []
    #         game.buttons = []
    #         game.update_player_text()
    #         game.buttons.append(Button("Back", 0, 0, 40, 40))
    #         game.show_board = False
    #         game.in_manager = True
    #     if (self.text == "Build"):
    #         if ((game.player.money - game.selected_property.building_costs) >= 0 
    #         and game.selected_property.current_tier != 6):
    #             game.selected_property.increase_tier() 
    #             game.player.money -= game.selected_property.building_costs 
    #             game.texts = []
    #             game.buttons = []
    #             game.update_player_text()
    #             game.buttons.append(Button("Back", 0, 0, 40, 40))
    #             game.selected_property.add_property_text(game.texts, game.buttons, game.player)
    #     if (self.text == "Sell"):
    #         if game.selected_property.current_tier >= 2:
    #             game.selected_property.current_tier -= 1
    #             game.player.money += game.selected_property.building_costs 
    #             game.texts = []
    #             game.buttons = []
    #             game.update_player_text()
    #             game.buttons.append(Button("Back", 0, 0, 40, 40))
    #             game.selected_property.add_property_text(game.texts, game.buttons, game.player)
    #     if (self.text == "Mortgage"):
    #         game.player.mortgage(game.selected_property)
    #         game.texts = []
    #         game.buttons = []
    #         game.selected_property.add_property_text(game.texts, game.buttons, game.player)
    #         game.buttons.append(Button("Back", 0, 0, 40, 40))
    #         game.update_player_text()
    #     if (self.text == "Lift Mortgage"):
    #         game.player.unmortgage(game.selected_property)
    #         game.texts = []
    #         game.buttons = []
    #         game.buttons.append(Button("Back", 0, 0, 40, 40))
    #         game.selected_property.add_property_text(game.texts, game.buttons, game.player)
    #         game.update_player_text()
    #     if (self.text == "Turn"):
    #         game.buttons.clear()
    #         player = game.players[game.currentTurn]
    #         player.roll(game)
