from enum import IntEnum, auto
import pygame 

class Events(IntEnum):
    MOUSEHOVER = pygame.USEREVENT + auto()