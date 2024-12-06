class Player:
    def __init__(self, stg, axis):
        self.stg = stg
        self.axis = bool(int(axis) % 2)
        self.pastWts  = None
        self.pastActs = []
    
    def __repr__(self):
        return f"{sum(self.pastActs)}"
    
    def makeChoice(self, wts):
        if self.axis:
            wts = list(map(lambda a: wts[a], [0, 2, 1, 3]))
        
        choice = self.stg(wts=wts, past=self.pastWts, acts=self.pastActs)
        self.pastWts = wts
        
        return choice
    
    def wins(self, val):
        self.pastActs += [val]

    def data(self):
        return {'points': sum(self.pastActs), 'actions': self.pastActs}