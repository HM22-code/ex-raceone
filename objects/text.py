import pygame.sprite
import utils.assets
from enums.layers import Layers

class Text(pygame.sprite.Sprite):
    """ Text sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, x: int, y: int, text: str, font_name: str, font_size: int, color: pygame.color.Color, *groups):
        """ Constructor

        Args:
            x (int): x position
            y (int): y position
            text (str): text to render
            font_name (str): text font name
            font_size (int): text font size
            color (pygame.color.Color): text color
        """
        super().__init__(*groups)
        self._layer = Layers.UI
        self.text = text
        self.antialias = True
        self.color = color
        self.font = utils.assets.load_font(font_name, font_size)
        self.image = self.font.render(self.text, self.antialias, self.color)
        self.rect = self.image.get_rect(center=(self.image.get_rect().center))
        self.rect.x = x
        self.rect.y = y
        
    def rerender(self):
        """ Rerender text surface with text property
        """
        self.image = self.image = self.font.render(self.text, self.antialias, self.color)
        
    def update(self, dt):
        self.rerender()