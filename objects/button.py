import pygame.sprite
from layers import Layers
import configs

class Button(pygame.sprite.Sprite):
    
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BUTTON_INACTIVE = RED
    BUTTON_ACTIVE = GREEN
    BUTTON_WIDTH = 200
    BUTTON_HEIGHT = 50
    BUTTON_SPACING = 20
    
    def __init__(self, x, y, width, height, text, *groups):
        self._layer = Layers.UI
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text = text
        self.font = pygame.font.SysFont(None, 40)
        super().__init__(*groups)

    def draw(self, screen, is_active):
        pygame.draw.rect(
            screen, self.BUTTON_ACTIVE if is_active else self.BUTTON_INACTIVE, self.rect
        )
        text_surface = self.font.render(self.text, True, self.WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def clicked(self):
        if self.text == "Start":
            print("Start the game!")
        elif self.text == "Options":
            print("Options menu")
        elif self.text == "Credits":
            print("Credits")
        elif self.text == "Quit":
            pygame.quit()
            quit()
