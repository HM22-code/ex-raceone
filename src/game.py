import pygame
import configs
import utils.assets
import sys
from states.boot import Boot

class Game:
    """ Game class
    """
    
    def __init__(self):
        # Init game running
        self.running = True
        # Initialize Pygame
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        # Create the screen
        self.screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT), pygame.FULLSCREEN|pygame.SCALED)
        # Screen options
        pygame.display.set_icon(utils.assets.load_sprite("icon.png"))
        pygame.display.set_caption(configs.TITLE)
        # Clock to control FPS
        self.clock = pygame.time.Clock()
        self.music = None
        self.music_volume = configs.MUSIC_VOLUME
        # Init Game state manager
        self.init_state()
        
    def init_state(self):
        """ Init state
        """
        self.current_state = Boot(self)
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
        
    def fadein(self):
        fade = pygame.Surface((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
        fade.fill((0, 0, 0))
        for alpha in range(0, 256, 1):
            fade.set_alpha(alpha)
            self.screen.blit(fade, (0, 0))
            pygame.display.update(fade.get_rect())
            pygame.time.delay(3)
    
    def process_input(self):
        """ Process input event
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            # Current state event handling
            self.get_current_state().handle_event(event)
    
    def update(self):
        """ Current state update
        """
        self.get_current_state().run()
    
    def run(self):
        """ Game loop
        """
        while self.running:
            self.process_input()
            self.update()
            pygame.display.flip()
            # Limits FPS to 60
            self.delta = self.clock.tick(configs.FPS)/1000
            
    def quit(self):
        """ Quit game program
        """
        self.running = False
        pygame.quit()
        sys.exit()
