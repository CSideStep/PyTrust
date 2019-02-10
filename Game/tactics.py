from typing import List
from random import choice

def always_cheat(id:int, games:List[tuple]):
    return 0

def always_coop(id:int, games:List[tuple]):
    return 1

def always_rdm(id:int, games:List[tuple]):
    return choice([0, 1])

def always_copy(id:int, games:List[tuple]):
    last_game = games[-1]
    if id in last_game.keys():
        for key in last_game.keys():
            if not key == id:
                return last_game[key]
    else:
        return choice([0, 1])