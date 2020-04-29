from axelrod.action import Action
from axelrod.player import Player
from axelrod.random_ import random_choice


class RandomImproved(Player):

    name = "RandomImproved"
    classifier = {
        "memory_depth": 1,  # Memory-one Four-Vector = (p, p, p, p)
        "stochastic": True,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self, p: float = 0.5) -> None:
        """
        Parameters
        ----------
        p, float
            The probability to cooperate

        Special Cases
        -------------
        Random(0) is equivalent to Defector
        Random(1) is equivalent to Cooperator
        """
        super().__init__()
        self.p = p
        if p in [0, 1]:
            self.classifier["stochastic"] = False

    def strategy(self, opponent: Player) -> Action:
        # First move
        if len(self.history) == 0:
            return random_choice(self.p)
        elif self.p > 0.7:
            return random_choice(self.p)
        elif (self.history[-1] == C and opponent.history[-1] == C):
            return C
        elif (self.history[-1] == D and opponent.history[-1] == C):
            return D
        elif (self.history[-1] == C and opponent.history[-1] == D):
            return D
        elif (self.history[-1] == D and opponent.history[-1] == D):
            return C
        return random_choice(self.p)

