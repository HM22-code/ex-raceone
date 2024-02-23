import pygame
import configs
from interfaces.state import State
from objects.background import Background
from objects.slider import Slider


class Option(State):
    """ Option state class

    Args:
        State (_type_): state
    """
    
    def __init__(self, game):
        super().__init__(game)
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        self.sliders = []
        self.create_sliders()
        # Create Game objects
        self.sprites.add(Background())
        
    def create_sliders(self):
        slider = Slider((configs.SCREEN_WIDTH // 2, configs.SCREEN_HEIGHT // 2), (300, 40), 0.5, 0, 100)
        self.sprites.add(slider)
        self.sliders.append(slider)
        
    def run(self):
        # Draw
        self.sprites.draw(self.game.screen)
        # Update
        self.sprites.update()
        
    def handle_event(self, event):
        mx, my = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.set_state(self.game.get_previous_state())
        for slider in self.sliders:
            if slider.rect.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    slider.move_slider((mx, my))
            
    def enter_state(self):
        super().enter_state()
    
    def exit_state(self):
        super().exit_state()    
        
    def process_input(self):
        super().process_input()
    
    def render(self):
        super().render()
    
    def update(self):
        super().update()