import pygame
import assets
import configs
from objects.button import Button
from states.ending import Ending
from states.level import Level
from objects.background import Background
from objects.floor import Floor
from objects.title import Title
from classes.state import State
from states.option import Option

class Start(State):
    """ Start state class

    Args:
        State (_type_): state
    """
    
    BUTTON_WIDTH = 200
    BUTTON_HEIGHT = 50
    BUTTON_SPACING = 20
    
    def __init__(self, game):
        super().__init__(game)
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        # Create Game objects
        Background(self.sprites)
        Title(self.sprites)
        # Adding buttons
        self.buttons = []
        self.create_buttons()
        # Background music
        self.music = assets.get_audio("menu")
        self.music.set_volume(0.3)
        
    def create_buttons(self):
        
        button_texts = ["Start", "Options", "Credits", "Quit"]
        button_total_height = len(button_texts) * (self.BUTTON_HEIGHT + self.BUTTON_SPACING)
        starting_x = (configs.SCREEN_WIDTH - self.BUTTON_WIDTH) // 2
        starting_y = (configs.SCREEN_HEIGHT - button_total_height) // 2
        for text in button_texts:
            button = Button(starting_x, starting_y, self.BUTTON_WIDTH, self.BUTTON_HEIGHT, text, self.sprites)
            starting_y += self.BUTTON_HEIGHT + self.BUTTON_SPACING
            self.buttons.append(button)
    
    def run(self):
        # Draw
        self.sprites.draw(self.game.screen)
        # Update
        self.sprites.update()
        
    def handle_event(self, event):
        mx, my = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.game.set_state(Level(self.game))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.buttons[0].rect.collidepoint((mx, my)):
                self.game.set_state(Level(self.game))
            if self.buttons[1].rect.collidepoint((mx, my)):
                self.game.set_state(Option(self.game))
            if self.buttons[2].rect.collidepoint((mx, my)):
                self.game.set_state(Ending(self.game))
            if self.buttons[3].rect.collidepoint((mx, my)):
                self.game.quit()
        
    def enter_state(self):
        self.music.play(loops = -1)
    
    def exit_state(self):
        self.music.stop()