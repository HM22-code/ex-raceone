import pygame.sprite
import configs
import assets
from enums.layers import Layers

class Text(pygame.sprite.Sprite):
    """ Text sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, text, *groups):
        super().__init__(*groups)
        self._layer = Layers.UI
        self.font = assets.load_font("16-bit-font.ttf", 36)
        self.image = self.font.render(text, True, (255, 255, 255))
        self.rect = self.image.get_rect(center=(self.image.get_rect().center))