from enum import IntEnum, auto
import pygame

class Events(IntEnum):
    """ Enum of custom events

    Args:
        IntEnum (_type_): Int enumeration
    """
    MOUSEHOVER = pygame.USEREVENT + 1
    ENEMY = auto()