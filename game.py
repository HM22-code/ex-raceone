import pygame
import configs
import assets
from objects.game_state_manager import GameStateManager

class Game():
    
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        
        # Create the screen
        self.screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
        
        # Loading assets
        assets.load_sprites()
        assets.load_audios()
        
        # Screen options
        pygame.display.set_icon(assets.get_sprite("icon"))
        pygame.display.set_caption(configs.TITLE)
        
        # Clock to controll FPS
        self.clock = pygame.time.Clock()
        
        # Init Game state manager
        self.game_state_manager = GameStateManager(self.screen)
    
    def run(self):
        # Game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

            # State
            self.game_state_manager.get_current_state().run()
            
            # Refresh the screen
            pygame.display.flip()
            
            # Control FPS
            self.clock.tick(configs.FPS)
            
        pygame.quit()
        quit()

if __name__ == "__main__":
    Game().run()
