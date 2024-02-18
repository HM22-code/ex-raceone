import pygame
from enums.events import Events

class MOUSEHOVER(pygame.event.Event(Events.MOUSEHOVER)):
    
    def __init__(self):
        super().__init__()