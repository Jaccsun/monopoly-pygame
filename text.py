import string
import pygame
class Text:
    def __init__(self, font, size, text, color, x, y):
        font = pygame.font.SysFont(font, size)
        self.surface = font.render(text, True, color)
        self.x = x
        self.y = y

    def draw(self, WIN):
        WIN.blit(self.surface, (self.x, self.y))