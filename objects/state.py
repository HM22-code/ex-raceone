class State():
    
    def __init__(self, game):
        self.game = game
        self.prev_state = None
        
    def run(self):
        '''
        Running in game loop
        '''
        pass
    
    def enter_state(self):
        '''
        Running start
        '''
        pass
    
    def exit_state(self):
        '''
        Running end
        '''
        pass