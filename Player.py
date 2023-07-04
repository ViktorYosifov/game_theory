from pick import pick
import random
class Player:
    def __init__(self, spoints: int,  pwn: int, pwp: int, plp: int, pln: int):
        self.pln = pln
        self.plp = plp
        self.pwp = pwp
        self.pwn = pwn
        self.decision = None
        self.points = spoints
        self.name = self.__class__.__name__
    @classmethod
    def create_from_engine(cls, spoints, pwn, pwp, plp, pln):
        return cls(spoints, pwn, pwp, plp, pln)
    def make_decision(self, positive: bool):
        self.positive = positive
    def outcome(self, win: bool):
        positive = self.positive
        if positive and win:
            print(f"{self.name} wins with a positive decision!")
            self.points += self.pwp
        elif positive and not win:
            print(f"{self.name} loses with a positive decision!")
            self.points -= self.plp
        elif not positive and win:
            print(f"{self.name} wins with a negative decision!")
            self.points += self.pwn
        elif not positive and not win:
            print(f"{self.name} loses with negative decision!")
            self.points -= self.pln

class Socializer(Player):
    def make_decision(self, **kwargs):
        super().make_decision(True)

class CopyPlayer(Player):
    def make_decision(self, **kwargs):
        previous_decision = kwargs['previous_decision']
        if previous_decision == True:
            super().make_decision(True)
        else:
            super().make_decision(False)

class Killer(Player):
    def make_decision(self, **kwargs):
        super().make_decision(False)

class CustomPlayer(Player):
    def make_decision(self, **kwargs):
        dec = bool(int(input("Enter 1 for a positive decision and 0 for a negative decision: ")))
        super().make_decision(dec)

class RandomPlayer(Player):
    def make_decision(self, **kwargs):
        positive = random.choice([True, False])
        super().make_decision(positive)