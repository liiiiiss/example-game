import pygame
from settings import settings

def run_game():
    pygame.init()
    gm.settings = settings()
    
    screen = pygame.display.set_mode[(gm_settings.screen_width, gm_settings.screen_heigh])
    
    running = True
    while running:
        screen.fill(gm_settings.bg_color)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        pygame.display.flip()
    
    pygame.quit()
        
    
                