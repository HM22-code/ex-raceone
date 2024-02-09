class State():
    """ State class for all states
    """
    
    def __init__(self, game):
        self.game = game
        
    def run(self):
        """ Called on every frames
        """
        pass
    
    def process_input(self):
        # TODO: Process event input
        pass
    
    def update(self):
        # TODO: Process update
        pass
    
    def render(self):
        # TODO: Process render
        pass
    
    def enter_state(self):
        """ Called when the state becomes the current state
        """
        pass
    
    def exit_state(self):
        """ Called when the state is no longer the current state
        """
        pass
    
    def handle_event(self, event):
        """ Handle event for the current state
        """
        pass