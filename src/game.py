from random import choice

chr = lambda a: a*choice([1, -1])

class Game:
    def __init__(self, wts):
        self.wts = wts
    
    def setPlayers(self, player1, player2):
        self.plr1 = player1
        self.plr2 = player2
    
    def setDelta(self, delta):
        if delta == 0:
            self.updateWts = lambda: self.wts
        else:
            self.delta = (delta%101)/100
            self.updateWts = lambda: [[i+chr(self.delta), j+chr(self.delta)] for i, j in self.wts]
        
    def play(self):
        self.wts = self.updateWts()
        out1 = self.plr1.makeChoice(self.wts)
        out2 = self.plr2.makeChoice(self.wts)

        for i in range(4):
            if (i//2) != out1: continue
            if (i% 2) != out2: continue
            win1, win2 = self.wts[i]

        self.plr1.wins(win1)
        self.plr2.wins(win2)
    
    def points(self):
        print(f"Player1: {self.plr1}\nPlayer2: {self.plr2}")
        return [self.plr1.data(), self.plr2.data()]
