import pygame.sprite
import utils.assets
from enums.layers import Layers

class Drone(pygame.sprite.Sprite):
    
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.layer = Layers.OBSTACLE
        self.image = utils.assets.get_sprite("drone-idle-0.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.frame_index = 0
        self.frame_number = 4
        self.velocity = 5
        self.animation = []
        self.import_animations()
        
    def import_animations(self):
        for i in range(0, self.frame_number - 1):
            self.animation.append(utils.assets.get_sprite("drone-idle-"+str(i)+".png"))
    
    def animate(self, fps, loop=True):
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
        self.animate(15 * dt, True)