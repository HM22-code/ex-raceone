import os
import pygame

sprites = {}

def load_sprites():
    path = os.path.join(os.path.abspath(os.curdir), "assets", "sprites")
    for file in os.listdir(path):
        sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file)).convert()
        
def get_sprite(name):
    return sprites[name]