import pygame.sprite
from objects.bullet import Bullet
import utils.assets
import configs
from enums.layers import Layers

class Player(pygame.sprite.Sprite):
    """ Player sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, bullets, sprites,*groups):
        super().__init__(*groups)
        self._layer = Layers.PLAYER
        self.bullets = bullets
        self.sprites = sprites
        self.image = utils.assets.get_sprite("player-1.png")
        self.rect = self.image.get_rect(topleft=(50, configs.SCREEN_HEIGHT//2))
        self.velocity = 5
        
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
                
    def shoot(self):
        bullet = Bullet(self.rect.right, self.rect.centery)
        bullet.add(self.bullets)
        bullet.add(self.sprites)