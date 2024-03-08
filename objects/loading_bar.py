import pygame

class LoadingBar(pygame.sprite.Sprite):
    """ LoadingBar sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, x, y, width, height, max_value):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.bar_color = (0, 255, 0)
        self.background_color = (50, 50, 50)
        self.value = 0
        self.max_value = max_value

    def update(self, dt):
        # Calculate width of the bar based on the current value and max value
        bar_width = int(self.rect.width * (self.value / self.max_value))
        # Draw the background of the loading bar
        self.image.fill(self.background_color)
        # Draw the loading bar itself
        pygame.draw.rect(self.image, self.bar_color, (0, 0, bar_width, self.rect.height))

    def set_value(self, value):
        # Set the value of the loading bar
        self.value = value
        if self.value < 0:
            self.value = 0
        elif self.value > self.max_value:
            self.value = self.max_value