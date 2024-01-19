import pygame
import configs
import assets
import sys
from states.start import Start

class Game():
    """ Game class
    """
    
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
        self.init_state()
        
    def init_state(self):
        """ Init state
        """
        self.current_state = Start(self)
        self.current_state.enter_state()
        self.previous_state = None
        
    def get_current_state(self):
        """ Get current state

        Returns:
            _type_: state
        """
        return self.current_state
    
    def get_previous_state(self):
        """ Get previous state

        Returns:
            _type_: state
        """
        return self.previous_state
    
    def set_state(self, state):
        """ Change the current state

        Args:
            state (_type_): state
        """
        self.previous_state = self.current_state
        self.previous_state.exit_state()
        self.current_state = state
        self.current_state.enter_state()
    
    def run(self):
        # Game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
            # States
            self.get_current_state().run()
            # Refresh the screen
            pygame.display.flip()
            # Control FPS
            self.clock.tick(configs.FPS)
        pygame.quit()
        sys.exit()
