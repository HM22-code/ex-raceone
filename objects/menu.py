import pygame.sprite
from layers import Layers
import configs
from objects.button import Button

class Menu(pygame.sprite.Sprite):
    
    BUTTON_WIDTH = 200
    BUTTON_HEIGHT = 50
    BUTTON_SPACING = 20
    active_button = 0
    
    def __init__(self, *groups):
        super().__init__(*groups)
        self._layer = Layers.BACKGROUND
        self.image = pygame.Surface((500, 500))
        self.rect = self.image.get_rect()
        self.buttons = []
        self.button_sprites = pygame.sprite.Group()
        self.create_buttons()
        
    def create_buttons(self):
        button_texts = ["Start", "Options", "Credits", "Quit"]
        button_total_height = len(button_texts) * (self.BUTTON_HEIGHT + self.BUTTON_SPACING)
        starting_y = (configs.SCREEN_HEIGHT - button_total_height) // 2

        for text in button_texts:
            button = Button(
                (configs.SCREEN_WIDTH - self.BUTTON_WIDTH) // 2,
                starting_y,
                self.BUTTON_WIDTH,
                self.BUTTON_HEIGHT,
                text,
            )
            self.buttons.append(button)
            self.button_sprites.add(button)
            starting_y += self.BUTTON_HEIGHT + self.BUTTON_SPACING

    def draw_buttons(self, screen, active_button):
        for i, button in enumerate(self.buttons):
            button.draw(screen, active_button == i)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.active_button = (self.active_button + 1) % len(self.buttons)
            elif event.key == pygame.K_UP:
                self.active_button = (self.active_button - 1) % len(self.buttons)
            elif event.key == pygame.K_RETURN:
                self.buttons[self.active_button].clicked()

    def update(self):
        self.active_button = 0