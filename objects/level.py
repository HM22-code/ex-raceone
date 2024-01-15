import pygame
import assets
from objects.player import Player
from objects.background import Background
from objects.floor import Floor
from objects.state import State

class Level(State):
    
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager
        
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        
        # Create Game objects
        Background(0, self.sprites)
        Background(1, self.sprites)
        Floor(0, self.sprites)
        Floor(1, self.sprites)
        Player(self.sprites)
        
        # Background music
        self.music = assets.get_audio("level1")
        self.music.set_volume(0.3)
    
    def run(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.game_state_manager.set_state(self.game_state_manager.get_previous_state())
        
        self.sprites.draw(self.display)
        self.sprites.update()
        
    def enter_state(self):
        self.music.play(loops = -1)
    
    def exit_state(self):
        self.music.stop()