import pygame
import configs
from interfaces.state import State
from objects.background import Background
from objects.slider import Slider
from objects.text import Text

class Option(State):
    """ Option state class

    Args:
        State (_type_): state
    """
    
    def __init__(self, game):
        super().__init__(game)
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        # Create Game objects
        self.sprites.add(Background())
        # Adding sliders
        self.sliders = []
        self.selected_slider = 0
        self.create_sliders()
        
    def create_sliders(self):
        self.font = "bit.ttf"
        self.music_text = Text(configs.SCREEN_WIDTH // 2 - 50, configs.SCREEN_HEIGHT // 8, "Musics :", self.font, 15, pygame.color.Color("white"))
        self.music_slider = Slider((configs.SCREEN_WIDTH // 2, configs.SCREEN_HEIGHT // 4), (configs.SLIDER_WIDTH, configs.SLIDER_HEIGHT), self.game.music_volume, configs.SLIDER_MIN, configs.SLIDER_MAX)
        self.sound_text = Text(configs.SCREEN_WIDTH // 2 - 50, configs.SCREEN_HEIGHT // 2.6, "Sounds :", self.font, 15, pygame.color.Color("white"))
        self.sound_slider = Slider((configs.SCREEN_WIDTH // 2, configs.SCREEN_HEIGHT // 2), (configs.SLIDER_WIDTH, configs.SLIDER_HEIGHT), self.game.sound_volume, configs.SLIDER_MIN, configs.SLIDER_MAX)
        self.sliders.append(self.music_slider)
        self.sliders.append(self.sound_slider)
        self.sprites.add(self.music_text)
        self.sprites.add(self.music_slider)
        self.sprites.add(self.sound_text)
        self.sprites.add(self.sound_slider)
    
    def change_selection(self, direction):
        self.selected_slider = (self.selected_slider + direction) % len(self.sliders)
        for i, slider in enumerate(self.sliders):
            slider.active = (i == self.selected_slider)
        
    def render(self):
        self.sprites.draw(self.game.screen)
    
    def update(self, dt):
        self.sprites.update(dt)
        
    def handle_event(self, event):
        self.handle_slider_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.change_selection(1)
            elif event.key == pygame.K_UP:
                self.change_selection(-1)
            elif event.key == pygame.K_RIGHT:
                if self.selected_slider == 0:  # Music slider
                    self.music_slider.set_slider(1)
                    self.game.music_volume = self.music_slider.get_value()
                elif self.selected_slider == 1:  # Sound slider
                    self.sound_slider.set_slider(1)
                    self.game.sound_volume = self.sound_slider.get_value()
            elif event.key == pygame.K_LEFT:
                if self.selected_slider == 0:  # Music slider
                    self.music_slider.set_slider(-1)
                    self.game.music_volume = self.music_slider.get_value()
                elif self.selected_slider == 1:  # Sound slider
                    self.sound_slider.set_slider(-1)
                    self.game.sound_volume = self.sound_slider.get_value()
                
    def handle_slider_event(self, event):
        mx, my = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.set_state(self.previous_state)
        if self.music_slider.rect.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.music_slider.move_slider((mx, my))
                self.game.music_volume = self.music_slider.get_value()
        if self.sound_slider.rect.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sound_slider.move_slider((mx, my))
                self.game.sound_volume = self.sound_slider.get_value()
            
    def enter_state(self):
        return super().enter_state()
    
    def exit_state(self):
        return super().exit_state()