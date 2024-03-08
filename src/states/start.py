import pygame
import utils.assets
import sys, platform
import configs
from objects.button import Button
from states.ending import Ending
from objects.background import Background
from objects.title import Title
from interfaces.state import State
from states.level import Level
from states.option import Option

class Start(State):
    """ Start state class

    Args:
        State (_type_): state
    """
    
    def __init__(self, game):
        super().__init__(game)
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        # Create Game objects
        self.sprites.add(Background())
        self.sprites.add(Title())
        # Adding buttons
        self.buttons = []
        self.selected_button = 0
        self.create_buttons()
        # Background music
        if sys.platform == "emscripten":
            self.music = utils.assets.get_audio("menu.ogg")
            self.select_sound = utils.assets.get_audio("select.ogg")
            self.enter_sound = utils.assets.get_audio("enter.ogg")
        else:
            self.music = utils.assets.get_audio("menu.wav")
            self.select_sound = utils.assets.get_audio("select.wav")
            self.enter_sound = utils.assets.get_audio("enter.wav")
        
    def start(self):
        self.game.set_state(Level(self.game))
    
    def options(self):
        self.game.set_state(Option(self.game))
    
    def credits(self):
        self.game.set_state(Ending(self.game))
    
    def quit(self):
        self.game.quit()
        
    def create_buttons(self):
        """ Create buttons objects
        """
        menu_items = [
            {
                'title' : 'Start',
                'action' : lambda: self.start(),
            },
            {
                'title' : 'Options',
                'action' : lambda: self.options(),
            },
            {
                'title' : 'Credits',
                'action' : lambda: self.credits(),
            },
            {
                'title' : 'Quit',
                'action' : lambda: self.quit(),
            }
        ]
        button_total_height = len(menu_items) * (configs.BUTTON_HEIGHT + configs.BUTTON_SPACING)
        starting_x = (configs.SCREEN_WIDTH - configs.BUTTON_WIDTH) // 2
        starting_y = (configs.SCREEN_HEIGHT - button_total_height) // 1.8
        for item in menu_items:
            button = Button(starting_x, starting_y, configs.BUTTON_WIDTH, configs.BUTTON_HEIGHT, item["title"], item["action"])
            starting_y += configs.BUTTON_HEIGHT + configs.BUTTON_SPACING
            self.sprites.add(button)
            self.buttons.append(button)
            
    def change_selection(self, direction):
        self.select_sound.play()
        self.selected_button = (self.selected_button + direction) % len(self.buttons)
        for i, button in enumerate(self.buttons):
            button.active = (i == self.selected_button)
        
    def render(self):
        self.sprites.draw(self.game.screen)
    
    def update(self, dt):
        self.sprites.update(dt)
        
    def handle_event(self, event):
        self.handle_button_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.change_selection(1)
            elif event.key == pygame.K_UP:
                self.change_selection(-1)
            elif event.key == pygame.K_RETURN:
                self.enter_sound.play()
                if self.selected_button == 0:  # Start button
                    self.start()
                elif self.selected_button == 1:  # Options button
                    self.options()
                elif self.selected_button == 2:  # Credits button
                    self.credits()
                elif self.selected_button == 3:  # Quit button
                    self.quit()
                    
    def handle_button_event(self, event):
        for button in self.buttons:
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.enter_sound.play()
                    button.action()
                    
    def enter_state(self):
        self.music.set_volume(self.game.music_volume)
        self.select_sound.set_volume(self.game.sound_volume)
        self.enter_sound.set_volume(self.game.sound_volume)
        self.music.play(loops = -1)
        
    def exit_state(self):
        self.music.fadeout(1000)
        self.game.fadein()