import pygame.sprite
from enums.layers import Layers
from objects.text import Text

class UI(pygame.sprite.Sprite):
    """ UI sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, x, y, width, height, text, *groups):
        super().__init__(*groups)
        self._layer = Layers.UI
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.score = 0
        self.life = 3
        self.weapon = 1
        self.health = 100
        self.text_object = Text(self.rect.right // 2, self.rect.bottom // 2, text, "16-bit-font.ttf", 36, pygame.color.Color("white"))