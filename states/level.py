from objects.parallax_background import ParallaxBackground
from objects.parallax_layer import ParallaxLayer
from objects.player import Player
from objects.enemy import Enemy
from objects.text import Text
from enums.events import Events
from interfaces.state import State
from states.over import Over
import utils.assets
import pygame
import random
import configs
import sys

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
        # Game level properties
        self.game.score = 0
        self.game.life = 3
        self.font = "score.ttf"
        self.score_ui = Text(10, 5, str(self.game.score), self.font, 10, pygame.color.Color("white"))
        self.sprites.add(self.score_ui)
        self.life_ui = Text(configs.SCREEN_WIDTH - 50, 5, str(self.game.life)+" x A", self.font, 10, pygame.color.Color("white"))
        self.sprites.add(self.life_ui)
        # Import music and sounds
        if sys.platform == "emscripten":
            self.music = utils.assets.get_audio("level.ogg")
            self.shoot_sound = utils.assets.get_audio("laser.ogg")
            self.explosion_sound = utils.assets.get_audio("explosion.ogg")
            self.gameover_sound = utils.assets.get_audio("gameover.ogg")
            self.hit_sound = utils.assets.get_audio("hit.ogg")
        else:
            self.music = utils.assets.get_audio("level.wav")
            self.shoot_sound = utils.assets.get_audio("laser.wav")
            self.explosion_sound = utils.assets.get_audio("explosion.wav")
            self.gameover_sound = utils.assets.get_audio("gameover.wav")
            self.hit_sound = utils.assets.get_audio("hit.wav")
    
    def render(self):
        self.sprites.draw(self.game.screen)
    
    def update(self, dt):
        self.sprites.update(dt)
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.set_state(self.previous_state)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.player.shoot()
            self.shoot_sound.play()
        if event.type == Events.ENEMY:
            enemy = Enemy(configs.SCREEN_WIDTH, random.randint(0, configs.SCREEN_HEIGHT-29))
            self.enemies.add(enemy)
            self.sprites.add(enemy)
        # Check for collisions
        for enemy in pygame.sprite.groupcollide(self.enemies, self.bullets, True, True):
            self.explosion_sound.play()
            self.game.score += 5
            self.score_ui.text = str(self.game.score) 
        for enemy in pygame.sprite.groupcollide(self.enemies, self.players, True, False):
            self.hit_sound.play()
            self.game.life -= 1
            if self.game.life < 0 :
                self.gameover()
            self.life_ui.text = str(self.game.life)+" x A"
    
    def gameover(self):
        """ Go to Over state
        """
        self.player.kill()
        self.gameover_sound.play()
        self.game.fadein()
        self.game.set_state(Over(self.game))
        
    def enter_state(self):
        self.shoot_sound.set_volume(self.game.sound_volume)
        self.explosion_sound.set_volume(self.game.sound_volume)
        self.gameover_sound.set_volume(self.game.sound_volume)
        self.hit_sound.set_volume(self.game.sound_volume)
        self.music.set_volume(self.game.music_volume)
        self.music.play(loops = -1)
        pygame.mouse.set_visible(False)
    
    def exit_state(self):
        self.music.stop()
        pygame.mouse.set_visible(True)