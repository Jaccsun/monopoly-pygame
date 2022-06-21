import pygame
from game import Game
def main():
    
    game = Game()
    run = True
    while run:
        game.clock.tick(game.FPS)
        mouse = pygame.mouse.get_pos()
        events = pygame.event.get()
        pass_event = None
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass_event = event
                if game.in_manager:
                    game.handle_click_definition(mouse)
                elif game.show_board is False:
                    game.handle_click_card(mouse)  

        game.handle_button_logic(mouse, pass_event)
        game.draw_window()

main()
pygame.quit()