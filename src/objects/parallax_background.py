import pygame.sprite
import utils.assets
import configs
from enums.layers import Layers

class ParallaxBackground(pygame.sprite.Sprite):
    """ ParallaxBackground sprite class

    Args:
        pygame (_type_): sprite
    """
    
    speed = 1
    
    def __init__(self, level, index, *groups):
        super().__init__(*groups)
        self._layer = Layers.BACKGROUND
        self.index = index
        self.image = utils.assets.get_sprite("parallax-"+str(level)+"-1.png")
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH * self.index, 0))
        self.bg_images = []
        self.bgimage2 = utils.assets.get_sprite("parallax-"+str(level)+"-2.png")
        self.bgimage3 = utils.assets.get_sprite("parallax-"+str(level)+"-3.png")
        self.bgimage4 = utils.assets.get_sprite("parallax-"+str(level)+"-4.png")
        self.bg_images.append(self.bgimage2)
        self.bg_images.append(self.bgimage3)
        self.bg_images.append(self.bgimage4)
    
    def update(self, dt):
        self.rect.x -= self.speed
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH
        for i in self.bg_images:
            self.image.blit(i, ((configs.SCREEN_WIDTH * self.index) - self.speed, 0))