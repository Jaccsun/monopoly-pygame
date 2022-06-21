from board.space import Monopoly_Space
from window.button import Button
from window.text import Text
class PropertyManager: 
    def __init__(self) -> None:
        self.turnedOn = False
        self.selected_property = None

    def display_prop_details(self, property : Monopoly_Space, texts, buttons):
        if not property.type == "property":
            raise TypeError("Space is not of property type.")
        if property.current_tier == -1:
            buttons.append(Button("Lift Mortgage", 20, 550, 80, 40))
        else:
            if self.current_tier == 0 or self.current_tier == 1:
                buttons.append(Button("Mortgage", 20, 550, 80, 40))
            if self.is_monopoly(property):
                buttons.extend([Button("Build", 20, 610, 80, 40), 
                Button("Sell", 20, 670, 80, 40)])
                if self.current_tier == 6:
                    texts.append(Text(f"1 hotel", 300, 500))
                else:
                    texts.append(Text(f"{self.current_tier - 1} houses", 300, 500))
        texts.append(Text(f"{self.space_name}:", 20, 500)) 
        
    
    def get_prop_details():
        print('test')


