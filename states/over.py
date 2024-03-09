from interfaces.state import State
from objects.text import Text
import pygame
import configs

class Over(State):
    """ Over state class

    Args:
        State (_type_): state
    """
    
    def __init__(self, game):
        super().__init__(game)
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        # Create Game objects
        self.title_font = "bit.ttf"
        self.upper_font = "score.ttf"
        self.lower_font = "retro.ttf"
        self.gameover_text = Text(configs.SCREEN_WIDTH // 2 - 75, configs.SCREEN_HEIGHT // 6, "Game Over", self.title_font, 40, pygame.color.Color("white"))
        self.score_text = Text(configs.SCREEN_WIDTH // 2 - 60, configs.SCREEN_HEIGHT // 2.6, "score : ", self.upper_font, 20, pygame.color.Color("white"))
        self.value_text = Text(configs.SCREEN_WIDTH // 2 + 30, configs.SCREEN_HEIGHT // 2.6, str(self.game.score), self.upper_font, 20, pygame.color.Color("white"))
        self.enter_text = Text(configs.SCREEN_WIDTH // 2 - 70, configs.SCREEN_HEIGHT // 1.2, "press Enter to return menu", self.lower_font , 10, pygame.color.Color("white"))
        self.sprites.add(self.gameover_text)
        self.sprites.add(self.score_text)
        self.sprites.add(self.value_text)
        self.sprites.add(self.enter_text)
        
    def render(self):
        self.game.screen.fill(pygame.color.Color("black"))
        self.sprites.draw(self.game.screen)
    
    def update(self, dt):
        self.sprites.update(dt)
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.game.set_state(self.game.get_previous_state().previous_state)

    def enter_state(self):
        pygame.mouse.set_visible(False)
    
    def exit_state(self):
        self.game.fadein()
        pygame.mouse.set_visible(True)