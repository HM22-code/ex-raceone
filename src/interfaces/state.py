import pygame
import configs
from abc import ABC, abstractmethod

class State(ABC):
    """ State class for all states
    """
    
    def __init__(self, game):
        self.game = game
     
    @abstractmethod   
    def run(self):
        """ Called on every frames
        """
        pass
    
    @abstractmethod 
    def process_input(self):
        """ Called to process input event for the current state
        """
        pass
    
    @abstractmethod 
    def update(self):
        """ Called on every frames to update the current state screen
        """
        pass
    
    @abstractmethod 
    def render(self):
        """ Called on every frames to render graphics for the current state
        """
        pass
    
    @abstractmethod 
    def enter_state(self):
        """ Called when the state becomes the current state
        """
        pass
    
    @abstractmethod 
    def exit_state(self):
        """ Called when the state is no longer the current state
        """
        pass
    
    @abstractmethod 
    def handle_event(self, event):
        """ Handle event for the current state
        """
        pass
    
    @abstractmethod 
    def fadein(self):
        fade = pygame.Surface((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
        fade.fill((0, 0, 0))
        for alpha in range(0, 256, 1):
            fade.set_alpha(alpha)
            self.game.screen.blit(fade, (0, 0))
            pygame.display.update(fade.get_rect())
            pygame.time.delay(3)
    
    @abstractmethod 
    def fadeout(self):
        fade = pygame.Surface((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
        fade.fill((0, 0, 0))
        for alpha in range(255, -1, -1):
            fade.set_alpha(alpha)
            self.game.screen.blit(fade, (0, 0))
            pygame.display.update(fade.get_rect())
            pygame.time.delay(3)
            
            