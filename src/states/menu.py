import pygame
import configs
from interfaces.state import State
from objects.background import Background
from objects.button import Button
from objects.title import Title
from states.level1 import Level1
from states.level2 import Level2
from states.level3 import Level3

class Menu(State):
    """ Menu state class

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
        
    def level1(self):
        self.game.set_state(Level1(self.game))
    
    def level2(self):
        self.game.set_state(Level2(self.game))
    
    def level3(self):
        self.game.set_state(Level3(self.game))
    
    def create_buttons(self):
        """ Create buttons objects
        """
        menu_items = [
            {
                'title' : 'Level 1',
                'action' : lambda: self.level1(),
            },
            {
                'title' : 'Level 2',
                'action' : lambda: self.level2(),
            },
            {
                'title' : 'Level 3',
                'action' : lambda: self.level3(),
            }
        ]
        button_total_height = len(menu_items) * (configs.BUTTON_HEIGHT + configs.BUTTON_SPACING)
        starting_x = (configs.SCREEN_WIDTH - configs.BUTTON_WIDTH) // 2
        starting_y = (configs.SCREEN_HEIGHT - button_total_height) // 2
        for item in menu_items:
            button = Button(starting_x, starting_y, configs.BUTTON_WIDTH, configs.BUTTON_HEIGHT, item["title"], item["action"], self.sprites)
            starting_y += configs.BUTTON_HEIGHT + configs.BUTTON_SPACING
            self.buttons.append(button)
            
    def run(self):
        # Draw
        self.sprites.draw(self.game.screen)
        # Update
        self.sprites.update()
    
    def handle_event(self, event):
        for button in self.buttons:
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button.action()
         
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
    
    def fadein(self):
        super().fadein()
    
    def fadeout(self):
        super().fadeout()
            
        
    