import pygame.sprite
from enums.layers import Layers
from objects.text import Text

class Button(pygame.sprite.Sprite):
    
    MOUSEHOVER = pygame.USEREVENT + 1
    
    def __init__(self, x, y, width, height, text, action, *groups):
        super().__init__(*groups)
        self._layer = Layers.UI
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text_object = Text(self.rect.right // 2, self.rect.bottom // 2, text, "16-bit-font.ttf", 36, pygame.color.Color("white"))
        self.action = action
        self.active = True
        
    def update(self, dt):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.event.post(pygame.event.Event(self.MOUSEHOVER))
            self.image.fill(pygame.color.Color("darkorchid1"))
        else:
            self.image.fill(pygame.color.Color("darkorchid2"))
        self.image.blit(self.text_object.image, self.text_object.image.get_rect(center = self.image.get_rect().center))
                 

