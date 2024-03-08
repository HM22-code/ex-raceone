import pygame
import configs
import asyncio
from interfaces.state import State
from enums.events import Events
import utils.assets
import sys, platform
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
        if sys.platform == "emscripten":
            self.screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
        else:
            self.screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT), pygame.FULLSCREEN|pygame.SCALED)
        # Screen options
        pygame.display.set_icon(utils.assets.load_sprite("favicon.png"))
        pygame.display.set_caption(configs.TITLE)
        # Clock to control FPS
        self.clock = pygame.time.Clock()
        self.music_volume = configs.MUSIC_VOLUME
        self.sound_volume = configs.SOUND_VOLUME
        # Init game stats
        self.score = 0
        self.life = 3
        # Events timer
        pygame.time.set_timer(Events.ENEMY, 750)
        # Init Game state manager
        self.init_state()
        
    def init_state(self):
        """ Init state
        """
        self.previous_state = None
        self.current_state = Boot(self)
        self.current_state.enter_state()
        
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
    
    def set_state(self, state: State):
        """ Change current state

        Args:
            state (_type_): state
        """
        self.previous_state = self.current_state
        self.previous_state.exit_state()
        self.current_state = state
        self.current_state.enter_state()
        
    def fadein(self):
        """ Fade screen
        """
        fade = pygame.Surface((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
        fade.fill(pygame.color.Color("black"))
        for alpha in range(0, 256, 1):
            fade.set_alpha(alpha)
            self.screen.blit(fade, (0, 0))
            pygame.display.update(fade.get_rect())
            pygame.time.delay(3)
    
    async def run(self):
        """ Game loop
        """
        while self.running:
            dt = self.clock.tick(configs.FPS)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                self.get_current_state().handle_event(event)
            self.get_current_state().render()
            self.get_current_state().update(dt)
            pygame.display.flip()
            await asyncio.sleep(0)
              
    def quit(self):
        """ Quit game program
        """
        self.running = False
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    asyncio.run(game.run())
