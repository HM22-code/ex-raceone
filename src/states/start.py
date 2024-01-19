import pygame
import assets
from states.level import Level
from objects.background import Background
from objects.floor import Floor
from objects.game_start_message import GameStartMessage
from classes.state import State

class Start(State):
    """ Start state class

    Args:
        State (_type_): state
    """
    
    def __init__(self, game):
        super().__init__(game)
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        # Create Game objects
        Background(0, self.sprites)
        Background(1, self.sprites)
        Floor(0, self.sprites)
        Floor(1, self.sprites)
        GameStartMessage(self.sprites)
        # Background music
        self.music = assets.get_audio("menu")
        self.music.set_volume(0.3)
    
    def run(self):
        # Input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.game.set_state(Level(self.game))
        # Draw
        self.sprites.draw(self.game.screen)
        # Update
        self.sprites.update()
        
    def enter_state(self):
        self.music.play(loops = -1)
    
    def exit_state(self):
        self.music.stop()