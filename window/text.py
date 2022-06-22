import string
from typing import Tuple
import pygame
class Text:

    # Create new text object. Position can be provided 
    # as Tuple of (x, y) coordinates or individually specified 
    # with x and y parameters. x and y parameters override 
    # the tuple values.
    def __init__(self, text, position : Tuple[int, int] = (0, 0), 
    color : Tuple[int, int, int] = (255, 255, 255),
    size=25, font='arial', x : int = 0, y : int = 0):
        font = pygame.font.SysFont(font, size)
        self.surface = font.render(text, True, color)
        self.text_string = text
        

        self.x = position[0]
        self.y = position[1]

        if x != 0: 
            self.x = x
        if y != 0:
            self.y = y

        self.position = [self.x, self.y]

    def draw(self, WIN):
        WIN.blit(self.surface, self.position)