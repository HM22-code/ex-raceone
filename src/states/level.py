import pygame
from objects.parallax_background import ParallaxBackground
from objects.parallax_layer import ParallaxLayer
from enums.events import Events
from objects.drone import Drone
from objects.plane import Plane
from objects.robot import Robot
import utils.assets
import random
import configs
from objects.player import Player
from interfaces.state import State

class Level(State):
    """ Level state class

    Args:
        State (_type_): state
    """
    
    def __init__(self, game):
        super().__init__(game)
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        # Game objects
        self.sprites.add(ParallaxBackground(0))
        self.sprites.add(ParallaxLayer(2, 0))
        self.sprites.add(ParallaxLayer(2, 1))
        self.sprites.add(ParallaxLayer(3, 0))
        self.sprites.add(ParallaxLayer(3, 1))
        self.sprites.add(ParallaxLayer(4, 0))
        self.sprites.add(ParallaxLayer(4, 1))
        self.player = Player(self.sprites)
        self.sprites.add(self.player)
        # Import music and sounds
        self.music = utils.assets.get_audio("level1.wav")
        self.shoot_sound = utils.assets.get_audio("sfx_wpn_laser8.wav")
    
    def render(self):
        self.sprites.draw(self.game.screen)
    
    def update(self, dt):
        self.sprites.update(dt)
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.set_state(self.game.get_previous_state())
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.player.shoot()
            self.shoot_sound.play()
        if event.type == Events.ENEMY:
            match random.choice(["Drone", "Robot", "Plane"]):
                case "Drone":
                    enemy = Drone(configs.SCREEN_WIDTH, random.randint(0, configs.SCREEN_HEIGHT))
                case "Robot":
                    enemy = Robot(configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT - 40)
                case "Plane":
                    enemy = Plane(configs.SCREEN_WIDTH, random.randint(0, configs.SCREEN_HEIGHT // 4))
            self.sprites.add(enemy)
        
    def enter_state(self):
        self.shoot_sound.set_volume(self.game.sound_volume)
        self.music.set_volume(self.game.music_volume)
        self.music.play(loops = -1)
    
    def exit_state(self):
        self.music.stop()