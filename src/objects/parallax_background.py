import pygame.sprite
import utils.assets
import configs
from enums.layers import Layers

class ParallaxBackground(pygame.sprite.Sprite):
    """ ParallaxBackground sprite class

    Args:
        pygame (_type_): sprite
    """
    
    moving_speed = 2
    
    def __init__(self, *groups):
        super().__init__(*groups)
        self._layer = Layers.BACKGROUND
        self.image = utils.assets.get_sprite("background")
        self.rect = self.image.get_rect(topleft=(0, 0))
    
    def update(self):
        self.rect.x -= self.moving_speed
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH    
        # self.image.blit(self.bgimage1, (self.bgX1, 0))
        # self.image.blit(self.bgimage2, (self.bgX2, 0))
        # self.image.blit(self.bgimage3, ((self.bgX3 - bg_width) - scroll * speed, 0))