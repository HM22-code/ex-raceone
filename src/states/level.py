import pygame
from objects.parallax_background import ParallaxBackground
from objects.parallax_layer import ParallaxLayer
import utils.assets
from objects.player import Player
from interfaces.state import State

class Level(State):
    """ Level state class

    Args:
        State (_type_): state
    """
    
    def __init__(self, game):
        super().__init__(game)
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        # Create Game objects
        self.sprites.add(ParallaxBackground(0))
        self.sprites.add(ParallaxLayer(2, 0))
        self.sprites.add(ParallaxLayer(2, 1))
        self.sprites.add(ParallaxLayer(3, 0))
        self.sprites.add(ParallaxLayer(3, 1))
        self.sprites.add(ParallaxLayer(4, 0))
        self.sprites.add(ParallaxLayer(4, 1))
        self.player = Player(self.sprites)
        self.sprites.add(self.player)
        # Background music
        self.music = utils.assets.get_audio("level1.wav")
        self.shoot_sound = utils.assets.get_audio("sfx_wpn_laser8.wav")
    
    def render(self):
        self.sprites.draw(self.game.screen)
    
    def update(self, dt):
        self.sprites.update(dt)
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.set_state(self.game.get_previous_state())
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.player.shoot()
            self.shoot_sound.play()
        
    def enter_state(self):
        self.shoot_sound.set_volume(self.game.sound_volume)
        self.music.set_volume(self.game.music_volume)
        self.music.play(loops = -1)
    
    def exit_state(self):
        self.music.stop()