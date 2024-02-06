import pygame
import configs
from classes.state import State
from objects.background import Background
from objects.button import Button
from objects.title import Title
from states.level import Level
from states.level_three import LevelThree
from states.level_two import LevelTwo
from states.start import Start


class Menu(State):
    
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
        
    def create_buttons(self):
        
        button_texts = ["Level 1", "Level 2", "Level 3"]
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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.set_state(Start(self.game))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.buttons[0].rect.collidepoint((mx, my)):
                self.game.set_state(Level(self.game))
            if self.buttons[1].rect.collidepoint((mx, my)):
                self.game.set_state(LevelTwo(self.game))
            if self.buttons[2].rect.collidepoint((mx, my)):
                self.game.set_state(LevelThree(self.game))
            
        
    