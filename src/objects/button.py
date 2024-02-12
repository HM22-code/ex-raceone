import pygame.sprite
from layers import Layers
import configs
from objects.text import Text

class Button(pygame.sprite.Sprite):
    
    def __init__(self, x, y, width, height, text, action, *groups):
        super().__init__(*groups)
        self._layer = Layers.UI
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text = text
        self.text_object = Text(self.text)
        self.action = action
        self.active = False
        
    def update(self):
        self.update_hover()
        
    def update_hover(self):
        if self.active:
            self.image.fill((50, 50, 255))
        else:
            self.image.fill((0, 0, 255))
        self.image.blit(self.text_object.image, self.text_object.image.get_rect(center = self.image.get_rect().center))           

