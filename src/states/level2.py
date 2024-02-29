import pygame
from objects.parallax_background import ParallaxBackground
import utils.assets
from objects.player import Player
from interfaces.state import State

class Level2(State):
    """ Level state class

    Args:
        State (_type_): state
    """
    
    def __init__(self, game):
        super().__init__(game)
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        # Create Game objects
        self.sprites.add(ParallaxBackground(2, 0))
        self.sprites.add(ParallaxBackground(2, 1))
        self.player = Player(self.sprites)
        self.sprites.add(self.player)
        # Background music
        self.music = utils.assets.get_audio("level2.wav")
        
    def render(self):
        self.sprites.draw(self.game.screen)
    
    def update(self, dt):
        self.sprites.update(dt)
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.set_state(self.game.get_previous_state())
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.player.shoot()
        
    def enter_state(self):
        self.music.set_volume(self.game.music_volume)
        self.music.play(loops = -1)
    
    def exit_state(self):
        self.music.stop()