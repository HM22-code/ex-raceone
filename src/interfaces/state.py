import pygame
import configs
from abc import ABC, abstractmethod

class State(ABC):
    """ State class for all states
    """
    
    def __init__(self, game):
        self.game = game
     
    @abstractmethod   
    def run(self):
        """ Called on every frames
        """
        pass
    
    @abstractmethod 
    def process_input(self):
        """ Called to process input event for the current state
        """
        pass
    
    @abstractmethod 
    def update(self):
        """ Called on every frames to update the current state screen
        """
        pass
    
    @abstractmethod 
    def render(self):
        """ Called on every frames to render graphics for the current state
        """
        pass
    
    @abstractmethod 
    def enter_state(self):
        """ Called when the state becomes the current state
        """
        pass
    
    @abstractmethod 
    def exit_state(self):
        """ Called when the state is no longer the current state
        """
        pass
    
    @abstractmethod 
    def handle_event(self, event):
        """ Handle event for the current state
        """
        pass
            
            