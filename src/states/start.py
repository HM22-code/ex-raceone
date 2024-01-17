import pygame
import assets
from states.level import Level
from objects.background import Background
from objects.floor import Floor
from objects.game_start_message import GameStartMessage
from classes.state import State

class Start(State):
    
    def __init__(self, display, state_manager):
        self.display = display
        self.state_manager = state_manager
        
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        
        # Create Game objects
        Background(0, self.sprites)
        Background(1, self.sprites)
        Floor(0, self.sprites)
        Floor(1, self.sprites)
        GameStartMessage(self.sprites)
        
        # Background music
        self.music = assets.get_audio("menu")
        self.music.set_volume(0.3)
    
    def run(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.state_manager.set_state(Level(self.display, self.state_manager))
        
        self.sprites.draw(self.display)
        self.sprites.update()
        
    def enter_state(self):
        self.music.play(loops = -1)
    
    def exit_state(self):
        self.music.stop()