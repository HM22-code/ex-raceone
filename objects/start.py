import pygame
import assets
from objects.player import Player
from objects.background import Background
from objects.floor import Floor
from objects.game_start_message import GameStartMessage

class Start():
    
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
        Player(self.sprites)
        
        # Background music
        '''
        music = assets.get_audio("menu")
        music.set_volume(0.3)
        music.play(loops = -1)
        '''
    
    def run(self):
        self.display.fill('blue')
        self.sprites.draw(self.display)
        self.sprites.update()