import pygame.sprite
import utils.assets
import configs
from enums.layers import Layers

class ParallaxLayer(pygame.sprite.Sprite):
    """ ParallaxLayer sprite class

    Args:
        pygame (_type_): sprite
    """
    
    speed = 16
    
    def __init__(self, level, index, *groups):
        super().__init__(*groups)
        self._layer = Layers.BACKGROUND
        self.image = utils.assets.get_sprite("parallax-"+str(level)+".png")
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH * index, 0))
        self.level = level
    
    def update(self, dt):
        self.rect.x -= (self.speed/self.level)
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH