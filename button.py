from text import Text
import pygame

class Button:

    name: str 
    text: Text
    rect: pygame.rect.Rect

    def __init__(self, text : str, x : int, y : int, x_size : int, y_size):
        self.name = text
        self.x, self.y, self.x_size, self.y_size  = x, y, x_size, y_size
        self.text = Text(text, x, y, color=(255, 255, 255))
        self.rect = pygame.Rect(x, y, x_size, y_size)