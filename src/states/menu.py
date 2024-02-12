import pygame
import configs
from classes.state import State
from objects.background import Background
from objects.button import Button
from objects.title import Title
from states.level import Level
from states.level_three import LevelThree
from states.level_two import LevelTwo

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
        self.game.set_state(Level(self.game))
    
    def level2(self):
        self.game.set_state(LevelTwo(self.game))
    
    def level3(self):
        self.game.set_state(LevelThree(self.game))
    
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
        mx, my = pygame.mouse.get_pos()
        for button in self.buttons:
            # Check if hover
            if button.rect.collidepoint((mx, my)):
                # Check if click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button.action()
                button.active = True
            else: 
                button.active = False
            
        
    