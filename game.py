import pygamee
from setting import sttings

pygame.init()
gm_settings = settings()



screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
pygame.display.set_caption(gm_settings.caption)


running = True
while running:
    screen.fill(gm_setting.bg_color)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
    pygame.display.flip()