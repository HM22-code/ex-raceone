import pygame
import assets
from objects.level import Level
from objects.player import Player
from objects.background import Background
from objects.floor import Floor
from objects.game_start_message import GameStartMessage
from objects.state import State

class Start(State):
    
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
        GameStartMessage(self.sprites)
        
        # Background music
        self.music = assets.get_audio("menu")
        self.music.set_volume(0.3)
        self.music.play(loops = -1)
    
    def run(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.music.stop()
            self.game_state_manager.set_state(Level(self.display, self.game_state_manager))
        
        self.display.fill('blue')
        self.sprites.draw(self.display)
        self.sprites.update()