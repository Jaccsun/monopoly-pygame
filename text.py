import string
import pygame
class Text:
    def __init__(self, text, x=0, y=0, color=(0, 0, 0), size=25, font='arial'):
        font = pygame.font.SysFont(font, size)
        self.surface = font.render(text, True, color)
        self.x = x
        self.y = y

    def draw(self, WIN):
        WIN.blit(self.surface, (self.x, self.y))