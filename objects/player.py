import pygame.sprite
import assets
import configs
from layer import Layer

class Player(pygame.sprite.Sprite):
    
    velocity = 5
    
    def __init__(self, *groups):
        self._layer = Layer.PLAYER
        self.image = assets.get_sprite("player")
        self.rect = self.image.get_rect(bottomleft=(50, configs.SCREEN_HEIGHT-20))
        super().__init__(*groups)
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.x < configs.SCREEN_WIDTH - self.rect.width:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.y < configs.SCREEN_HEIGHT - self.rect.height:
            self.rect.y += self.velocity