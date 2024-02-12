import pygame
import configs

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
        # TODO: Process event input
        pass
    
    def update(self):
        # TODO: Process update
        pass
    
    def render(self):
        # TODO: Process render
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
        fade = pygame.Surface((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
        fade.fill((0, 0, 0))
        for alpha in range(0, 255, 1):
            fade.set_alpha(alpha)
            self.game.screen.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(3)