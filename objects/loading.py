from objects.state import State

class Loading(State):
    
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager
    
    def run(self):
        self.display.fill('black')