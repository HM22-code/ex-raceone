from enum import IntEnum, auto
import pygame 

class Events(IntEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return pygame.USEREVENT + count
    MOUSEHOVER = auto()