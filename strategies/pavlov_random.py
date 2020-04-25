from axelrod.action import Action
from axelrod.player import Player
from axelrod.random_ import random_choice
import random

C, D = Action.C, Action.D


class PavlovRandom(Player):
    
    name = "Alternator"
    classifier = {
        "memory_depth": 1,
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def random():
        r = random.random()
        if r < p:
            return C
        return D


    def strategy(self, opponent: Player) -> Action:
	if not self.history or random.random() < 0.05:
            return self.random()
        if(self.history[-1] == C and opponent.history[-1] == C):
            return C
        if(self.history[-1] == D and opponent.history[-1] == C):
            return D
        return self.history[-1].flip()
