import pygame
from objects.parallax_background import ParallaxBackground
from objects.parallax_layer import ParallaxLayer
from enums.events import Events
from objects.enemy import Enemy
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
        self.players = pygame.sprite.GroupSingle()
        # Game objects
        self.sprites.add(ParallaxBackground(0))
        self.sprites.add(ParallaxLayer(2, 0))
        self.sprites.add(ParallaxLayer(2, 1))
        self.sprites.add(ParallaxLayer(3, 0))
        self.sprites.add(ParallaxLayer(3, 1))
        self.sprites.add(ParallaxLayer(4, 0))
        self.sprites.add(ParallaxLayer(4, 1))
        self.player = Player(self.bullets, self.sprites)
        self.players.add(self.player)
        self.sprites.add(self.player)
        # Import music and sounds
        self.music = utils.assets.get_audio("level1.wav")
        self.shoot_sound = utils.assets.get_audio("sfx_wpn_laser8.wav")
        self.explosion_sound = utils.assets.get_audio("explosion.wav")
    
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
            match random.choice(["Enemy"]):
                case "Enemy":
                    enemy = Enemy(configs.SCREEN_WIDTH, random.randint(0, configs.SCREEN_HEIGHT))
            self.enemies.add(enemy)
            self.sprites.add(enemy)
        # Check for collisions
        for enemy in pygame.sprite.groupcollide(self.enemies, self.bullets, True, True):
            self.explosion_sound.play()
        for enemy in pygame.sprite.groupcollide(self.enemies, self.players, True, False):
            self.explosion_sound.play()
        
    def enter_state(self):
        self.shoot_sound.set_volume(self.game.sound_volume)
        self.explosion_sound.set_volume(self.game.sound_volume)
        self.music.set_volume(self.game.music_volume)
        self.music.play(loops = -1)
    
    def exit_state(self):
        self.music.stop()