import pygame
from game import Game
def main():
    
    game = Game()
    run = True
    while run:
        game.clock.tick(game.FPS)
        events = pygame.event.get()
        mouseDown = None
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = event
        game.handle_mouse_position_event(mouseDown)
        game.draw()

main()
pygame.quit()