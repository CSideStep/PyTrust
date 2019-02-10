from typing import List
class Player:
    id:int
    def __init__(self, id):
        self.id=id
    def make_play(self, games:List[tuple]):
        pass

class HumanPlayer(Player): # Human player
    def __init__(self, id):
        super().__init__(id)
    def make_play(self, games:List[tuple]):
        action = -1
        while not action in ["0", "1"]:
            print("Choose your action")
            action = input()
        return int(action)

class AiPlayer(Player): #tactic function dictates behavior 
    def __init__(self, id:int, tactic):
        super().__init__(id)
        self.tactic = tactic
    def make_play(self, games:List[tuple]):
        return self.tactic(self.id, games)