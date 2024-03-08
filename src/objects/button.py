import pygame.sprite
from enums.layers import Layers
from objects.text import Text
from enums.events import Events

class Button(pygame.sprite.Sprite):
    """ Button sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, x, y, width, height, text, action, *groups):
        super().__init__(*groups)
        self._layer = Layers.UI
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text_object = Text(self.rect.right // 2, self.rect.bottom // 2, text, "bit.ttf", 15, pygame.color.Color("white"))
        self.action = action
        self.active = False
        
    def update(self, dt):
        if self.rect.collidepoint(pygame.mouse.get_pos()) or self.active:
            pygame.event.post(pygame.event.Event(Events.MOUSEHOVER))
            self.image.fill(pygame.color.Color("#9241f3"))
        else:
            self.image.fill(pygame.color.Color("#6110a2"))
        self.image.blit(self.text_object.image, self.text_object.image.get_rect(center = self.image.get_rect().center))
                 

