import pygame
import configs
import assets
from objects.background import Background
from objects.floor import Floor
from objects.game_start_message import GameStartMessage
from objects.player import Player

def main():
    # Initialize Pygame
    pygame.init()
    
    # Create the screen
    screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
    
    # Loading assets
    assets.load_sprites()
    assets.load_audios()
    
    # Screen options
    pygame.display.set_icon(assets.get_sprite("icon"))
    pygame.display.set_caption(configs.TITLE)
    
    # Clock to controll FPS
    clock = pygame.time.Clock()
    
    # Sprite Groups
    sprites = pygame.sprite.LayeredUpdates()
    
    # Create Game objects
    Background(0, sprites)
    Background(1, sprites)
    Floor(0, sprites)
    Floor(1, sprites)
    GameStartMessage(sprites)
    Player(sprites)
    
    # Background music
    '''
    music = assets.get_audio("menu")
    music.set_volume(0.3)
    music.play(loops = -1)
    '''
    
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        # Refresh the screen
        sprites.draw(screen)
        sprites.update()
        pygame.display.flip()
        
        # Control FPS
        clock.tick(configs.FPS)
        
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
