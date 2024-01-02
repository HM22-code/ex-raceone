import pygame
import configs
import assets
from objects.background import Background
from objects.floor import Floor

def main():
    pygame.init()
    screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    assets.load_sprites()
    pygame.display.set_icon(assets.get_sprite("icon"))
    pygame.display.set_caption(configs.TITLE)
    sprites = pygame.sprite.LayeredUpdates()
    Background(0, sprites)
    Background(1, sprites)
    Floor(0, sprites)
    Floor(1, sprites)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        sprites.draw(screen)
        sprites.update()
        pygame.display.flip()
        clock.tick(configs.FPS)
        
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
