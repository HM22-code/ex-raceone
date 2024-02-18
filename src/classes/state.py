import pygame
import configs.screen

class State():
    """ State class for all states
    """
    
    def __init__(self, game):
        self.game = game
        
    def run(self):
        """ Called on every frames
        """
        pass
    
    def process_input(self):
        """ Called to process input event for the current state
        """
        pass
    
    def update(self):
        """ Called on every frames to update the current state screen
        """
        pass
    
    def render(self):
        """ Called on every frames to render graphics for the current state
        """
        pass
    
    def enter_state(self):
        """ Called when the state becomes the current state
        """
        pass
    
    def exit_state(self):
        """ Called when the state is no longer the current state
        """
        pass
    
    def handle_event(self, event):
        """ Handle event for the current state
        """
        pass
    
    def fadein(self):
        fade = pygame.Surface((configs.screen.SCREEN_WIDTH, configs.screen.SCREEN_HEIGHT))
        fade.fill((0, 0, 0))
        for alpha in range(0, 256, 1):
            fade.set_alpha(alpha)
            self.game.screen.blit(fade, (0, 0))
            pygame.display.update(fade.get_rect())
            pygame.time.delay(3)
            
    def fadeout(self):
        fade = pygame.Surface((configs.screen.SCREEN_WIDTH, configs.screen.SCREEN_HEIGHT))
        fade.fill((0, 0, 0))
        for alpha in range(255, -1, -1):
            fade.set_alpha(alpha)
            self.game.screen.blit(fade, (0, 0))
            pygame.display.update(fade.get_rect())
            pygame.time.delay(3)
            
            