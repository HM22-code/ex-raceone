import pygame
import configs
import assets
from objects.background import Background
from objects.floor import Floor

def main():
    
    #init pygame
    pygame.init()
    
    screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    '''
    pygame.display.set_icon(icon)
    pygame.display.set_caption(title)
    '''
    
    #run loop
    running = True
    
    assets.load_sprites()
    
    sprites = pygame.sprite.LayeredUpdates()
    
    Background(0, sprites)
    Background(1, sprites)
    
    Floor(0, sprites)
    Floor(1, sprites)
    
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                break
    
        screen.fill("green")
        
        sprites.draw(screen)
        sprites.update()
        
        pygame.display.flip()
        clock.tick(configs.FPS)


if __name__ == "__main__":
    main()
