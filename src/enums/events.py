from enum import IntEnum
import pygame

class Events(IntEnum):
    MOUSEHOVER = pygame.USEREVENT + 1
    ENEMY = pygame.USEREVENT + 2