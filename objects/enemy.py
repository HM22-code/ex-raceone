import pygame.sprite
import utils.assets
from enums.layers import Layers

class Enemy(pygame.sprite.Sprite):
    """ Enemy sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.layer = Layers.OBSTACLE
        self.image = utils.assets.get_sprite("enemy-0.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.frame_index = 0
        self.frame_number = 5
        self.velocity = 2
        self.animation = []
        self.import_animations()
        
    def import_animations(self):
        """ Import animation frames
        """
        for i in range(0, self.frame_number):
            self.animation.append(utils.assets.get_sprite("enemy-"+str(i)+".png"))
    
    def animate(self, fps, loop=True):
        """ Play animation
        """
        self.frame_index += fps
        if self.frame_index >= len(self.animation) - 1:
            if loop:
                self.frame_index = 0
            else:
                self.frame_index = len(self.animation) - 1
        self.image = self.animation[int(self.frame_index)]
        
    def update(self, dt):
        self.rect.x -= self.velocity
        if self.rect.right <= 0:
            self.kill()
        self.animate(10 * dt, True)