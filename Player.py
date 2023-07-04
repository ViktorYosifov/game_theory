class Player:
    def __init__(self, spoints: int):
        self.decision = None
        self.spoints = spoints
        
    def make_decision(self, positive: bool):
        if positive:
            self.decision = "positive" 
        