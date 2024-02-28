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
        self.create_sliders()
        # Create Game objects
        self.sprites.add(Background())
        
    def create_sliders(self):
        self.music_slider = Slider((configs.SCREEN_WIDTH // 2, configs.SCREEN_HEIGHT // 4), (configs.SLIDER_WIDTH, configs.SLIDER_HEIGHT), self.game.music_volume, configs.SLIDER_MIN, configs.SLIDER_MAX)
        self.sound_slider = Slider((configs.SCREEN_WIDTH // 2, configs.SCREEN_HEIGHT // 2), (configs.SLIDER_WIDTH, configs.SLIDER_HEIGHT), self.game.sound_volume, configs.SLIDER_MIN, configs.SLIDER_MAX)
        self.sprites.add(self.music_slider)
        self.sprites.add(self.sound_slider)
        
    def render(self):
        self.sprites.draw(self.game.screen)
    
    def update(self, dt):
        self.sprites.update(dt)
        
    def handle_event(self, event):
        mx, my = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.set_state(self.game.get_previous_state())
        if self.music_slider.rect.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.music_slider.move_slider((mx, my))
                self.game.music_volume = self.music_slider.get_value()
        if self.sound_slider.rect.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sound_slider.move_slider((mx, my))
                self.game.music_volume = self.sound_slider.get_value()
            
    def enter_state(self):
        return super().enter_state()
    
    def exit_state(self):
        return super().exit_state()