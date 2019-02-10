from Game.Game import Engine
from Game.Players import Player, HumanPlayer, AiPlayer
from Game.tactics import *

if __name__ == "__main__": #Working prototype
    ps = [AiPlayer(0, always_cheat), AiPlayer(1, always_coop), AiPlayer(2, always_copy), AiPlayer(3, always_rdm)] # One Ai for each tactic
    cE = Engine([p.id for p in ps]) #init Engine
    for i in range(1000): #each Agent agaist each agent (inluding himself) 1k times
        for p1 in ps:
            for p2 in ps:
                cE.make_moves(p1, p2)
    print(cE.scores) #print scores