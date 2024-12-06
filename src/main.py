from game import Game
from player import Player
from strats import *

class Tournament:
    def __init__(self, game, player1, player2, delta = 0):
        self.game = game
        self.game.setPlayers(player1, player2)
        self.game.setDelta(delta)
    
    def run(self, rounds = 100):
        for i in range(rounds):
            self.game.play()
        return self.game.points()

def main():
    plr1 = Player(llm, 0)
    plr2 = Player(stg, 1)
    game = Game([[0, 0], [1, 0], [0, 1], [3, 3]])
    Tournament(game, plr1, plr2, 10).run()
    
if __name__ == '__main__':
    main()