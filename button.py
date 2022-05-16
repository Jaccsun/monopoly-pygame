from text import Text
import pygame

class Button:
    def __init__(self, text, x, y, x_size, y_size):
        self.name = text
        self.text = Text(text, x, y, color=(255, 255, 255))
        self.rect = pygame.Rect(x, y, x_size, y_size)