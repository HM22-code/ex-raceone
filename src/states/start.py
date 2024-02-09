import pygame
import assets
import configs
from objects.button import Button
from states.ending import Ending
from objects.background import Background
from objects.title import Title
from classes.state import State
from states.menu import Menu
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
        Background(self.sprites)
        Title(self.sprites)
        # Adding buttons
        self.buttons = []
        self.create_buttons()
        # Background music
        self.music = assets.get_audio("menu")
        self.music.set_volume(0.3)
        
    def create_buttons(self):
        """ Create buttons objects
        """
        button_texts = ["Start", "Options", "Credits", "Quit"]
        button_total_height = len(button_texts) * (configs.BUTTON_HEIGHT + configs.BUTTON_SPACING)
        starting_x = (configs.SCREEN_WIDTH - configs.BUTTON_WIDTH) // 2
        starting_y = (configs.SCREEN_HEIGHT - button_total_height) // 2
        for text in button_texts:
            button = Button(starting_x, starting_y, configs.BUTTON_WIDTH, configs.BUTTON_HEIGHT, text, self.sprites)
            starting_y += configs.BUTTON_HEIGHT + configs.BUTTON_SPACING
            self.buttons.append(button)
    
    def run(self):
        # Draw
        self.sprites.draw(self.game.screen)
        # Update
        self.sprites.update()
        
    def handle_event(self, event):
        mx, my = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.buttons[0].rect.collidepoint((mx, my)):
                self.game.set_state(Menu(self.game))
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