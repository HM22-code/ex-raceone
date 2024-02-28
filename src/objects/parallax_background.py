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
    
    def __init__(self, level, index, *groups):
        super().__init__(*groups)
        self._layer = Layers.BACKGROUND
        self.index = index
        self.image = utils.assets.get_sprite("parallax-"+str(level)+"-1.png")
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH * self.index, 0))
        self.bgimage2 = utils.assets.get_sprite("parallax-"+str(level)+"-2.png")
        self.bgimage3 = utils.assets.get_sprite("parallax-"+str(level)+"-3.png")
        self.bgimage4 = utils.assets.get_sprite("parallax-"+str(level)+"-4.png")
    
    def update(self, dt):
        self.rect.x -= self.moving_speed
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH
        self.image.blit(self.bgimage2, (configs.SCREEN_WIDTH * self.index, 0))
        self.image.blit(self.bgimage3, (configs.SCREEN_WIDTH * self.index, 0))
        self.image.blit(self.bgimage4, (configs.SCREEN_WIDTH * self.index, 0))
        """
        self.image.blit(self.bgimage4, ((self.bgX3 - bg_width) - scroll * speed, 0))
        """  