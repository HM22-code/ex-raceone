import pygame.sprite
import assets
import configs
from layer import Layer

class Player(pygame.sprite.Sprite):
    
    def __init__(self, *groups):
        self._layer = Layer.PLAYER
        self.image = assets.get_sprite("player")
        self.rect = self.image.get_rect(bottomleft=(50, configs.SCREEN_HEIGHT-20))
        super().__init__(*groups)