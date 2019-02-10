from typing import List, Dict
from Game.Players import Player
class Engine:
    games:List[Dict[int, int]]
    scores:Dict[int, int]
    def __init__(self, ids:List[int]):
        self.games = []
        self.scores = dict()
        for id in ids:
            self.scores[id]=0
    
    def play_game(self, move1:int, move2:int, id1:int, id2:int): #fundamental game logic
        if move1 == 1 and move2 == 1:
            game = {id1:2, id2:2}
        elif move1 == 0 and move2 == 0:
            game = {id1:0, id2:0}
        elif move2 == 1:
            game = {id1:3, id2:-1}
        else:
            game = {id1:-1, id1:3}
        self.games.append(game)
        for key in game.keys():
            self.scores[key]+=game[key]
        return game

    def make_moves(self, player1:Player, player2:Player): #play a game with 2 Players
        return self.play_game(player1.make_play(self.games), player2.make_play(self.games), player1.id, player2.id)