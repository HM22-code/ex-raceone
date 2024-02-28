import pygame.sprite
import utils.assets
import configs
from enums.layers import Layers

class Player(pygame.sprite.Sprite):
    """ Player sprite class

    Args:
        pygame (_type_): sprite
    """
    
    velocity = 5
    
    def __init__(self, *groups):
        super().__init__(*groups)
        self._layer = Layers.PLAYER
        self.image = utils.assets.get_sprite("player.png")
        self.rect = self.image.get_rect(bottomleft=(50, configs.SCREEN_HEIGHT-20))
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.x < configs.SCREEN_WIDTH - self.rect.width:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.y < configs.SCREEN_HEIGHT - self.rect.height:
            self.rect.y += self.velocity