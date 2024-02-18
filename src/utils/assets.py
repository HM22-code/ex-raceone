import os
import pygame

sprites = {}
audios = {}
fonts = {}

def load_sprites():
    """ Load all sprites from assets/images/
    """
    path = os.path.join(os.path.abspath(os.curdir), "assets", "images")
    for file in os.listdir(path):
        sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file)).convert_alpha()

def load_sprite(file):
    """ Load a sprite from assets/images/ from file

    Args:
        file (_type_): file

    Returns:
        _type_: image
    """
    path = os.path.join(os.path.abspath(os.curdir), "assets", "images")
    return pygame.image.load(os.path.join(path, file)).convert_alpha()
        
def get_sprite(name):
    """ Get sprite from name

    Args:
        name (_type_): string

    Returns:
        _type_: image
    """
    return sprites[name]

def load_audios():
    """ Load all audios from assets/audios/
    """
    path = os.path.join(os.path.abspath(os.curdir), "assets", "audios")
    for file in os.listdir(path):
        audios[file.split('.')[0]] = pygame.mixer.Sound(os.path.join(path, file))
        
def load_audio(file):
    """ Load an audio from assets/audios/ from file

    Args:
        file (_type_): file

    Returns:
        _type_: audio
    """
    path = os.path.join(os.path.abspath(os.curdir), "assets", "audios")
    return pygame.mixer.Sound(os.path.join(path, file))
        
def get_audio(name):
    """ Get audio from name

    Args:
        name (_type_): string

    Returns:
        _type_: audio
    """
    return audios[name]

def load_fonts():
    """ Load all fonts from assets/fonts/ with default font size
    """
    path = os.path.join(os.path.abspath(os.curdir), "assets", "fonts")
    for file in os.listdir(path):
        fonts[file.split('.')[0]] = pygame.font.Font(os.path.join(path, file), 36)
        
def load_font(file, size):
    """ Load a font from assets/fonts/ from file

    Args:
        file (_type_): file
        size (_type_): int

    Returns:
        _type_: font
    """
    path = os.path.join(os.path.abspath(os.curdir), "assets", "fonts")
    return pygame.font.Font(os.path.join(path, file), size)
    
        
def get_font(name):
    return fonts[name]
    