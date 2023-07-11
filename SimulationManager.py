from Engine import *
from Config import Config
from Player import *
import uuid
import datetime

def print_and_return(*args):
    args = [str(i for i in args)]
    print(*args)
    return " ".join(args) + "\n"

class SimulationManager:
    def __init__(self, players : dict, config : dict):
        self.players = players
        self.config = config


    def create_ranklist(self, ranklist: dict):
        self.ranklist = {}
        for player in self.players.keys():
            self.ranklist[player] = 0

    def run_simulation(self, player_1, player_2):
        eng = Engine(

            **self.config.get_conf(),
            player_1=player_1,
            player_2=player_2
        )

        return eng.run()

    def run(self):
        results = "Input: \n"
        conf = self.config.get_conf()
        for key in self.config.get_conf():
            results += f"{key}: {conf[key]}\n"
        results += "\n-----------------------\nOutput: \n"

        p = list(self.players.keys())
        for _ in range(len(p)):
            p1 = p.pop(0)
            for p2 in p:
                print(p1, "plays with", p2)
                res_p1, res_p2 = self.run_simulation(self.players[p1], self.players[p2])
                print(p1, "gains " if res_p1 > 0 else "lost", res_p1, "points ")
                print(p2, "gains "if res_p2 > 0 else "lost", res_p2, "points ")
                self.ranklist[p1] += res_p1
                self.ranklist[p2] += res_p2
                print(p1, "now has", self.ranklist[p1])
                print(p2, "now has", self.ranklist[p2])

        for player in self.ranklist.keys():
            results += print_and_return(player, " - ", self.ranklist[player])

        filename = str(datetime.datetime.now())
        filename = filename.replace(" ", "_").replace(":", "_") + ".txt"
        with open(filename, "w") as file:
            file.write(results)
