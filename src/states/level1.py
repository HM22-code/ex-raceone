import pygame
import utils.assets
from objects.player import Player
from objects.background import Background
from classes.state import State

class Level1(State):
    """ Level state class

    Args:
        State (_type_): state
    """
    
    def __init__(self, game):
        super().__init__(game)
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        # Create Game objects
        Background(self.sprites)
        Player(self.sprites)
        # Background music
        self.music = utils.assets.get_audio("level1")
        self.music.set_volume(0.3)
    
    def run(self):
        # Draw
        self.sprites.draw(self.game.screen)
        # Update
        self.sprites.update()
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.set_state(self.game.get_previous_state())
        
    def enter_state(self):
        self.music.play(loops = -1)
    
    def exit_state(self):
        self.music.stop()