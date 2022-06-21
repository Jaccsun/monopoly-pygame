import pygame
from player import Player
from board.space import Monopoly_Space
from cpu import CPU

# Trade manager for the game.
class TradeSystem:

    def __init__(self) -> None:

        self.turnedOn = False

        self.current_trade = 1
        self.tradeRecipient = self.PLAYER_LIST[self.current_trade]

        self.leftPlayer, self.rightPlayer = None 
        self.tradeParticipants = [self.leftPlayer, self.rightPlayer]

        # Exchange windows
        self.moneyExchange = []
        self.propertyExchange = [[],[]]
        
        # Visual representation of trade windows
        self.window_1, self.window_2 = (
            pygame.Rect(20, 200, 400, 400), 
            pygame.Rect(450, 200, 400, 400)
        )

    # Advances the trade to the next player.
    # Follow TRADE_LIST order so it is constant.
    def change_trade_recipient(self):
        print("test")

    # Executes the exchange between two players and rightPlayer can be given 
    # as arguments, or will default to what is. leftPlayer cannot be a CPU
    def exchange(self, tradeParticipants : list[Player] = None, 
    moneyExchange : list[int] = None, 
    propertyExchange : list[Monopoly_Space]=None, 
    overrideEvaluation : bool =False):

        if not tradeParticipants:
            tradeParticipants = self.tradeParticpants
        if not moneyExchange:
            moneyExchange = self.moneyExchange
        if not propertyExchange:
            propertyExchange = self.propertyExchange

        leftPlayer = tradeParticipants[0]
        rightPlayer = tradeParticipants[1]

        leftMoneyExchange = moneyExchange[0]
        rightMoneyExchange = moneyExchange[1]

        leftPropertyExchange = propertyExchange[0]
        rightPropertyExchange = propertyExchange[1]

        leftAccept = True
        rightAccept = True

        # Players evaluate trades ---- 
        if type(leftPlayer) is CPU:
            leftAccept = leftPlayer.evaluate_trade()
        if type(rightPlayer) is CPU:
            rightAccept = rightPlayer.evaluate_trade()

        if (leftAccept and rightAccept) or overrideEvaluation:   

            leftPlayer.money -= leftMoneyExchange  
            leftPlayer.money += rightMoneyExchange

            rightPlayer.money -= rightMoneyExchange 
            rightPlayer.money += leftMoneyExchange 

            for property in leftPropertyExchange:
                property.owner_rect[1] = rightPlayer.color
            for property in rightPropertyExchange:
                property.owner_rect[1] = leftPlayer.color
            leftPlayer.properties.extend(rightPropertyExchange)  
            rightPlayer.properties.extend(leftPropertyExchange)  

            self.moneyExchange.clear()
            self.moneyExchange.extend([0, 0])
            self.propertyExchange.clear()
            self.propertyExchange.extend[[], []]
            # game.update_trade_text()
            
        else:
            print("test")
            # game.rejected_offer = True
            # game.update_trade_text()

    # Handles what happens when a property in the trade window is clicked on.
    # Entirely depends on context.
    def handle_property_click(self, clickedProperty : Monopoly_Space):
        
        i = 0
        done = False
                
        # ADD TO TRADE WINDOW
        if property_list is self.property_exchange[0]:
            self.trade_list[0].properties.append(p_2)
            self.property_exchange[0].remove(p_2)
            done = True
            self.rejected_offer = False
        if property_list is self.property_exchange[1]:
            self.trade_list[1].properties.append(p_2)
            self.property_exchange[1].remove(p_2)
            done = True
            self.rejected_offer = False
        # REMOVE FROM TRADE WINDOW
        if done is not True:
            for player in self.trade_list:
                properties = player.properties
                for p in properties:
                    card_rect = p.card.rect
                    
                    mouse_over_card = (card_rect.x <= mouse[0] <= card_rect.x + card_rect.width and
                    card_rect.y <= mouse[1] <= card_rect.y + card_rect.height)
                    if mouse_over_card:
                        if player is self.trade_list[0]:
                            self.property_exchange[0].append(p)
                            self.trade_list[0].properties.remove(p)
                            self.rejected_offer = False
                        if player is self.trade_list[1]:
                            self.property_exchange[1].append(p)
                            self.trade_list[1].properties.remove(p)
                            self.rejected_offer = False
                    i += 1
                self.update_trade_text()
    def _find_trade_window(self, property : Monopoly_Space):
        print("test")
    
