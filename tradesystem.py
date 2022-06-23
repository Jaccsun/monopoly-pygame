import pygame
from player import Player
from board.space import MonopolySpace
from cpu import CPU
from window.button import Button
from pygame import Rect
# Trade manager for the self.
class TradeSystem:

    def __init__(self) -> None:

        self.turnedOn = False

        self.current_trade = 1

        self.leftPlayer, self.rightPlayer = None, None
        self.tradeParticipants = [self.leftPlayer, self.rightPlayer]

        # Exchange windows
        self.moneyExchange = [0, 0]
        self.propertyExchange = [[],[]]
        
        # Visual representation of trade windows
        self.window_1, self.window_2 = (
            pygame.Rect(20, 200, 400, 400), 
            pygame.Rect(450, 200, 400, 400)
        )

    # Opens the window and displays 
    def open(self, leftPlayer : Player, rightPlayer : Player,
    buttons : list[Button]):
        self.leftPlayer = leftPlayer
        self.rightPlayer = rightPlayer

        # self.moneyExchange = [0, 0]
        # self.show_board = False
        # self.current_trade = 1
        # self.tradeParticipants.extend([self.player, self.player_2])

        buttons.extend([
            Button("Next Player",Rect(790, 0, 105, 40), 
                event=self.change_trade_recipient),
            Button("Back", Rect(0, 0, 40, 40),
                event = self.needMethod),
            Button("Increase", Rect(140, 600, 75, 40),
                self.increase('left')),
            Button("Decrease", Rect(240, 600, 75, 40),
                self.decrease('left')),
            Button("Increase", Rect(580, 600, 75, 40),
                self.increase('right')),
            Button("Decrease", Rect(680, 600, 75, 40),
                self.increase('right')),
            Button("Make Trade", Rect(20, 700, 120, 50),
                self.exchange),           
        ])

    def increase(self, side : str):
        if (side == 'left' and self.moneyExchange[0] + 50 
        <= self.tradeParticipants[0].money):
                self.moneyExchange[0] += 50
        if (side == 'right' and self.moneyExchange[1] + 50 
        <= self.tradeParticipants[1].money):
                self.moneyExchange[1] += 50

    def decrease(self, side : str):
        if side == 'left' and self.moneyExchange[0] - 50 >= 0:
            self.moneyExchange[0] -= 50
        if side == 'right' and self.moneyExchange[1] - 50 >= 0:
            self.moneyExchange[1] -= 50

     # Executes the exchange between two players and rightPlayer can be given 
    # as arguments, or will default to what is. leftPlayer cannot be a CPU
    def exchange(self, tradeParticipants : list[Player] = None, 
    moneyExchange : list[int] = None, 
    propertyExchange : list[MonopolySpace]=None, 
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
            # self.update_trade_text()
            
        else:
            print("test")
            # self.rejected_offer = True
            # self.update_trade_text()


    # Advances the trade to the next player.
    def change_trade_recipient(self):
        self.moneyExchange.clear()
        self.moneyExchange.extend([0, 0])    

        self.tradeParticipants[0].properties.extend(self.propertyExchange[0])
        self.tradeParticipants[1].properties.extend(self.propertyExchange[1])
        self.propertyExchange = [[],[]]

        player = self.PLAYER_LIST[self.current_trade]
        self.tradeParticipants[1] = player    

    # Handles what happens when a property in the trade window is clicked on.
    # Entirely depends on context.
    def handle_property_click(self, clickedProperty : MonopolySpace):  
        # ADD TO TRADE WINDOW
        if clickedProperty in self.tradeParticipants[0]:
            self.propertyExchange[0].append(clickedProperty)
            self.tradeParticipants[0].properties.remove(clickedProperty)
            return None
        if clickedProperty in self.tradeParticipants[1]:
            self.propertyExchange[1].append(clickedProperty)
            self.tradeParticipants[1].properties.remove(clickedProperty)
            return None
        # REMOVE FROM TRADE WINDOW
        if clickedProperty in self.propertyExchange[0]:
            self.tradeParticipants[0].properties.append(clickedProperty)
            self.propertyExchange[0].remove(clickedProperty)
            return None
        if clickedProperty is self.propertyExchange[1]:
            self.tradeParticipants[1].properties.append(clickedProperty)
            self.propertyExchange[1].remove(clickedProperty)
            return None

    def _reset(self):
        self.moneyExchange.clear()
        self.moneyExchange.extend([0, 0])
        self.currentTrade = 1