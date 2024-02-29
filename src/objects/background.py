import pygame.sprite
import utils.assets
from enums.layers import Layers

class Background(pygame.sprite.Sprite):
    """ Background sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, *groups):
        super().__init__(*groups)
        self._layer = Layers.BACKGROUND
        self.image = utils.assets.get_sprite("background-0.png")
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.frame_index = 0
        self.animation = []
        self.import_animations()
        
    def import_animations(self):
        for i in range(0, 48):
            self.animation.append(utils.assets.get_sprite("background-"+str(i)+".png"))
        
    def animate(self, fps, loop=True):
        self.frame_index += fps
        if self.frame_index >= len(self.animation) - 1:
            if loop:
                self.frame_index = 0
            else:
                self.frame_index = len(self.animation) - 1
        self.image = self.animation[int(self.frame_index)]
    
    def update(self, dt):
        self.animate(15 * dt)